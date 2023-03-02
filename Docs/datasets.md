## Datasets

### American Community Survey Data Profiles for 2021 at Block Group Level

- **Provider: [US Census Bureau | American Community Survey](https://www.census.gov/programs-surveys/acs/about.html)**
- **Filenames:**
  - `data/acs-variables.json` - subset of Data Profile variables used for this analysis and their description in a tabular format (should be compatible with [`pandas.read_json`](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html), for example)
  - `acs_dp_block_groups_BK.geojson` - the actual data for each census 
- **Description:** "Data Profiles have the most frequently requested social, economic, housing, and demographic data. Each of these four subject areas is a separate data profile. The Data Profiles summarize the data for a single geographic area, both numbers and percent, to cover the most basic data on all topics."
- **Links:**
  - [Data Profiles](https://www.census.gov/acs/www/data/data-tables-and-tools/data-profiles/)
  - [DP02 | Selected Social Characteristics](https://data.census.gov/table?tid=ACSDP5Y2021.DP02&g=0400000US36_0500000US36047) - Example table showing overall numbers for the social data profile variables for both New York State and Brooklyn (Kings County).
  - [DP03 | Selected Economic Characteristics](https://data.census.gov/table?tid=ACSDP5Y2021.DP03&g=0400000US36_0500000US36047) 
  - [DP04 | Selected Housing Characteristics](https://data.census.gov/table?tid=ACSDP5Y2021.DP04&g=0400000US36_0500000US36047)
  - [DP05 | ACS Demographic and Housing Estimates](https://data.census.gov/table?tid=ACSDP5Y2021.DP05&g=0400000US36_0500000US36047)
- **Documentation:** 
  - American Community Survey Information Guide - `docs/ACS_Information_Guide.pdf`
  - [Census definition of Block Group](https://www.census.gov/programs-surveys/geography/about/glossary.html#par_textimage_4)
  - [Definition of tidy data](https://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html). 
- **Format:** [GeoJSON](https://macwright.com/2015/03/23/geojson-second-bite.html)
- **Download method:**
  - The Clojure script defined in `notebooks/census_data_finder.clj` was used to identify and download the [machine-readable metadata](https://www.census.gov/data/developers/updates/new-discovery-tool.html) for the subset of Data Profile variables intended for use in the project. This metadata, output to `data/acs-variables.json`, includes the specific variable identifiers (e.g. `DP05_0024E` - population aged 65 and over). This was used as an input for the R script defined in `R/acs_summary_data.R`, which used that list of variable identifiers to query the Census API using the `tidycensus` package. More on the formatting and join below.

#### Note on data formatting for ACS data

The table views on the Census website are good for getting familiar with the hierarchical way the ACS data is organized. Because it comes pre-aggregated to a given geographic boundary, each variable of interest will have different "sub-variables" labelling each individual value. This means that in order to be well-organized, the data returned by `tidycensus` needs to be organized a little differently from other tabular data formats. The format of the output of `tidycensus` corresponds to the definition of "Tidy Data" as described by [Wickham [2014]](https://www.jstatsoft.org/article/view/v059i10):
> In tidy data:
> Every column is a variable.
> Every row is an observation.
> Every cell is a single value.

In this terminology, the ACS geojson dataset has two primary variable columns - "estimate", representing the count for the census, and "moe", representing the margin of error on that count (as the counts are inferred from a sample of surveys).  The rows, or observations, correspond to a count and margin of error for each combination of  Census field (e.g. `DP05_0024E` - population aged 65 and over) and block group (e.g. `GEOID 15000US360470730001` - Block Group 1, Census Tract 730, Kings County, New York).

If we tried to use a tabular format for the same information, with each row being a block group and each column being a different ACS variable and each cell representing a count, it would take two tables to represent both the counts and margins of error. The tidy format allows representation of all of the dimensions of interest in a single dataset. While the "estimate" and "moe" correspond to the observational information about the actual counts for each ACS variable, the dataset also retains labels  and other metadata from the `acs-variables.json` file to make working with this dataset easier. For example, the label for variable `DP05_0024E` is "Estimate!!SEX AND AGE!!Total population!!65 years and over". The components of the label separated by exclamation points make it easier to search and filter by the different categories and groupings of variables.

### MapPLUTO 

- **Provider: [NYC Department of City Planning](https://www.nyc.gov/site/planning/index.page)**
- **Filenames:**
  - `data/nyc_mappluto_22v3_shp`
  - `data/nyc_mappluto_22v3_fgdb`
- **Description:** "MapPLUTO merges PLUTO tax lot data with tax lot features from the Department of Finance's Digital Tax Map (DTM) and is available as shoreline clipped and water included. It contains extensive land use and geographic data at the tax lot level in ESRI shapefile and File Geodatabase formats."
- **Links:**
  - https://www.nyc.gov/site/planning/data-maps/open-data/dwn-pluto-mappluto.page
- **Documentation:** See `docs/MapPLUTO_metadata_22v3.pdf` for detailed information about this dataset.
- **Format:**
  - [Shapefile](https://desktop.arcgis.com/en/arcmap/10.3/manage-data/shapefiles/what-is-a-shapefile.htm)
  - [Geodatabase](https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/what-is-a-geodatabase-.htm)
- **Download method:** NYC DCP provides the data and metadata as static assets on their website, which were downloaded and extracted using the scripts specified in the `get_pluto_data` stage of the `dvc.yaml` pipeline.

### Cameras
There are two datasets of camera locations: one for a small sample of privately owned cameras, and another for a systmatic search of Google Street View for cameras operated by the NYPD.
#### NYPD Argus Cameras

- **Provider: [Amnesty International's Citizen Evidence Lab](https://citizenevidence.org/)**
- **Filenames** `data/amnesty_camera_counts_per_intersections.csv`
- **Description:** As part of efforts to ban the use of facial recognition technology by the NYPD, Amnesty International crowd-sourced a dataset of 15,000 camera locations to understand more about where the NYPD deploys its technology.
- **Links:**
  - [Interactive Map of Camera Locations](https://banthescan.amnesty.org/decode/)
  - [Project Overview on data collection methods](https://decoders.amnesty.org/projects/decode-surveillance)
  - [Initial Analysis of collected data](https://citizenevidence.org/2021/11/17/decode-surveillance-early-analysis/)
  - [GitHub repo with full datasets & R code for cleanup & analysis](https://github.com/amnesty-crisis-evidence-lab/decode-surveillance-nyc)
- **Documentation:** See `docs/DecodeSurveillanceNYCMethodology.pdf` for a detailed overview of the data collection and cleanup process.
- **Format:** [CSV](https://en.wikipedia.org/wiki/Comma-separated_values)
- **Download method:** Using the scripts specified in the `get_camera_data` stage of `dvc.yaml`, Amnesty's datasets were downloaded from GitHub, where they are hosted as static assets.

#### HikVision Camera Census

- **Provider: [Surveillance Technology Oversight Project](https://www.stopspying.org)**
- **Filename:** `data/NYC Surveillance Map Hikvision.kmz`
- **Description:** "In this first annual surveillance census, S.T.O.P. sought to map out all of the internet-enabled cameras operating in New York City. Even as many companies hide the location of their surveillance equipment, the Chinese-based firm Hikvision still allows their devices to be located... and the results are shocking. We identified 16,692 cameras in New Yorker City alone."
- **Links:**
  - [Project description](https://www.stopspying.org/2021-hikvision)
  - [Interactive Google map](https://www.google.com/maps/d/viewer?ll=40.706704542421086%2C-73.89314270000001&mid=12-p7Al4lR9Ltff85tN--7-y60pUNJnou&z=10)
- **Documentation:** See project description above for methodology.
- **Format:** [KML](https://developers.google.com/kml/documentation/kml_tut)
- **Download method:** The underlying [KML](https://en.wikipedia.org/wiki/Keyhole_Markup_Language) file with the camera locations was downloaded manually from the interactive Google map and added to this repo - no reliable automated method of fetching the KML data was identified.

