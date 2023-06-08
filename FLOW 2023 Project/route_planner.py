import streamlit as st
import pandas as pd

def plan_route():
    with st.form("route"):
        st.markdown("## Plan a Route")
        start_address = st.text_input("Enter the Starting Street Address")
        stop_address = st.text_input("Enter the Destination Street Address")

        submitted = st.form_submit_button("Submit")

        if submitted:
            st.write(start_address,stop_address)