from utils import *

st.title(APP_NAME)
st.header(GREENER_FASTER_HEADER)

st.markdown(
    """
    Some regions and industries are managing to lower their greenhouse gas emissions over time — but how do they compare to others? 
    This tracks relative emission reductions within industries and across regions, highlighting who is making the greatest progress 
    (not just who pollutes the least).
    """
)
top_container = st.container()
middle_container = st.container()
bottom_container = st.container()
prompt_container = st.container()

with st.sidebar:
    region_selection = st.multiselect('Region',continent,default=['Europe','Latin America and the Caribbean','Northern America'],placeholder=None)
    industry_selection = st.multiselect('Industry',industry,default=['Agriculture, Forestry and Fishing','Construction'],placeholder=None)
    gas_type_selection = st.selectbox('Gas Type',gas_type,default="Carbon dioxide")

# Filter data based on selections
filtered_df = green_df[
    (green_df['Region'].isin(region_selection)) &
    (green_df['Gas Type'] == gas_type_selection) &
    (green_df['Industry'].isin(industry_selection))
]


with top_container:
    col1, col2 = st.columns(2)

with prompt_container:
    st.subheader("Policy Assistant")
    clicked = st.button("Generate Insights")
    if clicked:
        prompt = " You are an environmental expert focusing on reducing greenhouse gases quickly using technology and environmentally-friendly solutions, " \
        "looking at these different regions " + str(region_selection)  + " and in these industries " + str(industry_selection)  + " . Generate 3 practical recommendations that " \
        "climate leaders in these regions can take to reduce " + str(gas_type_selection) + " emissions "
    
        client = genai.Client() 
        response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=prompt
        )
    
        outcome_txt = st.text_area(label=" ",value=response.text,placeholder='', disabled=True, height='500px')