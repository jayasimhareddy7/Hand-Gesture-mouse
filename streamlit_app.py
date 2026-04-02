import streamlit as st
import subprocess

st.title("Hand Gesture Mouse Controller")
if st.button("Start Gesture Mouse"):
    subprocess.Popen(["python", "app.py"])
