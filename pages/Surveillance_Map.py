import streamlit as st
import geopandas as gpd
import pandas as pd
import numpy as np
import folium
from folium.plugins import MiniMap
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
from branca.colormap import linear

st.set_page_config(layout="wide", page_title="Brooklyn Surveillance Map")
st.title("Brooklyn Surveillance Metric and Total Cameras in an Interactive Map")

tab0,tab1,tab2 = st.tabs(["Blocks", "Tracts", "Neighborhoods"])

with tab0:
    st.subheader("")
    # Step 1: Load and preprocess the data
    @st.cache_data
    def load_data():
        filepath = "/Users/rahnumatarannum/bk_defenders_surveillance_capstone/Outputs/kde_final_output_0.shp"
        df = gpd.read_file(filepath)
        return df

    df = load_data()

    # Set the CRS for the GeoDataFrame
    gdf = df.set_crs(epsg=2263, inplace=False).to_crs(epsg=4326)

    # Calculate quartiles for the "avg_value_" column
    quartiles = np.percentile(gdf['avg_value_'], [25, 50, 75])

    # Create a linear colormap from yellow to red based on the "avg_value_" range
    colormap = linear.YlOrRd_09.scale(gdf['avg_value_'].min(), gdf['avg_value_'].max())

    # Create an interactive map centered around the data
    m = folium.Map(location=[gdf.centroid.y.mean(), gdf.centroid.x.mean()], zoom_start=12)

    # Add the GeoDataFrame to the map with colored boundaries based on "avg_value_"
    folium.GeoJson(
        gdf,
        name='Surveillance Metric',
        style_function=lambda feature: {
            'fillColor': colormap(feature['properties']['avg_value_']),
            'color': 'black',
            'weight': 2,
            'fillOpacity': 0.7
        },
        tooltip=folium.features.GeoJsonTooltip(
            fields=['avg_value_'],
            aliases=['Surveillance Metric:'],
            localize=True,
            labels=True,
            sticky=False,
            style="font-weight:bold"
        )
    ).add_to(m)

    # Create a layout with two columns: one for the map and one for the quartile values
    col1, col2 = st.columns([2, 1])

    # Display the map in the first column
    with col1:
        st.title("Census Blocks")
        folium_static(m)

    # Display quartile values in the second column
    with col2:
        st.title("Surveillance Metric Percentiles")
        st.markdown("25th Percentile: {:.2f}%".format(np.percentile(gdf['avg_value_'], 25)))
        st.markdown("50th Percentile: {:.2f}%".format(np.percentile(gdf['avg_value_'], 50)))
        st.markdown("75th Percentile: {:.2f}%".format(np.percentile(gdf['avg_value_'], 75)))



with tab1:
    # Step 1: Load and preprocess the data
    @st.cache_data
    def load_data():
        filepath = "/Users/rahnumatarannum/bk_defenders_surveillance_capstone/Outputs/kde_final_output_1.shp"
        df = gpd.read_file(filepath)
        return df

    df = load_data()

    # Set the CRS for the GeoDataFrame
    gdf = df.set_crs(epsg=2263, inplace=False).to_crs(epsg=4326)

    # Calculate quartiles for the "avg_value_" column
    quartiles = np.percentile(gdf['avg_value_'], [25, 50, 75])

    # Create a linear colormap from yellow to red based on the "avg_value_" range
    colormap = linear.YlOrRd_09.scale(gdf['avg_value_'].min(), gdf['avg_value_'].max())

    # Create an interactive map centered around the data
    m = folium.Map(location=[gdf.centroid.y.mean(), gdf.centroid.x.mean()], zoom_start=12)

    # Add the GeoDataFrame to the map with colored boundaries based on "avg_value_"
    folium.GeoJson(
        gdf,
        name='Surveillance Metric',
        style_function=lambda feature: {
            'fillColor': colormap(feature['properties']['avg_value_']),
            'color': 'black',
            'weight': 2,
            'fillOpacity': 0.7
        },
        tooltip=folium.features.GeoJsonTooltip(
            fields=['avg_value_'],
            aliases=['Surveillance Metric:'],
            localize=True,
            labels=True,
            sticky=False,
            style="font-weight:bold"
        )
    ).add_to(m)

    # Create a layout with two columns: one for the map and one for the quartile values
    col1, col2 = st.columns([2, 1])

    # Display the map in the first column
    with col1:
        st.title("Census Tracts")
        folium_static(m)

    # Display quartile values in the second column
    with col2:
        st.title("Surveillance Metric Percentiles")
        st.markdown("25th Percentile: {:.2f}%".format(np.percentile(gdf['avg_value_'], 25)))
        st.markdown("50th Percentile: {:.2f}%".format(np.percentile(gdf['avg_value_'], 50)))
        st.markdown("75th Percentile: {:.2f}%".format(np.percentile(gdf['avg_value_'], 75)))


with tab2:


    # Step 1: Load and preprocess the data
    @st.cache_data
    def load_data():
        filepath = "/Users/rahnumatarannum/bk_defenders_surveillance_capstone/Data/nta_surv_metric_TEST_FOR_NUMA/nta_surv_metric_TEST_FOR_NUMA.shp"
        df = gpd.read_file(filepath)
        return df

    df = load_data()

    # Step 2: Load the surveillance metric data
    metric_filepath = "/Users/rahnumatarannum/bk_defenders_surveillance_capstone/Outputs/kde_final_output_2.shp"
    metric_df = gpd.read_file(metric_filepath)

    # Merge the df and metric_df on 'ntaname' column
    merged_df = df.merge(metric_df[['ntaname', 'avg_value_']], on='ntaname', how='left')

    # Create a linear colormap from yellow to red based on the "avg_value_" range
    colormap = linear.YlOrRd_09.scale(merged_df['avg_value_'].min(), merged_df['avg_value_'].max())

    # Create an interactive map centered around the data
    m = folium.Map(location=[merged_df.centroid.y.mean(), merged_df.centroid.x.mean()], zoom_start=12)

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
            'fillColor': 'gray' if feature['properties']['avg_value_'] < -2.0 else colormap(feature['properties']['avg_value_']),
            **non_highlight_style
        },
        highlight_function=lambda x: {'weight': 3, **highlight_style},
        tooltip=folium.features.GeoJsonTooltip(fields=['ntaname', 'avg_value_'], aliases=['Neighborhood', 'Surveillance Metric'], localize=True)
    ).add_to(m)

    # Add the legend to the right side of the map
    colormap.caption = 'Surveillance Metric'
    m.add_child(colormap)
    m.get_root().html.add_child(folium.Element('<div style="position: fixed; top: 10px; right: 10px; z-index:9999; font-size: 12px; background-color: rgba(255, 255, 255, 0.7); padding: 10px; border-radius: 5px;">' + colormap.caption + '</div>'))

    # Create a layout with two columns: one for the map and one for the quartile values
    col1, col2 = st.columns([2, 1])

    # Display the map in the first column
    with col1:
        st.title("Neighborhood Basis Surveillance Load")
        folium_static(m)

    # Display quartile values in the second column
    with col2:
        st.title("Surveillance Metric Percentiles")
        st.markdown("25th Percentile: {:.2f}".format(np.percentile(merged_df['avg_value_'], 25)))
        st.markdown("50th Percentile: {:.2f}".format(np.percentile(merged_df['avg_value_'], 50)))
        st.markdown("75th Percentile: {:.2f}".format(np.percentile(merged_df['avg_value_'], 75)))
