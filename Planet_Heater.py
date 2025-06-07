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
    industry_selection = st.multiselect('Industry',industry,default=['Agriculture, Forestry and Fishing','Construction'],placeholder=None)
    gas_type_selection = st.selectbox('Gas Type',gas_type,placeholder='Carbon dioxide')

# Filter data based on selections
filtered_df = green_df[
    (green_df['Region'].isin(region_selection)) &
    (green_df['Gas Type']==(gas_type_selection)) &
    (green_df['Industry'].isin(industry_selection))
]

st.subheader("Total GHG Emissions")
top_container = st.container()
middle_container = st.container()
bottom_container = st.container()
prompt_container = st.container()


with top_container:
    col1, col2 = st.columns(2)
    with col1:
        emissions_by_region = filtered_df.groupby('Region')['Total'].sum().sort_values(ascending=True).reset_index()
        fig_region = px.bar(
            emissions_by_region,
            x='Total',
            y='Region',
            orientation='h',
            title='Emissions by Region (metric tons)'
        )
        st.plotly_chart(fig_region, use_container_width=True)
    
    with col2:
        emissions_by_industry = filtered_df.groupby('Industry')['Total'].sum().sort_values(ascending=True).reset_index()
        fig_industry = px.bar(
            emissions_by_industry,
            x='Total',
            y='Industry',
            orientation='h',
            title='Emissions by Industry (metric tons)'
        )
        st.plotly_chart(fig_industry, use_container_width=True)


with middle_container:
    sankey_data = filtered_df.groupby(['Region', 'Industry'])['Total'].sum().reset_index()
    all_nodes = list(pd.concat([sankey_data['Region'], sankey_data['Industry']]).unique())
    sankey_data['source'] = sankey_data['Region'].apply(lambda x: all_nodes.index(x))
    sankey_data['target'] = sankey_data['Industry'].apply(lambda x: all_nodes.index(x))

    fig_sankey = go.Figure(data=[go.Sankey(
        node=dict(
          pad=15,
          thickness=20,
          line=dict(color="black", width=0.5),
          label=all_nodes,
        ),
        link=dict(
          source=sankey_data['source'],
          target=sankey_data['target'],
          value=sankey_data['Total']
      ))])

    fig_sankey.update_layout(title_text="GHG Emissions: Region to Industry Flow (metric tons)", font_size=10)
    st.plotly_chart(fig_sankey, use_container_width=True)

with bottom_container:
    col1, col2 = st.columns(2)
    with col1:
        region_by_year = filtered_df.groupby(['Year', 'Region'])['Total'].sum().reset_index()
        fig_region_line = px.line(
            region_by_year,
            x='Year',
            y='Total',
            color='Region',
            title='Emissions by Region Trend (metric tons)'
        )
        st.plotly_chart(fig_region_line, use_container_width=True)

    with col2:
        # Emissions by Industry over Time (Line Chart)
        industry_by_year = filtered_df.groupby(['Year', 'Industry'])['Total'].sum().reset_index()
        fig_industry_line = px.line(
            industry_by_year,
            x='Year',
            y='Total',
            color='Industry',
            title='Emissions by Industry Trend (metric tons)'
        )
        st.plotly_chart(fig_industry_line, use_container_width=True)
        
with prompt_container:
    st.write("")