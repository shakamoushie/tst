import streamlit as st
from st_screen_stats import ScreenData     # pip install streamlit-screen-stats

screenD = ScreenData(setTimeout=1000)
screen_d = screenD.st_screen_data_window_top()
st.write(f"screen_d: {screen_d}")
