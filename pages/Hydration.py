import streamlit as st

facial_stage = ""
st.subheader("Water intake")
water = st.slider("How many cups of water do you drink in a day?", 0, 20, 0)
st.write("---")
st.subheader("Coffee intake")
caffine = st.slider("How many cups of coffee did you have today?", 0, 15, 0)

percentage = water * 12.5 - caffine * 10

st.subheader(f"Your facial hydration for today is {percentage}%")
if caffine > 3 :
    if percentage > 80 :
        st.write(":rainbow[Even though your hydration is good... DONT DRINK THAT MUCH COFFEE!!]")

if percentage < 70 :
    facial_stage = "Dehydrated"
if 70 < percentage < 100 :
    facial_stage = "Bueno 👌"
if 110 < percentage :
    facial_stage = "Plump"

st.write(f"Face quality: {facial_stage}")