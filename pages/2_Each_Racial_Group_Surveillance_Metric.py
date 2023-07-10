import streamlit as st
import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide", page_title="Brooklyn Surveillance Metric (Racial & Ethnic Communities)")
st.title("Raw Surveillance Metric for Each Racial and Ethnic Groups")
st.write("Distribution of our surveillance metric for each racial group across census tracts.")

# Step 1: Load and preprocess the data
@st.cache_data
def load_data():
    filepath = "/Users/rahnumatarannum/bk_defenders_surveillance_capstone/Outputs/tract_racial_ethnic_surveillance.shp"
    df = gpd.read_file(filepath)
    return df

df = load_data()

# Rename the columns
df = df.rename(columns={
    'White, n_3': 'White',
    'Black or_3': 'Black or African American',
    'Asain, n_3': 'Asian',
    'Hispanic_3': 'Hispanic or Latino',
    'Other Ra_3': 'Other Races'
})

# Filter the data for non-null values and values greater than 0 in the selected columns
filtered_df = df[['White', 'Black or African American', 'Asian',
                  'Hispanic or Latino', 'Other Races']].dropna()

# Exclude rows where all values are 0
filtered_df = filtered_df[(filtered_df > 0.0).any(axis=1)]

# Multiselect to choose races for the density plot
selected_races = st.multiselect('Select Races for Density Plot', filtered_df.columns)

# Plot the density line chart for selected races
if selected_races:
    fig, ax = plt.subplots(figsize=(10, 5))
    colors = sns.color_palette("Set1", len(selected_races))

    for race, color in zip(selected_races, colors):
        values = filtered_df[race]
        mean_value = values.mean()
        std_value = values.std()
        sns.kdeplot(values[values > 0.0], color=color, label=race, ax=ax)
        ax.text(0.55, 0.65 - selected_races.index(race) * 0.05, f"{race}'s Surveillance: {mean_value:.2f} +/- {std_value:.2f}", transform=ax.transAxes, ha='left', va='top', color=color)

    ax.set_xlim([0, 1])
    ax.set_xlabel('Surveillance Metric')
    ax.set_title('Surveillance Metric Distribution by Race/Ethnicity')
    ax.legend()

    # Display the plot
    st.pyplot(fig)
else:
    st.write("Please select at least one race for the density plot.")
