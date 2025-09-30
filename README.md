# AT2 - Building Currency Converter in Python

## Author

Name: Siddharth Nair

Student ID: 25548684

## Description

- FUNCTIONALITIES OF THE APPLICATION

  This project is a **currency converter web application** built using **Streamlit** in Python. It integrates with the open-source [Frankfurter API](https://frankfurter.dev/), which provides users with real-time and historical exchange rate data. This application helps users:

1. **Convert between any two supported currencies** by entering an amount and selecting the source and target currency codes.
2. **Fetch the latest conversion rates**, along with the calculated converted amount and the inverse rate for transparency.
3. **Retrieve historical rates** by selecting a specific date from a calendar input, giving users the ability to review past conversion values.
4. **Visualize long-term trends** in exchange rates by selecting a number of years, after which the app plots a quarterly trend line chart for the chosen currency pair.

The goal of the app is to make foreign exchange information easily accessible in a clean, interactive, and user-friendly way without needing to query APIs directly.

- CHALLENGES FACED

1. Handling API errors gracefully when data was unavailable or the request failed.
2. Formatting the output consistently to match the assignment’s requirement.
3. Ensuring Streamlit widgets worked together using `st.session_state`.
4. Converting quarterly dates into a trend chart with consistent ordering.

- FUTURE WORKS

1. Add support for multiple target currencies at once.
2. Allow exporting conversion history as CSV.
3. Implement caching for API calls to reduce network requests.

## How to Setup

- STEPS TO SET-UP

1. **Clone or download** the project zip file and extract the contents.

   ```bash
   dsp_at2_25548684.zip
   ```

   Alternatively, **clone the [GITHUB REPO](https://github.com/Sidsuresh/Currency_Converter)**.

   ```bash
   git clone https://github.com/Sidsuresh/Currency_Converter.git
   ```

2. **Install [VSCode](https://code.visualstudio.com/)** or your preferred IDE.
3. **Install [Python](https://www.python.org/downloads/)**, above version 3.10. Python version 3.12.3 was used for this project.
4. **Install the required packages**

```bash
   a. streamlit==1.36.0  # Provides an easy way to build interactive web apps for data visualization and machine learning projects.
   b. pandas==2.2.2 # Offers powerful tools for data manipulation, analysis, and handling tabular datasets.
   c. requests==2.32.3 # Simplifies making HTTP requests to APIs and retrieving data from the web.
```

## How to Run the Program

1. **Open your preferred terminal** and **navigate to the project folder**
2. **Run the streamlit server**

```bash
streamlit run app.py
```

This will start a local Streamlit server (usually on http://localhost:8501) and open the app in your browser.

### Example Usage

1. Enter an amount (e.g., 100).
2. Select a from currency (AUD) and a to currency (BGN).
3. Click "Get Latest Rate" to see

```bash
The conversion rate on 2025-09-29 from AUD to BGN was 1.0951. So, 1.0 in AUD corresponds to 1.0951 in BGN. The inverse rate is 0.9132.
```

4. Use the date picker to select a past date and fetch historical rates.
5. Use the slider to view a quarterly trend over the last N years (line chart).

## Project Structure

The files present in this project include:

```bash
app.py           # Main Streamlit app handling UI and user inputs
api.py           # Helper functions for making HTTP requests to the Frankfurter API
frankfurter.py   # Functions to fetch currency list, latest rate, historical rates, and rate trends
currency.py      # Utility functions: rounding rates, inverse rate, formatting output text
README.md        # Project documentation
```

## Citations

1. [Frankfurter API Docs](https://frankfurter.dev/) - Used for currency exchange endpoints.
2. [Streamlit Docs](https://docs.streamlit.io/) - For building the web interface.
3. [Requests Library Documentation](https://requests.readthedocs.io/en/latest/) - For handling HTTP requests.
   All code in this project was written by **Siddharth Nair (25548684)**, except where adapted from the above references.
