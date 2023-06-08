import streamlit as st
from beebotte import *
import time
import pandas as pd
import numpy as np

def display_sensor_data():
    # Setup Beebotte data transfer
    API_KEY = "2D1dB51ox1vLwp069wmpx9XD"
    SECRET_KEY = "S3wZ1rhnx39zG1iBQZcvxsXnWZYlKQCQ"

    bclient = BBT(API_KEY,SECRET_KEY)

    channel = bclient.getChannel('Temp_Humidity')
    temp_resource = Resource(bclient, 'Temp_Humidity', 'Temperature')
    hmid_resource = Resource(bclient, 'Temp_Humidity', 'Humidity')

    # Header Text for the webpage
    st.title("Temperature and Humidity Dashboard")

    frame = st.empty()

    # Read beebotte data
    temp_records = temp_resource.read()
    hmid_records = hmid_resource.read()

    temp_df = pd.DataFrame(temp_records)
    hmid_df = pd.DataFrame(hmid_records)

    # Collect temperature and humidity data, exclude other info
    temp_data = temp_df#['data']
    hmid_data = hmid_df#['data']

    # Display the data 
    with frame.container():
        # Display Average Values 
        avg1, avg2 = st.columns(2)

        average_one = round(np.mean(temp_data['data']))
        average_two = round(np.mean(hmid_data['data']))

        avg1.metric(
            label="Average Temperature",
            value=average_one
        )
        avg2.metric(
            label="Average Humidity",
            value=average_two
        )

        # Line Chart with the data
        column_one, column_two = st.columns(2)
        with column_one:
            st.markdown("## Temperature Data")
            st.line_chart(temp_data['data'])
        with column_two:
            st.markdown("## Humidity Data")
            st.line_chart(hmid_data['data'])

