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
prompt_container = st.container()

with st.sidebar:
    region_selection = st.multiselect('Region',continent,default=['Europe','Latin America and the Caribbean','Northern America'],placeholder=None)
    industry_selection = st.multiselect('Industry',industry,default=['Agriculture, Forestry and Fishing','Construction'],placeholder=None)
    gas_type_selection = st.selectbox('Gas Type',gas_type,placeholder="Carbon dioxide")

# Filter data based on selections
filtered_df = green_df[
    (green_df['Region'].isin(region_selection)) &
    (green_df['Gas Type'] == gas_type_selection) &
    (green_df['Industry'].isin(industry_selection))
]

latest_year = filtered_df['Year'].max()
earliest_year = filtered_df['Year'].min()
df = filtered_df[filtered_df['Year'].isin([earliest_year, latest_year])]

with top_container:
    col1, col2 = st.columns(2)
    with col1:
        pivot_df = df.pivot_table(index='Region', columns='Year', values='Total', aggfunc='sum').dropna()
        if not pivot_df.empty and len(pivot_df.columns) == 2:
            pivot_df['% change'] = (pivot_df[latest_year] - pivot_df[earliest_year]) / pivot_df[earliest_year] * 100
            pivot_df = pivot_df.reset_index()
            fig = px.bar(pivot_df,x='% change', y='Region', color='% change',hover_name='Region',
                         title = f'Region Emissions vs. Rate of Increase ({earliest_year}-{latest_year})')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning(NO_DATA_INFO) 

    with col2:
        pivot_df = df.pivot_table(index='Industry', columns='Year', values='Total', aggfunc='sum').dropna()
        if not pivot_df.empty and len(pivot_df.columns) == 2:
            pivot_df['% change'] = (pivot_df[latest_year] - pivot_df[earliest_year]) / pivot_df[earliest_year] * 100
            pivot_df = pivot_df.reset_index()
            fig = px.bar(pivot_df,x='% change', y='Industry', color='% change',hover_name='Industry',
                         title = f'Industry Emissions vs. Rate of Increase ({earliest_year}-{latest_year})')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning(NO_DATA_INFO)

with middle_container:
    agg = (
    df
    .groupby(['Industry', 'Region', 'Year'], as_index=False)['Total']
    .sum()
    )
    
    pivot_df = agg.pivot(index=['Industry', 'Region'], columns='Year', values='Total')
    if not pivot_df.empty:
        pivot_df['% change'] = ((pivot_df[latest_year] - pivot_df[earliest_year]) /pivot_df[earliest_year] * 100)
        heatmap_data = pivot_df['% change'].unstack('Region')
        fig = px.imshow(
            heatmap_data,
            x=heatmap_data.columns,   # Regions
            y=heatmap_data.index,     # Industries
            color_continuous_scale='Viridis',
            labels=dict(x="Region", y="Industry", color="% Change")
        )
        fig.update_layout(width=700, height=700)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning(NO_DATA_INFO)


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
    
        outcome_txt = st.text_area(label=" ",value=response.text,placeholder='', disabled=True)