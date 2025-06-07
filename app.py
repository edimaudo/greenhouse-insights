import streamlit as st

pg = st.navigation([
    st.Page("About.py", icon="💬"),
    st.Page("Planet_Heater.py", icon="🌍"),
    st.Page("Carbon_Chronicles.py", icon="🔥"),
    st.Page("Greener_Faster.py", icon="🔍"),
])
pg.run()