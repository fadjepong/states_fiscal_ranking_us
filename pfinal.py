import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import plotly.express as px



st.title('States Fiscal Ranking')
st.markdown('The Data is from 2006 to 2016 and explores three areas: '
'1. The Population of US by States, '
'2. The Per-capita income of the working population by States, and '
'3. Overall Ranking of the Fiscal Performance of Each State with number 1 being best performing and number 50 being least performing.')






DATE_COLUMN = 'year'


st.sidebar.header("Filteration Options")
year_to_filter = st.sidebar.slider('year', 2006, 2016, 2006)

@st.cache(allow_output_mutation=True)
def load_data(year_to_filter):
   df = pd.read_csv('statesranking.csv')
   df =df[df[DATE_COLUMN] == year_to_filter].reset_index(drop=True)
   lowercase = lambda x: str(x).lower()
   df.rename(lowercase, axis='columns', inplace=True)
   return df

df_filtered= load_data(year_to_filter)
df_filtered=pd.DataFrame(df_filtered)
selection_list =pd.array(data=['population','overallrank','person_income_per_capita'])

name_of_selectbox = st.sidebar.selectbox('Select Value for map', selection_list)
tab1, tab2, tab3 = st.tabs(['Data Overview','Bar Chart','Map visualizatoin'])
with tab1:
    if st.checkbox('Show raw data'):
       
        st.subheader('Raw data')
        st.dataframe(df_filtered, use_container_width=True)
       

with tab2:
    if name_of_selectbox == 'population':
        st.subheader(f'Chart of {name_of_selectbox} in year {year_to_filter}')
        c1=alt.Chart(df_filtered).mark_bar().encode(
            x=alt.X('state',sort='-y'),
            y=alt.Y('population'),
            tooltip=['population', 'state'])
        st.altair_chart(c1, use_container_width=True)
    elif name_of_selectbox == 'overallrank':
        st.subheader(f'Chart of {name_of_selectbox} in year {year_to_filter}')
        c1=alt.Chart(df_filtered).mark_bar().encode(
            x=alt.X('state',sort='-y'),
            y=alt.Y('overallrank'),
            tooltip=['overallrank', 'state'])
        
        st.altair_chart(c1, use_container_width=True)
        
    elif name_of_selectbox == 'person_income_per_capita':
        st.subheader(f'Chart of {name_of_selectbox} in year {year_to_filter}')
        c1=alt.Chart(df_filtered).mark_bar().encode(
            x=alt.X('state',sort='-y'),
            y=alt.Y('person_income_per_capita'),
            tooltip=['person_income_per_capita', 'state'])

        st.altair_chart(c1, use_container_width=True)
    

with tab3:
    
    st.subheader(f'Map of {name_of_selectbox} in year {year_to_filter}')
    df_filtered['state'] = df_filtered['state'].str.strip()
    
    state_codes = {
    'District of Columbia' : 'dc','Mississippi': 'MS', 'Oklahoma': 'OK', 
    'Delaware': 'DE', 'Minnesota': 'MN', 'Illinois': 'IL', 'Arkansas': 'AR', 
    'New Mexico': 'NM', 'Indiana': 'IN', 'Maryland': 'MD', 'Louisiana': 'LA', 
    'Idaho': 'ID', 'Wyoming': 'WY', 'Tennessee': 'TN', 'Arizona': 'AZ', 
    'Iowa': 'IA', 'Michigan': 'MI', 'Kansas': 'KS', 'Utah': 'UT', 
    'Virginia': 'VA', 'Oregon': 'OR', 'Connecticut': 'CT', 'Montana': 'MT', 
    'California': 'CA', 'Massachusetts': 'MA', 'West Virginia': 'WV', 
    'South Carolina': 'SC', 'New Hampshire': 'NH', 'Wisconsin': 'WI',
    'Vermont': 'VT', 'Georgia': 'GA', 'North Dakota': 'ND', 
    'Pennsylvania': 'PA', 'Florida': 'FL', 'Alaska': 'AK', 'Kentucky': 'KY', 
    'Hawaii': 'HI', 'Nebraska': 'NE', 'Missouri': 'MO', 'Ohio': 'OH', 
    'Alabama': 'AL', 'Rhode Island': 'RI', 'South Dakota': 'SD', 
    'Colorado': 'CO', 'New Jersey': 'NJ', 'Washington': 'WA', 
    'North Carolina': 'NC', 'New York': 'NY', 'Texas': 'TX', 
    'Nevada': 'NV', 'Maine': 'ME'}

    df_filtered['state_code'] = df_filtered['state'].apply(lambda x : state_codes[x])

    if name_of_selectbox =='population':
        fig = px.choropleth(df_filtered,
                    locations='state_code', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='population',            
                    color_continuous_scale="Viridis_r",)
        st.write(fig)

    elif name_of_selectbox =='overallrank': 
         fig = px.choropleth(df_filtered,
                    locations='state_code', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='overallrank',            
                    color_continuous_scale="pinkyl",)
         st.write(fig)
    
    elif name_of_selectbox =='person_income_per_capita': 
         fig = px.choropleth(df_filtered,
                    locations='state_code', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='person_income_per_capita',            
                    color_continuous_scale="rdylgn",)
         st.write(fig)

   

