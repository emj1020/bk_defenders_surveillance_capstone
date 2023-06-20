import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import folium_static
from shapely.geometry import Polygon
from branca.colormap import linear

st.title("Brooklyn Surveillance Camera's in an Interactive Map")

# Step 1: Load and preprocess the data
@st.cache_data
def load_data():
    df = pd.read_csv('/Users/rahnumatarannum/bk_defenders_surveillance_capstone/Data/nta_surv_metric_TEST_FOR_NUMA.csv')
    # Convert 'geometry' column to GeoDataFrame
    df['geometry'] = gpd.GeoSeries.from_wkt(df['geometry'])
    return df

df = load_data()

# Step 2: Validate geometries and remove invalid ones
valid_geometries = []
valid_names = []
valid_cameras = []
for geometry, name, cameras in zip(df['geometry'], df['ntaname'], df['Total Cameras']):
    if isinstance(geometry, Polygon) and geometry.is_valid:
        valid_geometries.append(geometry)
        valid_names.append(name)
        valid_cameras.append(cameras)

# Create a new GeoDataFrame with valid geometries and assign the CRS
valid_df = gpd.GeoDataFrame(geometry=valid_geometries, crs='EPSG:4326')
valid_df['ntaname'] = valid_names  # Add 'ntaname' column
valid_df.set_index('ntaname', inplace=True)  # Set 'ntaname' as the index
valid_df['Total Cameras'] = valid_cameras

# Calculate the normalized values for the "Total Cameras" column
normalized_cameras = (valid_df['Total Cameras'] - valid_df['Total Cameras'].min()) / (valid_df['Total Cameras'].max() - valid_df['Total Cameras'].min())

# Create a linear colormap from yellow to red
colormap = linear.YlOrRd_09.scale(0, 1)

# Step 3: Create the interactive map
# Create a map centered on Brooklyn
brooklyn_center = [40.650002, -73.949997]
m = folium.Map(location=brooklyn_center, zoom_start=12, tiles='CartoDB positron')

# Define the highlight style for selected and non-selected polygons
highlight_style = {
    'color': 'black',
    'weight': 2,
    'fillOpacity': 0.7,
}

non_highlight_style = {
    'color': 'gray',
    'weight': 2,
    'fillOpacity': 0.3,
}

# Add GeoJson layer to outline neighborhood boundaries and display name and color based on normalized "Total Cameras" column
geojson_layer = folium.GeoJson(
    valid_df,
    name='Neighborhood Boundaries',
    style_function=lambda feature: {
        'fillColor': colormap(normalized_cameras.get(feature['properties']['Total Cameras'], 0.5)),  # Use a default color if neighborhood not found
        **non_highlight_style,  # Set initial style to non-highlight
    },
    highlight_function=lambda x: {'weight': 3, **highlight_style},  # Apply highlight style
    tooltip=folium.features.GeoJsonTooltip(fields=['Total Cameras'], aliases=['Total Cameras'], localize=True),
).add_to(m)

# Add neighborhood names as text on the map
for _, row in valid_df.iterrows():
    centroid = row.geometry.centroid
    if row.geometry.contains(centroid):
        folium.Marker(
            location=[centroid.y, centroid.x],
            icon=folium.DivIcon(html=f'<div style="font-weight: bold;">{row.name}</div>'),
            popup=None,
        ).add_to(geojson_layer)

# Display the map with neighborhood boundaries and markers using streamlit-folium
folium_static(m)
