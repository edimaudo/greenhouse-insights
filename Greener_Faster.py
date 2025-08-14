from utils import *

st.title(APP_NAME)
st.header(GREENER_FASTER_HEADER)

st.markdown(
    """
    Some regions and industries are managing to lower their greenhouse gas emissions over time — but how do they compare to others? 
    This tracks relative emission reductions within industries and across regions, highlighting who is making the greatest progress (not just who pollutes the least).
    """
)

with st.sidebar:
    region_selection = st.multiselect('Region',continent,default=['Europe','Latin America and the Caribbean','Northern America'],placeholder=None)
    industry_selection = st.multiselect('Industry',industry,default=['Agriculture, Forestry and Fishing','Construction'],placeholder=None)

      # prompt = " You are a community safety advisor. Based on the following crime" + str(crime_output) + " that occurred in " + str(premises_options) + " at " + str(hour_options) + " hours in " + str(neighbourhood_options) + " a neigbhorhood in Toronto, Ontario, " + "generate 3 practical safety recommendations for local residents."
    