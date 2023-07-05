import streamlit as st
import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(layout="wide", page_title="Brooklyn Surveillance Metric (Racial & Ethnic Communities)")
st.title("Raw Surveillance Metric for Each Racial and Ethnic Groups")
st.write(
    ("Distribution of our surveillance metric for each racial group across census tracts.")
)

# Step 1: Load and preprocess the data
@st.cache_data
def load_data():
    filepath = "/Users/rahnumatarannum/bk_defenders_surveillance_capstone/Outputs/tract_racial_ethnic_surveillance.shp"
    df = gpd.read_file(filepath)
    return df

df = load_data()

# Rename the columns
df = df.rename(columns={
    'White, n_3': 'White, not hispanic',
    'Black or_3': 'Black or African American, not hispanic',
    'Asain, n_3': 'Asian, not hispanic',
    'Hispanic_3': 'Hispanic or Latino',
    'Other Ra_3': 'Other Races, not hispanic'
})

# Filter the data for non-null values in the selected columns
filtered_df = df[['White, not hispanic', 'Black or African American, not hispanic', 'Asian, not hispanic',
                  'Hispanic or Latino', 'Other Races, not hispanic']].dropna()

# Display the density plots
selected_races = st.multiselect('Select Races for Density Plot', filtered_df.columns,
                                default=["White, not hispanic", "Black or African American, not hispanic"])

colors = sns.color_palette("Set1", len(selected_races))

fig, ax = plt.subplots()

for race, color in zip(selected_races, colors):
    values = filtered_df[race]
    avg_value = values.mean()
    st.write(f"Average value for {race}: {avg_value:.2f}")
    sns.kdeplot(values, color=color, label=race, ax=ax)

ax.set_title("Surveillance Metric by Race/Ethnicity")
ax.set_xlabel("Surveillance Metric")
ax.set_ylabel("Density")
ax.legend()

st.pyplot(fig)
