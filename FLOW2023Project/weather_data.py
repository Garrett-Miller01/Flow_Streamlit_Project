import streamlit as st
import requests

def weather():
    #--------------------------------------------------------------------------------------
    def get_weather_by_city(api_key, city):
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                return None

    api_key = "055b2dc0383f0ae92acbac6336e462ee"

    #-------------------------------------------------------------------------------------- Weather in Montpellier

    st.header("Current Weather in Montpellier")

    weather_data = get_weather_by_city(api_key, 'Montpellier')

    if weather_data:
        weather_description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        
        column_one, column_two, column_three = st.columns(3)
        with column_one:
            st.write("Description:", weather_description)    
        with column_two:
            st.write("Temperature:", temperature, "C°")
        with column_three:
            st.write("Humidity:", humidity, "%")

    else:
        st.write("Failed to fetch weather data.")

    
    #------------------------------------------------------------------------------- FETCHING WEATHER BY City
    with st.form('city_weather'):

        st.header("Weather Info for a City")

        city_name = st.text_input('Insert a City Name')
        submitted = st.form_submit_button("Submit")

        if submitted:
            weather_data = get_weather_by_city(api_key, city_name)
            
            if weather_data:
                weather_description = weather_data['weather'][0]['description']
                temperature = weather_data['main']['temp']
                humidity = weather_data['main']['humidity']
                
                st.header("Current Weather in " + city_name)
                column_one, column_two, column_three = st.columns(3)
                with column_one:
                    st.write("Description:", weather_description)    
                with column_two:
                    st.write("Temperature:", temperature, "C°")
                with column_three:
                    st.write("Humidity:", humidity, "%")
            else:
                st.write("Failed to fetch weather data.")
