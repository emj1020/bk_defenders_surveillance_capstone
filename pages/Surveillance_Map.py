import streamlit as st
import geopandas as gpd
import pandas as pd
import folium
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
from branca.colormap import linear

st.set_page_config(layout="wide", page_title="Brooklyn Surveillance Map")
st.title("Brooklyn Surveillance Metric and Total Cameras in an Interactive Map")

# Step 1: Load and preprocess the data
@st.cache_data
def load_data():
    filepath = "/Users/rahnumatarannum/bk_defenders_surveillance_capstone/Data/nta_surv_metric_TEST_FOR_NUMA/nta_surv_metric_TEST_FOR_NUMA.shp"
    df = gpd.read_file(filepath)
    return df

df = load_data()

# Create a new GeoDataFrame and assign the CRS
valid_df = gpd.GeoDataFrame(df, crs=df.crs)

# Convert "Total Came" column to numeric
valid_df["Total Came"] = pd.to_numeric(valid_df["Total Came"], errors="coerce")

# Step 2: Load the surveillance metric data
metric_filepath = "/Users/rahnumatarannum/bk_defenders_surveillance_capstone/Outputs/kde_final_output.shp"
metric_df = gpd.read_file(metric_filepath)

# Merge the valid_df and metric_df on 'ntaname' column
merged_df = valid_df.merge(metric_df[['ntaname', 'avg_value_']], on='ntaname', how='left')

# Create a linear colormap from yellow to red with more colors based on "avg_value_scaled"
colormap = linear.YlOrRd_09.scale(merged_df['avg_value_'].min(), merged_df['avg_value_'].max())

# Step 3: Create the interactive map
# Create a map centered on Brooklyn
brooklyn_center = [40.650002, -73.949997]
m = folium.Map(location=brooklyn_center, zoom_start=12, tiles="CartoDB positron", width="100%", height=600)

# Define the highlight style for selected and non-selected polygons
highlight_style = {
    'color': 'black',
    'weight': 2,
    'fillOpacity': 0.7
}

non_highlight_style = {
    'color': 'gray',
    'weight': 2,
    'fillOpacity': 0.3
}

# Add GeoJson layer to outline neighborhood boundaries and display name and color based on "avg_value_scaled" column
geojson_layer = folium.GeoJson(
    merged_df,
    name='Neighborhood Boundaries',
    style_function=lambda feature: {
        'fillColor': 'gray' if feature['properties']['Total Came'] <= 2 else colormap(feature['properties']['avg_value_']),
        **non_highlight_style
    },
    highlight_function=lambda x: {'weight': 3, **highlight_style},
    tooltip=folium.features.GeoJsonTooltip(fields=['Total Came', 'avg_value_'], aliases=['Total Cameras', 'Surveillance Metric'], localize=True)
).add_to(m)

# Add neighborhood names as text on the map
for _, row in merged_df.iterrows():
    centroid = row.geometry.centroid
    if row.geometry.contains(centroid):
        folium.Marker(
            location=[centroid.y, centroid.x],
            icon=folium.DivIcon(
                html=f'<div style="font-weight: bold; text-align: center; width: 100%; font-size: 8px;">{row.ntaname}</div>'
            ),
            popup=None
        ).add_to(geojson_layer)

# Add a legend to the right side of the map
colormap.caption = 'Surveillance Metric'
m.add_child(colormap)
m.get_root().html.add_child(folium.Element('<div style="position: fixed; top: 10px; right: 10px; z-index:9999; font-size: 12px; background-color: rgba(255, 255, 255, 0.7); padding: 10px; border-radius: 5px;">' + colormap.caption + '</div>'))

# Create a full-width and larger-height container for the map
map_container = st.container()
with map_container:
    folium_static(m, width=800, height=2000)

# Inject custom CSS to make the map container take up the whole screen
st.markdown(
    """
    <style>
    .fullScreenMap {
        height: 100vh !important;
        width: 100% !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
