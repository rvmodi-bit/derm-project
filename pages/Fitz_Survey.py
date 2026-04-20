import streamlit as st
import numpy as np 

fpscale = 0
before_score = 0
eye_number = {"Blue/Green": 0, "Grey": 1, "Light Brown": 2, "Brown": 3, "Dark Brown": 4}
eye_color = st.selectbox("Eye color", ["Blue/Green", "Grey", "Light Brown", "Brown", "Dark Brown"])

hair_number = {"Blonde": 0, "Light red": 1, "Dirty blonde, chestnut": 2, "Light Brown": 3, "Dark Brown, Black": 4}
hair_color = st.selectbox("Hair color", ["Blonde", "Light red", "Dirty blonde, chestnut", "Light Brown", "Dark Brown, Black"])

# continue here tmrw
skin_number = {"Very pale": 0, "Beige": 1, "Brown": 2, "Dark Brown":3, "Black": 4}
skin_color = st.selectbox("Skin color", ["Very pale", "Beige", "Brown", "Dark Brown", "Black"])

burn_number = {"Very painful/peeling": 0, "Strong burn": 1, "Average pain": 2, "Slight burning": 3, "No burning": 4}
burn_intes = st.selectbox("When you go out in the sun for too long how bad if your burn", ["Very painful/peeling", "Strong burn", "Average pain", "Slight burning", "No burning"])

tan_number = {"Instant tan": 0, "Easily tanned": 1, "Tanned in an average time": 2, "Long time to tan":3, "No tan": 4}
tan_intes = st.selectbox("Skin color", ["Instant tan", "Easily tanned", "Tanned in an average time", "Long time to tan", "No tan"])

freckles_number = {"A lot of freckles": 0, "High amount of freckles": 1, "Moderate freckles": 2, "Partial freckles": 3, "No freckles": 4}
freckles_amount = st.select_slider("Select the amount of freckles you have",
                                   options = ["A lot of freckles", "High amount of freckles", "Moderate freckles", "Partial freckles", "No freckles"]
                                   )

before_score += eye_number[eye_color]
before_score += hair_number[hair_color]
before_score += skin_number[skin_color]
before_score += burn_number[burn_intes]
before_score += tan_number[tan_intes]
before_score += freckles_number[freckles_amount]

if -1 < before_score < 5:
    fpscale = 1
if 4 < before_score < 9:
    fpscale = 2
if 8 < before_score < 13:
    fpscale = 3
if 12 < before_score < 17:
    fpscale = 4
if 16 < before_score < 21:
    fpscale = 5
if 20 < before_score < 25:
    fpscale = 6

st.header("Results")
st.subheader(f"Your Fitzpatrick score is {before_score}/24")
st.write(f"That means that you're {fpscale} on the Fitzpatrick scale")


