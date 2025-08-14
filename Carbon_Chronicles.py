from utils import *


st.title(APP_NAME)
st.header(CARBON_CHRONICLES_HEADER)

st.markdown(
    """
    CO₂ continues to be the most infamous greenhouse gas. This highlights how different industries have contributed to its steady rise, with alarming trends in transport.
    """
)

with st.sidebar:
    region_selection = st.multiselect('Region',continent,default=['Europe','Latin America and the Caribbean','Northern America'],placeholder=None)
    industry_selection = st.multiselect('Industry',industry,default=['Agriculture, Forestry and Fishing','Construction', 'Transportation and Storage'],placeholder=None)

filtered_df = green_df[
    (green_df['Region'].isin(region_selection)) &
    (green_df['Gas Type']== 'Carbon dioxide') &
    (green_df['Industry'].isin(industry_selection))
]

top_container = st.container()
middle_container = st.container()
bottom_container = st.container()
prompt_container = st.container()


with top_container:
    col1, col2 = st.columns(2)
    with col1:
        industry_by_year = filtered_df.groupby(['Year', 'Industry'])['Total'].sum().reset_index()
        if not industry_by_year.empty:
            fig_area_industry = px.area(
                industry_by_year,
                x='Year',
                y='Total',
                color='Industry',
                title='CO₂ Emissions by Industry',
                labels={'Total': 'CO₂ Emissions (metric tons)', 'Year': 'Year'}
            )
            st.plotly_chart(fig_area_industry, use_container_width=True)
        else:
            st.warning(NO_DATA_INFO)
    
    with col2:
        region_by_year = filtered_df.groupby(['Year', 'Region'])['Total'].sum().reset_index()
        if not region_by_year.empty:
            fig_area_region = px.area(
                region_by_year,
                x='Year',
                y='Total',
                color='Region',
                title='CO₂ Emissions by Region',
                labels={'Total': 'CO₂ Emissions (metric tons)', 'Year': 'Year'}
            )
            st.plotly_chart(fig_area_region, use_container_width=True)
        else:
            st.warning(NO_DATA_INFO)


with middle_container:
    latest_year = filtered_df['Year'].max()
    previous_year = latest_year - 1
    df_bubble = filtered_df[filtered_df['Year'].isin([previous_year, latest_year])]
    col1, col2 = st.columns(2)
    with col1:
        pivot_industry = df_bubble.pivot_table(index='Industry', columns='Year', values='Total', aggfunc='sum').dropna()
        if not pivot_industry.empty and len(pivot_industry.columns) == 2:
            pivot_industry['pct_change'] = (pivot_industry[latest_year] - pivot_industry[previous_year]) / pivot_industry[previous_year] * 100
            pivot_industry = pivot_industry.reset_index()

            fig_bubble_industry = px.scatter(
                pivot_industry, x='pct_change', y=latest_year, size=latest_year, color='Industry',
                hover_name='Industry', size_max=60, title=f'Industry Emissions vs. Rate of Increase ({previous_year}-{latest_year})',
                labels={'pct_change': 'Rate of Increase (%)', str(latest_year): f'CO₂ Emissions in {latest_year} (metric tons)'}
            )
            st.plotly_chart(fig_bubble_industry, use_container_width=True)
        else:
            st.warning(NO_DATA_INFO)        
    with col2:
        pivot_region = df_bubble.pivot_table(index='Region', columns='Year', values='Total', aggfunc='sum').dropna()
        if not pivot_region.empty and len(pivot_region.columns) == 2:
            pivot_region['pct_change'] = (pivot_region[latest_year] - pivot_region[previous_year]) / pivot_region[previous_year] * 100
            pivot_region = pivot_region.reset_index()

            fig_bubble_region = px.scatter(
                pivot_region, x='pct_change', y=latest_year, size=latest_year, color='Region',
                hover_name='Region', size_max=60, title=f'Region Emissions vs. Rate of Increase ({previous_year}-{latest_year})',
                labels={'pct_change': 'Rate of Increase (%)', str(latest_year): f'CO₂ Emissions in {latest_year} (metric tons)'}
            )
            st.plotly_chart(fig_bubble_region, use_container_width=True)
        else:
            st.warning(NO_DATA_INFO)  


with prompt_container:
    st.subheader("Policy Assistant")
    clicked = st.button("Generate Insights")
    if clicked:
        prompt = " You are an environmental expert focusing on climate change solutions, looking at these different regions " + str(region_selection)  + " and in these industries " + str(industry_selection)  + " . Generate 3 practical recommendations that climate leaders in these regions can take to reduce " + "Carbon dioxide" + " emissions "
    
        client = genai.Client() 
        response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=prompt
        )
    
        outcome_txt = st.text_area(label=" ",value=response.text,placeholder='', disabled=True, height='100px')
