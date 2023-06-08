import streamlit as st
from th_data import display_sensor_data
from bikeMap import bike_map
from route_planner import plan_route
from weather_data import weather

st.set_page_config(
    page_title = 'Green Path',
    page_icon = 'favicon.ico',
    layout = 'wide'
)

st.header("Montpellier Guide App")

tab_one, tab_two, tab_three = st.tabs(["Current Weather", "Bike Rental Locator", "Live Sensor Data"])

with tab_one:
   weather()

with tab_two:
   bike_map()

with tab_three:
   display_sensor_data()



#plan_route()