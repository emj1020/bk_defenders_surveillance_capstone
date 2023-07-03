import streamlit as st
import geopandas as gpd
import pandas as pd
import numpy as np
import plotly.express as px


st.set_page_config(layout="wide", page_title="Brooklyn Surveillance Metric (Racial & Ethnic Communities)")
st.title("Raw Surveillance Metric for Each Racial and Ethnic Groups")

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

# Display the histograms
selected_races = st.multiselect('Select Races for Histogram Comparison', filtered_df.columns,
                                default=["White, not hispanic", "Black or African American, not hispanic"])

colors = px.colors.qualitative.Set1[:len(selected_races)]  # Assign colors to each selected race

for race, color in zip(selected_races, colors):
    st.subheader(f'Histogram of {race}')
    values = filtered_df[race]
    avg_value = values.mean()
    st.write(f"Average value: {avg_value:.2f}")
    fig = px.histogram(values, nbins=10, title=f"{race} - Surveillance Metric", color_discrete_sequence=[color])
    fig.update_layout(xaxis_title="Surveillance Metric", yaxis_title="Frequency")
    st.plotly_chart(fig)