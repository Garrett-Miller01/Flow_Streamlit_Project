import streamlit as st
import pandas as pd
import numpy as np
import time
from bike_api import make_request
import math
import geocoder

def find_distance(lat1,lon1,lat2,lon2):
    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Earth's radius in kilometers
    radius = 6371

    # Difference between latitudes and longitudes
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine formula
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c

    return distance

def bike_map():

    with st.form("user_coords"):
        location_df = pd.DataFrame({'LATITUDE':[43.610767], 'LONGITUDE':[3.876716]})

        st.markdown("## Bike Rental Station Locator")
        user_lat = st.number_input('Insert a latitude coordinate')
        user_long = st.number_input('Insert a longitude coordinate')

        column_one, column_two = st.columns(2)
        with column_one:
            submitted = st.form_submit_button("Submit")
        with column_two:
            current_location = st.form_submit_button("Use Current Location")

        if current_location:
            g = geocoder.ip('me')
            if g.ok:
                user_lat, user_long = g.latlng
                submitted = True
                st.write("User Latitude :", user_lat, "User Longitude :", user_long)
                

        if submitted:
            #make_request()

            station_data = pd.read_csv('FLOW2023Project/BikeStations.csv')

            station_df = pd.DataFrame(station_data)

            location_df = pd.DataFrame({'LATITUDE':[user_lat], 'LONGITUDE':[user_long]})

            nearest_bike = {'LATITUDE':[0], 'LONGITUDE':[0]}
            shortest_distance = 10000
            nearby_street = ''
            available_bikes = 0
            for index, row in station_df.iterrows():
                # Get the lat and long of the current station
                station_lat = row['Latitude']
                station_long = row['Longitude']
                # Find the distance from the user
                current_distance = find_distance(user_lat,user_long,station_lat,station_long)
                # Check to see if this station is closer
                if current_distance < shortest_distance and row['availableBikeNumber'] > 0:
                    # If it is closer than the previous closet stop, update it
                    shortest_distance = current_distance
                    nearest_bike = {'LATITUDE':[station_lat], 'LONGITUDE':[station_long]}
                    nearby_street = row['Street']
                    available_bikes = row['availableBikeNumber']

            st.markdown("## Closest Rental Station")
            column_one, column_two, column_three, column_four, column_five = st.columns(5)
            with column_one:
                st.write("Station Latitude :", station_lat)
            with column_two:
                st.write("Station Longitude :", station_long)
            with column_three:
                st.write("Street Location :", nearby_street)
            with column_four:
                st.write("Distance :", round(current_distance,2))
            with column_five:
                st.write("There are",available_bikes,"bikes available")

            closest_station = pd.DataFrame(nearest_bike)
            location_df = pd.concat([location_df, closest_station])


        st.map(location_df)
