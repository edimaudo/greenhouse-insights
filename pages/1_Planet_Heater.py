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
    gas_type_selection = st.selectbox('Gas Type',gas_type,default=['Carbon dioxide'],placeholder=None)
    industry_selection = st.multiselect('Industry',industry,default=['Agriculture, Forestry and Fishing','Construction'],placeholder=None)

top_container = st.container()
middle_container = st.container()
bottom_container = st.container()
prompt_container = st.container()

st.subheader("Total GHG Emissions")
with top_container:
    col1, col2 = st.columns(2)
    with col1:
        # emissions by region
        st.write("")
    
    with col2:
        # emissions by industry
        st.write("")


with middle_container:
    st.write("")
    # sankey chart

with bottom_container:
    col1, col2 = st.columns(2)
    with col1:
        #emissions by region
        st.write("")

    with col2:
        #emissions by industry
        st.write("")
        
with prompt_container:
    st.write("")