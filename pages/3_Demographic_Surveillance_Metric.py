import streamlit as st
import geopandas as gpd
import numpy as np
import folium
from folium.plugins import MiniMap
from streamlit_folium import folium_static
from branca.colormap import LinearColormap


st.set_page_config(layout="wide", page_title="Brooklyn Surveillance Metric (Racial & Ethnic Communities)")
st.title("Brooklyn Demographic Metric in an Interactive Visuals")
st.write((

    "Surveillance metrics for each major racial and ethnic group across all census tracts and neighborhood tabulation areas in Brooklyn."
)
)

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

    # Calculate the 10% quartiles of the "Black/Whit" column which is the avg value scaled for black vs whites
    quartiles = np.percentile(df["Black/Whit"].dropna(), [10, 20, 30, 40, 50, 60, 70, 80, 90])

    # Define the colors for the colormap
    colors = ['#FFFF00', '#FFEB00', '#FFD600', '#FFC200', '#FFAE00', '#FF9A00', '#FF8600', '#FF7200', '#FF5E00', '#FF4A00', '#FF3600', '#FF2200', '#FF0E00']

    # Create a linear colormap based on the colors and quartiles
    colormap = LinearColormap(colors, vmin=quartiles[0], vmax=quartiles[-1]).scale(quartiles[0], quartiles[-1])

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

    map_container, text_container = st.columns([5, 1])
    with map_container:
        folium_static(m, width=800, height=900)

    with text_container:
        st.write("If this metric is greater than 1.0, that means Black residents are surveilled at higher rates than White residents within the same neighborhood.")
        st.write("Based on the left map, Black vs. White surveillance rates at the Census Tract level, we see that Black residents are surveilled greater than White residents in more than 50% of the census tracts.")

    st.markdown(
        """
        <style>
        .layout-container {
            display: flex;
            flex-direction: row;
        }
        .map-container {
            flex: 1;
        }
        .text-container {
            width: 200px;
            font-size: 12px;
            background-color: rgba(255, 255, 255, 0.7);
            padding: 10px;
            border-radius: 5px;
            margin-left: 100px;
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

    # Calculate the 10% quartiles of the "Hispanic/W" column which is the avg value sclaed for Hispanic vs whites
    quartiles = np.percentile(df["Hispanic/W"].dropna(), [10, 20, 30, 40, 50, 60, 70, 80, 90])

    # Define the colors for the colormap
    colors = ['#FFFF00', '#FFEB00', '#FFD600', '#FFC200', '#FFAE00', '#FF9A00', '#FF8600', '#FF7200', '#FF5E00', '#FF4A00', '#FF3600', '#FF2200', '#FF0E00']

    # Create a linear colormap based on the colors and quartiles
    colormap = LinearColormap(colors, vmin=quartiles[0], vmax=quartiles[-1]).scale(quartiles[0], quartiles[-1])

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

    # Calculate the 10% quartiles of the "Black/Whit" column
    quartiles = np.percentile(df["Black/Whit"].dropna(), [10, 20, 30, 40, 50, 60, 70, 80, 90])

    # Define the gradient shades of red colors for the colormap
    colors = ['#FFFF00', '#FFEB00', '#FFD600', '#FFC200', '#FFAE00', '#FF9A00', '#FF8600', '#FF7200', '#FF5E00', '#FF4A00', '#FF3600', '#FF2200', '#FF0E00']


    # Create a linear colormap based on the colors and quartiles
    colormap = LinearColormap(colors, vmin=quartiles[0], vmax=quartiles[-1]).scale(quartiles[0], quartiles[-1])

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

    map_container, text_container = st.columns([5, 1])
    with map_container:
        folium_static(m, width=800, height=900)

    with text_container:
        st.write("The surveillance rates by race at the NTA level show lower racial disparities on average because we are randomly sampling points from our KDE output across a much larger geographical unit.")
        st.write("This also contributes to a larger margin of errors compared to surveillance rates by race sampled at the Census Tract level.")
    st.markdown(
        """
        <style>
        .layout-container {
            display: flex;
            flex-direction: row;
        }
        .map-container {
            flex: 1;
        }
        .text-container {
            width: 200px;
            font-size: 12px;
            background-color: rgba(255, 255, 255, 0.7);
            padding: 10px;
            border-radius: 5px;
            margin-left: 100px;
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

    # Define the colors for the colormap
    colors = ['#FFFF00', '#FFEB00', '#FFD600', '#FFC200', '#FFAE00', '#FF9A00', '#FF8600', '#FF7200', '#FF5E00', '#FF4A00', '#FF3600', '#FF2200', '#FF0E00']
    
    # Create a linear colormap based on the colors and quartiles
    colormap = LinearColormap(colors, vmin=quartiles[0], vmax=quartiles[-1]).scale(quartiles[0], quartiles[-1])

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

    