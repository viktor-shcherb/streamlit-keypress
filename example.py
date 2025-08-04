import streamlit as st
from streamlit_keypress import key_press_events

st.title("Streamlit Keypress Demo")
st.write("Press any key on your keyboard")

if "history" not in st.session_state:
    st.session_state["history"] = []

key = key_press_events()
if key:
    st.session_state["history"].append(key)

st.write(f"Pressing history: {st.session_state['history']}")
