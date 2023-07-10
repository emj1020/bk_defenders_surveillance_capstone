import streamlit as st
import geopandas as gpd
import pandas as pd
import numpy as np
import folium
from folium.plugins import Fullscreen
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
from branca.colormap import linear


st.set_page_config(layout="wide", page_title="Brooklyn Surveillance Map")
st.title("Brooklyn Surveillance Metric in an Interactive Map")
st.write((
            "Using KDE output within the bounds of geographic units defined by various geospatial datasets like census blocks, tracts, and " 
            "neighborhood tabulation areas to see which certain neighborhoods are subjected to higher rates of surveillance compared to others."
            " Our final surveillance metric is the average density within each neighborhood boundary and is then scaled to be between 0 and 1."
)
)

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

    # Rename the "avg_value_" column to "avg_value_scaled"
    gdf.rename(columns={'avg_value_': 'avg_value_scaled'}, inplace=True)

    # Create a linear colormap from yellow to red based on the "avg_value_scaled" range
    colormap = linear.YlOrRd_09.scale(gdf['avg_value_scaled'].min(), gdf['avg_value_scaled'].max())

    # Create an interactive map centered around the data
    m = folium.Map(location=[gdf.centroid.y.mean(), gdf.centroid.x.mean()], zoom_start=14)

    # Add the GeoDataFrame to the map with colored boundaries based on "avg_value_scaled"
    folium.GeoJson(
        gdf,
        name='Surveillance Metric',
        style_function=lambda feature: {
            'fillColor': colormap(feature['properties']['avg_value_scaled']),
            'color': 'black',
            'weight': 2,
            'fillOpacity': 0.7
        },
        tooltip=folium.features.GeoJsonTooltip(
            fields=['avg_value_scaled', 'quartile_b', 'quartile_l'],
            aliases=['Surveillance Metric:', 'Quartile Label:', 'Percentile:'],
            localize=True,
            labels=True,
            sticky=False,
            style="font-weight:bold"
        )
    ).add_to(m)

    # Add the legend to the right side of the map
    colormap.caption = 'Surveillance Metric'
    m.add_child(colormap)

    # Create the legend HTML with the updated CSS class
    legend_html = '''
    <div class="legend-container">
        <p><strong>Legend:</strong></p>
        <p><strong>Quartile Buckets & Labels:</strong></p>
        <p>Q1: Bottom 25%</p>
        <p>Q2: Second Quartile</p>
        <p>Q3: Third Quartile</p>
        <p>Q4: Top 25%</p>
    </div>
    '''

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
        .legend-container {
            width: 200px;
            font-size: 12px;
            background-color: rgba(255, 255, 255, 0.7);
            padding: 10px;
            border-radius: 5px;
            margin-left: 50px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    layout_container = st.container()
    with layout_container:
        col1, col2 = st.columns([3, 1])
        with col1:
            map_container = st.container()
            with map_container:
                folium_static(m, width=800, height=900)

        with col2:
            legend_container = st.container()
            with legend_container:
                st.markdown(legend_html, unsafe_allow_html=True)


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

    # Rename the "avg_value_" column to "avg_value_scaled"
    gdf.rename(columns={'avg_value_': 'avg_value_scaled'}, inplace=True)

    # Calculate quartiles for the "avg_value_scaled" column
    quartiles = np.percentile(gdf['avg_value_scaled'], [25, 50, 75])

    # Create a linear colormap from yellow to red based on the "avg_value_scaled" range
    colormap = linear.YlOrRd_09.scale(gdf['avg_value_scaled'].min(), gdf['avg_value_scaled'].max())

    # Create an interactive map centered around the data
    m = folium.Map(location=[gdf.centroid.y.mean(), gdf.centroid.x.mean()], zoom_start=14)

    folium.GeoJson(
        gdf,
        name='Surveillance Metric',
        style_function=lambda feature: {
            'fillColor': colormap(feature['properties']['avg_value_scaled']),
            'color': 'black',
            'weight': 2,
            'fillOpacity': 0.7
        },
        tooltip=folium.features.GeoJsonTooltip(
            fields=['avg_value_scaled', 'quartile_b', 'quartile_l'],
            aliases=['Surveillance Metric:', 'Quartile Label:', 'Percentile:'],
            localize=True,
            labels=True,
            sticky=False,
            style="font-weight:bold"
        )
    ).add_to(m)

    # Add the legend to the right side of the map
    colormap.caption = 'Surveillance Metric'
    m.add_child(colormap)

    # Create the legend HTML with the updated CSS class
    legend_html = '''
    <div class="legend-container">
        <p><strong>Legend:</strong></p>
        <p><strong>Quartile Buckets & Labels:</strong></p>
        <p>Q1: Bottom 25%</p>
        <p>Q2: Second Quartile</p>
        <p>Q3: Third Quartile</p>
        <p>Q4: Top 25%</p>
    </div>
    '''

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
        .legend-container {
            width: 200px;
            font-size: 12px;
            background-color: rgba(255, 255, 255, 0.7);
            padding: 10px;
            border-radius: 5px;
            margin-left: 50px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    layout_container = st.container()
    with layout_container:
        col1, col2 = st.columns([3, 1])
        with col1:
            map_container = st.container()
            with map_container:
                folium_static(m, width=800, height=900)

        with col2:
            legend_container = st.container()
            with legend_container:
                st.markdown(legend_html, unsafe_allow_html=True)



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
    merged_df = df.merge(metric_df[['ntaname', 'avg_value_','quartile_b', 'quartile_l' ]], on='ntaname', how='left')

    # Rename the "avg_value_" column to "avg_value_scaled"
    merged_df.rename(columns={'avg_value_': 'avg_value_scaled'}, inplace=True)

    # Create a linear colormap from yellow to red based on the "avg_value_scaled" range
    colormap = linear.YlOrRd_09.scale(merged_df['avg_value_scaled'].min(), merged_df['avg_value_scaled'].max())

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
            'fillColor': 'gray' if feature['properties']['avg_value_scaled'] <= 0 else colormap(feature['properties']['avg_value_scaled']),
            **non_highlight_style
        },
        highlight_function=lambda x: {'weight': 3, **highlight_style},
        tooltip=folium.features.GeoJsonTooltip(
            fields=['ntaname', 'avg_value_scaled', 'quartile_b', 'quartile_l'],
            aliases=['Neighborhood:', 'Surveillance Metric:', 'Quartile Label:', 'Percentile:'],
            localize=True
        )
    ).add_to(m)

    # Add the legend to the right side of the map
    colormap.caption = 'Surveillance Metric'
    m.add_child(colormap)

    # Create the legend HTML with the updated CSS class
    legend_html = '''
    <div class="legend-container">
        <p><strong>Legend:</strong></p>
        <p><strong>Quartile Buckets & Labels:</strong></p>
        <p>Q1: Bottom 25%</p>
        <p>Q2: Second Quartile</p>
        <p>Q3: Third Quartile</p>
        <p>Q4: Top 25%</p>
    </div>
    '''

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
        .legend-container {
            width: 200px;
            font-size: 12px;
            background-color: rgba(255, 255, 255, 0.7);
            padding: 10px;
            border-radius: 5px;
            margin-left: 50px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    layout_container = st.container()
    with layout_container:
        col1, col2 = st.columns([3, 1])
        with col1:
            map_container = st.container()
            with map_container:
                folium_static(m, width=800, height=700)

        with col2:
            legend_container = st.container()
            with legend_container:
                st.markdown(legend_html, unsafe_allow_html=True)