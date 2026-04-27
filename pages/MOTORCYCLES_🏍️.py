import streamlit as st

st.title("If ur ridin' today, better put that SPF")
st.subheader("In the meantime look at these bikes 🏍️")
st.write("")
st.write("---")
st.image("images/kawasaki.png", caption="KAWASAKI NINJA", width=600)
st.write("---")
st.write("")
st.image("images/scrambler.png", caption="Ducati SCRAMBLER", width=600)

st.write("After all of that looking you probably want some relazing")
if st.button("Click here for GAMES"):
    st.toast("YOU REALLY WANT TO PLAY GAMES!!? BAD BOY/GIRL... idk", icon="😡")