import config
from utils import *

st.set_page_config(
    page_title=" 🔥 Carbon Chronicles",
    page_icon="🔥",
    layout="wide"
)

st.title(APP_NAME)
st.header(CARBON_CHRONICLES_HEADER)

st.markdown(
    """
    CO₂ continues to be the most infamous greenhouse gas. This story highlights how different industries have contributed to its steady rise, with alarming trends in energy and transport..
    """
)

with st.sidebar:
    region_selection = st.multiselect('Region',continent,default=None,placeholder=None)
    industry_selection = st.multiselect('Industry',industry,default=None,placeholder=None)