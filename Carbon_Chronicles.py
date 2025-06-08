import config
from utils import *

st.title(APP_NAME)
st.header(CARBON_CHRONICLES_HEADER)

st.markdown(
    """
    CO₂ continues to be the most infamous greenhouse gas. This story highlights how different industries have contributed to its steady rise, with alarming trends in energy and transport.
    """
)

with st.sidebar:
    region_selection = st.multiselect('Region',continent,default=['Europe','Latin America and the Caribbean','Northern America'],placeholder=None)
    industry_selection = st.multiselect('Industry',industry,default=['Agriculture, Forestry and Fishing','Construction'],placeholder=None)

# Filter for CO₂, and sidebar selection
filtered_df = green_df[
    (green_df['Region'].isin(region_selection)) &
    (green_df['Gas Type']== 'Carbon dioxide') &
    (green_df['Industry'].isin(industry_selection))
]

st.header("CO₂ Emissions")
top_container = st.container()
middle_container = st.container()
bottom_container = st.container()
prompt_container = st.container()


with top_container:
    col1, col2 = st.columns(2)
    with col1:
    
    with col2:


with middle_container:
    col1, col2 = st.columns(2)
    with col1:
    
    with col2:

