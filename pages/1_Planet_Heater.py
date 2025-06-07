import config
from utils import *



st.title(APP_NAME)
st.header(PLANET_HEATER_HEADER)

st.markdown(
    """
    As extreme weather intensifies, who contributes the most to the crisis? This story breaks down emissions across regions and industries to show where the heat is truly coming from.
    """
)

with st.sidebar:
    region_selection = st.multiselect('Region',continent,default=['Europe','Latin America and the Caribbean','Northern America'],placeholder=None)
    gas_type_selection = st.multiselect('Gas Type',gas_type,default=['Carbon dioxide','Nitrous oxide'],placeholder=None)
    industry_selection = st.multiselect('Industry',industry,default=['Agriculture, Forestry and Fishing','Construction'],placeholder=None)

top_container = st.container()
middle_container = st.container()
bottom_container = st.container()
prompt_container = st.container()

with top_container:
    st.subheader("Total GHG emissions")
    col1, col2 = st.columns(2)

with middle_container:
    st.subheader("Emissions by region and industry")
    col3, col4 = st.columns(2)

with bottom_container:
    st.subheader("Emissions Trend")
    col5, col6 = st.columns(2)
