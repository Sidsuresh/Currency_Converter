# AT2 - Building Currency Converter in Python

## Author

Name: Siddharth Nair
Student ID: 25548684

## Description

- FUNCTIONALITIES OF THE APPLICATION -
  This project is a **currency converter web application** built using **Streamlit** in Python. It integrates with the open-source [Frankfurter API](https://www.frankfurter.app), which provides users with real-time and historical exchange rate data. This application helps users:

* **Convert between any two supported currencies** by entering an amount and selecting the source and target currency codes.
* **Fetch the latest conversion rates**, along with the calculated converted amount and the inverse rate for transparency.
* **Retrieve historical rates** by selecting a specific date from a calendar input, giving users the ability to review past conversion values.
* **Visualize long-term trends** in exchange rates by selecting a number of years, after which the app plots a quarterly trend line chart for the chosen currency pair.

The goal of the app is to make foreign exchange information easily accessible in a clean, interactive, and user-friendly way without needing to query APIs directly.

- CHALLENGES FACED

* Handling API errors gracefully when data was unavailable or the request failed.
* Formatting the output consistently to match the assignment’s requirement.
* Ensuring Streamlit widgets worked together using `st.session_state`.
* Converting quarterly dates into a trend chart with consistent ordering.

- FUTURE WORKS

* Add support for multiple target currencies at once.
* Allow exporting conversion history as CSV.
* Implement caching for API calls to reduce network requests.

## How to Setup

<Provide a step-by-step description of how to get the development environment set and running.>
<Which Python version you used>
<Which packages and version you used>

## How to Run the Program

<Provide instructions and examples>

## Project Structure

<List all folders and files of this project and provide quick description for each of them>

## Citations

<Mention authors and provide links code you source externally>
