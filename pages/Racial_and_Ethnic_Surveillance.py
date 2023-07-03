import streamlit as st
import geopandas as gpd
import folium
from folium.plugins import MiniMap
from streamlit_folium import folium_static
from branca.colormap import LinearColormap


st.set_page_config(layout="wide", page_title="Brooklyn Surveillance Metric (Racial & Ethnic Communities)")
st.title("Brooklyn Racial and Ethnic Surveillance Metric in an Interactive Map")

tab0, tab1 = st.tabs(["Tracts", "Neighborhoods"])

with tab0:
    st.subheader("Black Vs. White Communities")
    # Step 1: Load and preprocess the data
    @st.cache_data
    def load_data():
        filepath = "/Users/rahnumatarannum/bk_defenders_surveillance_capstone/Outputs/tract_racial_ethnic_surveillance.shp"
        df = gpd.read_file(filepath)
        return df

    df = load_data()

    # Set the CRS for the GeoDataFrame
    gdf = df.to_crs(epsg=4326)

    # Define the colors and thresholds for the colormap
    colors = ['#ffffcc', '#ffeda0', '#fed976', '#feb24c', '#fd8d3c', '#fc4e2a', '#e31a1c', '#bd0026', '#800026']
    thresholds = list(range(0, 101, 10))

    # Create a linear colormap based on the colors and thresholds
    colormap = LinearColormap(colors, vmin=0, vmax=100).scale(min(thresholds), max(thresholds))

    # Create an interactive map centered around the data
    m = folium.Map(location=[gdf.centroid.y.mean(), gdf.centroid.x.mean()], zoom_start=12)

    folium.GeoJson(
    gdf,
    name='Surveillance Metric',
    style_function=lambda feature: {
        'fillColor': colormap(feature['properties']['Black/Whit']) if feature['properties']['Black/Whit'] is not None else 'gray',
        'color': 'black',
        'weight': 2,
        'fillOpacity': 0.7
    },
    tooltip=folium.features.GeoJsonTooltip(
        fields=['Black/Whit'],
        aliases=['Surveillance Metric:'],
        localize=True,
        labels=True,
        sticky=False,
        style="font-weight:bold"
    )
).add_to(m)

    # Add the colormap to the map legend
    colormap.add_to(m)

    map_container = st.container()
    with map_container:
        folium_static(m, width=800, height=900)

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

    st.subheader("Hispanic Vs. White Communities")
    # Step 1: Load and preprocess the data
    @st.cache_data
    def load_data():
        filepath = "/Users/rahnumatarannum/bk_defenders_surveillance_capstone/Outputs/tract_racial_ethnic_surveillance.shp"
        df = gpd.read_file(filepath)
        return df

    df = load_data()

    # Set the CRS for the GeoDataFrame
    gdf = df.to_crs(epsg=4326)

    # Define the colors and thresholds for the colormap
    colors = ['#0000FF', '#0055FF', '#00AAFF', '#00FFFF', '#55FFAA', '#AAFF55', '#FFFF00', '#FFAA00', '#FF5500']
    thresholds = list(range(0, 101, 10))

    # Create a linear colormap based on the colors and thresholds
    colormap = LinearColormap(colors, vmin=0, vmax=100).scale(min(thresholds), max(thresholds))

    # Create an interactive map centered around the data
    m = folium.Map(location=[gdf.centroid.y.mean(), gdf.centroid.x.mean()], zoom_start=12)

    folium.GeoJson(
    gdf,
    name='Surveillance Metric',
    style_function=lambda feature: {
        'fillColor': colormap(feature['properties']['Hispanic/W']) if feature['properties']['Hispanic/W'] is not None else 'gray',
        'color': 'black',
        'weight': 2,
        'fillOpacity': 0.7
    },
    tooltip=folium.features.GeoJsonTooltip(
        fields=['Hispanic/W'],
        aliases=['Surveillance Metric:'],
        localize=True,
        labels=True,
        sticky=False,
        style="font-weight:bold"
    )
).add_to(m)

    # Add the colormap to the map legend
    colormap.add_to(m)

    map_container = st.container()
    with map_container:
        folium_static(m, width=800, height=900)

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


