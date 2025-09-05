import streamlit as st
from backend import get_prediction
st.title("California Housing Data Input")

st.write("Please enter the housing details:")

# Input fields
longitude = st.number_input("Longitude", format="%.6f")
latitude = st.number_input("Latitude", format="%.6f")
housing_median_age = st.number_input("Housing Median Age", min_value=0)
total_rooms = st.number_input("Total Rooms", min_value=0)
total_bedrooms = st.number_input("Total Bedrooms", min_value=0)
population = st.number_input("Population", min_value=0)
households = st.number_input("Households", min_value=0)
median_income = st.number_input("Median Income", min_value=0.0, format="%.2f")

# Submit button
if st.button("Submit"):
    st.subheader("Entered Data")
    st.write({
        "longitude": longitude,
        "latitude": latitude,
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income
    })
    input_data=[longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population,households,median_income]
    result=get_prediction([input_data])
    st.write(result)

