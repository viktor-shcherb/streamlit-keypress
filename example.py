import streamlit as st
from streamlit_keypress import key_press_events

st.title("Streamlit Keypress Demo")
st.write("Press any key on your keyboard")

key = key_press_events()
if key:
    st.write(f"You pressed: {key}")