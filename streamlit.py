import streamlit as st
import time

st.title('Startup Dashbord')
st.header('I am learning streamlit')
st.subheader('FUCK YOU')

st.write('crrr')

st.markdown("""
### Horror
- conjuring
- heredetry
""")

st.metric('revenue','Rs 3cr','-4%')

st.sidebar.title('sidebar ka title')

st.error('login failed')
st.success('login sucessfull')

bar=st.progress(0)
for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)