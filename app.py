import streamlit as st
import datetime
import pandas as pd

from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate, get_rate_trend
from currency import reverse_rate, round_rate, format_output

# ------------------------ Display Streamlit App Title -------------------------
st.title("FX Converter")

# ------------------------ Get the list of available currencies from Frankfurter -----------------
# Call the function to get the list of available currencies
available_currencies = get_currencies_list()

# ------------------------ If the list of available currencies is None, display an error message in Streamlit App ------------------------
if available_currencies is None:
    st.error("Error: Unable to fetch the list of available currencies.")

# ------------------------ Add input fields for capturing amount, from and to currencies ------------------------
st.number_input("Enter the amount to be converted: ", min_value = 0.0, value = 1.0, step = 0.1, format = "%.2f", key = "amount")
st.selectbox("From Currency: ", options = available_currencies, index = 0, key = "from_currency")
st.selectbox("To Currency: ", options = available_currencies, index = 1, key = "to_currency")

# ------------------------ Add a button to get and display the latest rate for selected currencies and amount ------------------------
if st.button("Get Latest Rate", key = "latest_rate_button"):
    # Create a header for the latest conversion rate
    st.header("Latest Conversion Rate")
    # Call the function to get the latest rate
    date, rate = get_latest_rates(st.session_state.from_currency, st.session_state.to_currency, st.session_state.amount)
    
    # If the date and rate are not None, display the formatted output in Streamlit App
    if date is not None and rate is not None:
        st.text(format_output(date, st.session_state.from_currency, st.session_state.to_currency, rate, st.session_state.amount))

    # Otherwise, display an error message in Streamlit App    
    else:
        st.error("Error: Unable to fetch the latest conversion rate.")

# ------------------------ Add a year selector (slider) ------------------------
st.slider("Select number of years for historical rate: ", min_value = 1, max_value = 10, value = 1, step = 1, key = "years")

# ------------------------ Add a button to get and display the historical rate for selected currencies, amount and number of years ------------------------
if st.button("Get Historical Rate Trend", key = "historical_rate_years_button"):
    # Create a header for the historical conversion rate trend
    st.header(f"Rate Trend over the last {st.session_state.years} years")
    # Call the function to get the historical rate trend
    rate_trend = get_rate_trend(st.session_state.from_currency, st.session_state.to_currency, st.session_state.years)
    
    # If the rate trend is not None, display the rate trend in Streamlit App
    if rate_trend != {}:
        # Create a DataFrame from the rate trend dictionary
        rate_trend_df = pd.DataFrame(list(rate_trend.items()), columns = ["Quarter", "Rate"])
        # Set the "Quarter" column as a categorical variable with the correct order otherwise the line chart will be plotted based on 
        # alphabetical order of the quarter labels
        rate_trend_df["Quarter"] = pd.Categorical(rate_trend_df["Quarter"], categories=list(rate_trend.keys()), ordered=True)
        # Set the "Quarter" column as the index of the DataFrame and plot the line chart
        rate_trend_df = rate_trend_df.set_index("Quarter")
        # Display the line chart in Streamlit App
        st.line_chart(rate_trend_df, x_label = "Quarter", y_label = "Rate")

    # Otherwise, display an error message in Streamlit App
    else:
        st.error("Error: Unable to fetch the historical conversion rate trend.")

# ------------------------ Add a date selector (calendar) ------------------------
st.date_input("Select a date for historical rate: ", value = "today", key = "selected_date")

# ------------------------ Add a button to get and display the historical rate for selected date, currencies and amount ------------------------
if st.button("Conversion Rate", key = "historical_rate_button"):
    # Create a header for the conversion rate
    st.header("Conversion Rate")
    # Call the function to get the historical rate
    hist_rate = get_historical_rate(st.session_state.from_currency, st.session_state.to_currency, st.session_state.selected_date, st.session_state.amount)
    
    # If the historical rate is not None, display the formatted output in Streamlit App
    if hist_rate is not None:
        st.text(format_output(st.session_state.selected_date, st.session_state.from_currency, st.session_state.to_currency, hist_rate, st.session_state.amount))
    # Otherwise, display an error message in Streamlit App
    else:
        st.error("Error: Unable to fetch the historical conversion rate.")