with tab1:
    st.subheader("Black Vs. White Communities")
    # Step 1: Load and preprocess the data
    @st.cache_data
    def load_data():
        filepath = "/Users/rahnumatarannum/bk_defenders_surveillance_capstone/Outputs/nta_racial_ethnic_surveillance.shp"
        df = gpd.read_file(filepath)
        return df

    df = load_data()

    # Set the CRS for the GeoDataFrame
    gdf = df.to_crs(epsg=4326)

    # Define the colors and thresholds for the colormap
    colors = ['#ffffcc', '#ffeda0', '#fed976', '#feb24c', '#fd8d3c', '#fc4e2a', '#e31a1c', '#bd0026', '#800026']
    thresholds = list(range(0, 101, 10))

    # Create a linear colormap based on the colors and thresholds
    colormap = LinearColormap(colors, vmin=0, vmax=100).scale(min(thresholds), max(thresholds))

    # Create an interactive map centered around the data
    m = folium.Map(location=[gdf.centroid.y.mean(), gdf.centroid.x.mean()], zoom_start=12)

    folium.GeoJson(
    gdf,
    name='Surveillance Metric',
    style_function=lambda feature: {
        'fillColor': colormap(feature['properties']['Black/Whit']) if feature['properties']['Black/Whit'] is not None else 'gray',
        'color': 'black',
        'weight': 2,
        'fillOpacity': 0.7
    },
    tooltip=folium.features.GeoJsonTooltip(
        fields=['Black/Whit'],
        aliases=['Surveillance Metric:'],
        localize=True,
        labels=True,
        sticky=False,
        style="font-weight:bold"
    )
).add_to(m)

    # Add the colormap to the map legend
    colormap.add_to(m)

    map_container = st.container()
    with map_container:
        folium_static(m, width=800, height=900)

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

    st.subheader("Hispanic Vs. White Communities")
    # Step 1: Load and preprocess the data
    @st.cache_data
    def load_data():
        filepath = "/Users/rahnumatarannum/bk_defenders_surveillance_capstone/Outputs/nta_racial_ethnic_surveillance.shp"
        df = gpd.read_file(filepath)
        return df

    df = load_data()

    # Set the CRS for the GeoDataFrame
    gdf = df.to_crs(epsg=4326)

    # Define the colors and thresholds for the colormap
    colors = ['#0000FF', '#0055FF', '#00AAFF', '#00FFFF', '#55FFAA', '#AAFF55', '#FFFF00', '#FFAA00', '#FF5500']
    thresholds = list(range(0, 101, 10))

    # Create a linear colormap based on the colors and thresholds
    colormap = LinearColormap(colors, vmin=0, vmax=100).scale(min(thresholds), max(thresholds))

    # Create an interactive map centered around the data
    m = folium.Map(location=[gdf.centroid.y.mean(), gdf.centroid.x.mean()], zoom_start=12)

    folium.GeoJson(
    gdf,
    name='Surveillance Metric',
    style_function=lambda feature: {
        'fillColor': colormap(feature['properties']['Hispanic/W']) if feature['properties']['Hispanic/W'] is not None else 'gray',
        'color': 'black',
        'weight': 2,
        'fillOpacity': 0.7
    },
    tooltip=folium.features.GeoJsonTooltip(
        fields=['Hispanic/W'],
        aliases=['Surveillance Metric:'],
        localize=True,
        labels=True,
        sticky=False,
        style="font-weight:bold"
    )
).add_to(m)

    # Add the colormap to the map legend
    colormap.add_to(m)

    map_container = st.container()
    with map_container:
        folium_static(m, width=800, height=900)

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