import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# load dataset
country_covid_stat = pd.read_csv("./country_covid_status.csv")
covid_data = pd.read_csv("./covid_data.csv")

st.dataframe(country_covid_stat.style.highlight_max(axis=0))
st.dataframe(covid_data)

selected_country = st.sidebar.selectbox("Choose a Country", country_covid_stat["Country"])

country_dataframe = country_covid_stat[country_covid_stat["Country"] == selected_country]
country_dataframe = country_dataframe.drop(["Country", "Country_code"], axis=1)

st.dataframe(country_dataframe.style.highlight_max(axis=0))


country_covid_data = covid_data[covid_data["Country"] == selected_country]

# output country new_case, new_deaths
country_new_case = country_covid_data["New_cases"]
country_new_deaths = country_covid_data["New_deaths"]
date = country_covid_data["Date_reported"]

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("page1", "page2")
)

if add_selectbox == "page1":
    fig, ax = plt.subplots(2, figsize=(20, 12))
    ax[0].plot(date, country_new_case)
    ax[1].plot(date, country_new_deaths)
    st.pyplot(fig)
else:
    fig, ax = plt.subplots()
    ax.scatter(country_covid_stat["gdp_per_capita"], country_covid_stat["deaths_by_cases"])
    st.pyplot(fig)