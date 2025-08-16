import streamlit as st

pg = st.navigation([
    st.Page("About.py"),
    st.Page("Planet_Heater.py"),
    st.Page("Carbon_Chronicles.py"),
    st.Page("Greener_Faster.py"),
])
pg.run()