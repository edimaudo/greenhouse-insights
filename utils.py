"""
Libraries
"""
import streamlit as st
import pandas as pd
import datetime
import os, os.path
import warnings
import random
import plotly.express as px
import plotly.graph_objects as go

"""
Dashboard Information
"""
APP_NAME = 'Greenhouse Insights'
ABOUT_HEADER = 'About'
PLANET_HEATER_HEADER = "Who's Heating the Planet?"
CARBON_CHRONICLES_HEADER = 'Carbon Chronicles: Rise of CO₂'
GREENER_FASTER_HEADER = 'Greener, Faster: Who’s Leading the Emission Efficiency Race?'
APP_FILTERS = 'Filters'
NO_DATA_INFO = 'No data available to display based on the filters'

warnings.simplefilter(action='ignore', category=FutureWarning)
st.set_page_config(
    page_title=APP_NAME,
    layout="wide"
)

"""
Load data
"""
@st.cache_data
def load_data(data_file):
    data = pd.read_excel(data_file)
    data['Year'] = pd.to_numeric(data['Year'])
    return data

green_df = load_data("greenhouse.xlsx")

"""
Filters
"""
gas_type = ['Carbon dioxide',
'Fluorinated gases',
'Greenhouse gas',
'Methane',
'Nitrous oxide']

continent = ['Africa',
'Asia',
'Europe',
'Latin America and the Caribbean',
'Northern America',
'Oceania']

industry = ['Agriculture, Forestry and Fishing',
'Construction',
'Electricity, Gas, Steam and Air Conditioning Supply',
'Manufacturing',
'Mining',
'Other Services Industries',
'Transportation and Storage',
'Water supply; sewerage, waste management and remediation activities']

industry_other = ['Agriculture, Forestry and Fishing',
'Construction',
'Electricity, Gas, Steam and Air Conditioning Supply',
'Manufacturing',
'Mining',
'Other Services Industries',
'Total Households',
'Total Industry and Households',
'Transportation and Storage',
'Water supply; sewerage, waste management and remediation activities']

geographical_area = ['Advanced Economies',
'Africa',
'Americas',
'Asia',
'Australia and New Zealand',
'Central Asia',
'Eastern Asia',
'Eastern Europe',
'Emerging and Developing Economies',
'Europe',
'G20',
'G7',
'Latin America and the Caribbean',
'Northern Africa',
'Northern America',
'Northern Europe',
'Oceania',
'Other Oceania sub-regions',
'South-eastern Asia',
'Southern Asia',
'Southern Europe',
'Sub-Saharan Africa',
'Western Asia',
'Western Europe',
'World']