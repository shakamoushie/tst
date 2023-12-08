import streamlit as st
from st_screen_stats import ScreenData     # pip install streamlit-screen-stats


def DetermineLoginDevice():
    screenD = ScreenData(setTimeout=1000)
    screen_stats = screenD.st_screen_data_window_top()

    return "mobile" if screen_stats['screen']['width'] <= 400 or screen_stats['screen']['height'] <= 400 else "laptop"

st.info(f"Login device = {DetermineLoginDevice()}")