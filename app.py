import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('startup_cleaned.csv')
st.set_page_config(page_title='Startup Analysis')


df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month


def load_overall_analysis():
    st.title('Over all analysis')
    #total invested analysis
    total = round(df['amount'].sum())

    #max amount infused in a startup
    max_funding=df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]

    # avg ticket (funding amount) size is
    avg_funding=df.groupby('startup')['amount'].sum().mean()

    # total funded startups
    total =df['startup'].nunique()

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric('Total', str(total) + ' Cr')
    with col2:
        st.metric('Max', str(max_funding) + ' Cr')

    with col3:
        st.metric('Avg', str(round(avg_funding)) + ' Cr')

    with col4:
        st.metric('Funded Startups', str(total))

    st.header('MoM graph')
    selected_option = st.selectbox('Select Type',['Total','count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')

    fig,ax =plt.subplots()
    ax.plot(temp_df['x_axis'],temp_df['amount'])
    st.pyplot(fig)

def load_startup_details(startup):
    st.title(startup)
    least_5=df[df['startup'].str.contains(startup)].head()[['date','startup','vertical','city','round','investors','amount']]
    st.subheader('most recent startup')
    st.dataframe(least_5)
st.sidebar.title('Startup Funding Analysis')

option =st.sidebar.selectbox('select one' , ['overall analysis','Startup'])

if option == 'overall analysis':
        load_overall_analysis()

elif option == 'Startup':
    selected_investor=st.sidebar.selectbox('select startup',sorted(df['startup'].unique().tolist()))
    btn=st.sidebar.button('Find startUp Details')
    if btn:
        load_startup_details(selected_investor)


