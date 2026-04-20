import streamlit as st 
import requests
from streamlit_extras.let_it_rain import rain
st.title("This page will give you recommendations on what to do based on the weather")

actual_uv = None
city = st.text_input("Type in the City you want:", "Overland Park")
if st.button("Check the UV index") :
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_resp = requests.get(geo_url)
    if geo_resp.status_code == 200 and "results" in geo_resp.json():
        city_stuff = geo_resp.json()["results"][0]
        lat, lon = city_stuff["latitude"], city_stuff["longitude"]
        UV_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=uv_index_max&timezone=auto"
        UV_data = requests.get(UV_url)

        if UV_data.status_code == 200:
            actual_uv = UV_data.json()["daily"]["uv_index_max"][0]
else :
    st.write("Broski, ts is not a city 🤦‍♂️ ")

if actual_uv is not None:
    if 0 < actual_uv < 4:
        st.write(f"The Max UV index for today is {actual_uv}. Your chillin'. Just make to sure to protect your throughout the day")
        rain(
        emoji="👌",
        font_size=65,            
        falling_speed=5,       
        animation_length="5",   
    )
    elif 3 < actual_uv < 7:
        st.write(f"The Max UV index for today is {actual_uv}. Man. Its getting bad. Make sure to put on SPF")
        rain(
        emoji="🧴",
        font_size=65,            
        falling_speed=5,        
        animation_length="5",   
    )
    elif 7 < actual_uv < 9:
        st.write(f"The Max UV index for today is {actual_uv}. THAT IS VERY BAD, DON'T GO OUTSIDE, STAY INSIDE AND BINGE OR SOMETHIN' IDK!!")
        rain(
        emoji="🥵",
        font_size=65,           
        falling_speed=5,        
        animation_length="5",   
    )
    else:
        st.write(f"The Max UV index for today is {actual_uv}. Is that even possible?!")
        rain(
        emoji="🤨",
        font_size=65,            
        falling_speed=5,         
        animation_length="5",   
        )