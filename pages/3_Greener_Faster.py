import config
from utils import *

st.set_page_config(
    page_title=" 🔍 Greener Faster",
    page_icon="🔍",
    layout="wide"
)

st.title(APP_NAME)
st.header(GREENER_FASTER_HEADER)

st.markdown(
    """
    CSome regions and industries are managing to lower their greenhouse gas emissions over time — but how do they compare to others? This story tracks relative emission reductions within industries and across regions, highlighting who is making the greatest progress (not just who pollutes the least).
    """
)

with st.sidebar:
    region_selection = st.multiselect('Region',continent,default=None,placeholder=None)
    industry_selection = st.multiselect('Industry',industry,default=None,placeholder=None)