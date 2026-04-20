import streamlit as st 
import requests
st.title("This page will give you recommendations on what to do based on the weather")

city = st.text_input("Type in the City you want:", "Overland Park")
if st.button("Check the UV index") :
    geo_url = f"https://open-meteo.com{name}&count=1"
    geo_resp = requests.get(geo_url)
    if geo_resp.status_code == 200 and "results" in geo_resp.json():
        st.write("hei")