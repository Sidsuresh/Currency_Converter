from api import get_url
import json
from datetime import datetime, timedelta

BASE_URL = "https://api.frankfurter.dev/v1"

def get_currencies_list():
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the list of available currencies.
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the list of currency codes and return it as Python list.
    Otherwise it will return the value None.

    Parameters
    ----------
    None

    Returns
    -------
    list
        List of available currencies or None in case of error
    """
    # Call the currencies endpoint from Frankfurter API
    endpoint_url = f"{BASE_URL}/currencies"
    # Make the API call
    response = get_url(endpoint_url)
    # Check if the API call was successful
    if response[0] == 200:
        # Extract the list of currency codes from the response JSON and return it as a Python list
        currencies = list(response[1].keys())
        return currencies
    # Otherwise return None
    else:
        return None
    

def get_latest_rates(from_currency, to_currency, amount):
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the latest conversion rate between the provided currencies. 
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the latest conversion rate and the date and return them as 2 separate objects.
    Otherwise it will return the value None twice.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted

    Returns
    -------
    str
        Date of latest FX conversion rate or None in case of error
    float
        Latest FX conversion rate or None in case of error
    """
    # Call the latest rates endpoint from Frankfurter API with the provided currencies
    endpoint_url = f"{BASE_URL}/latest?base={from_currency}&symbols={to_currency}"
    # Make the API call
    response = get_url(endpoint_url)
    # Check if the API call was successful
    if response[0] == 200:
        # Load the response as JSON
        response_json = response[1]
        # Extract the date and rate from the response JSON
        date = response_json.get("date")
        rate = response_json.get("rates", {}).get(to_currency)

        # Return the date and rate as 2 separate objects
        return date, rate
    
    # Otherwise return None twice
    else:
        return None, None

    

def get_historical_rate(from_currency, to_currency, from_date, amount):
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the conversion rate for the given currencies and date
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the conversion rate and return it.
    Otherwise it will return the value None.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    from_date : str
        Date when the conversion rate was recorded

    Returns
    -------
    float
        Latest FX conversion rate or None in case of error
    """
    # Call the historical rates endpoint from Frankfurter API with the provided currencies and date
    endpoint_url = f"{BASE_URL}/{from_date}?base={from_currency}&symbols={to_currency}"
    # Make the API call
    response = get_url(endpoint_url)
    # Check if the API call was successful
    if response[0] == 200:
        # Load the response as JSON
        response_json = response[1]
        # Extract the rate from the response JSON
        rate = response_json.get("rates", {}).get(to_currency)
        return rate
    # Otherwise return None
    else:
        return None

def get_rate_trend(from_currency: str, to_currency: str, years: int) -> dict:
    """
    Fetches historical rates for the past N years on a quarterly basis and returns a dictionary with dates as keys and rates as values.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    years : int
        Number of years in the past for which to fetch rates

    Returns
    -------
    dict
        Dictionary containing dates and their corresponding rates
    """
    # Calculate the start and end dates for the historical data
    end_date = datetime.today()
    start_date = end_date - timedelta(days = years * 365)

    # Initialise a list that will store the quarterly dates within the specified range
    quarterly_dates = []
    
    # Calculate the number of quarters which will be the number of loop iterations
    quarters = years * 4

    # Start from the end date and move backwards in 3-month increments
    current = end_date

    # Loop to generate the quarterly dates
    for _ in range(quarters):

        # Append the current date to the list
        quarterly_dates.append(current)

        # Move back by 3 months
        month = current.month - 3
        year = current.year

        # Adjust the year if month goes below 1
        if month <= 0:
            month += 12
            year -= 1
        
        # Set the current date to the first day of the new month and year
        current = current.replace(year=year, month=month, day=1)

    # Sort the list of quarterly dates in ascending order
    quarterly_dates = sorted(quarterly_dates)

    # Call the historical rates endpoint from Frankfurter API with the provided currencies and date range
    endpoint_url = f"{BASE_URL}/{start_date.date()}..{end_date.date()}?base={from_currency}&symbols={to_currency}"
    # Make the API call
    response = get_url(endpoint_url)
    # Check if the API call was successful
    if response[0] == 200:
        # Load the response as JSON
        response_json = response[1]
        # Extract the rates for the quarterly dates
        rates = response_json.get("rates", {})
        # Convert the date strings in the rates dictionary to datetime objects for comparison
        sorted_rates = sorted(datetime.strptime(d, "%Y-%m-%d") for d in rates.keys())

        # Initialise a dictionary to store the quarterly rates
        quarterly_rates = {}

        # Find the nearest available date in the rates for each quarterly date
        for marker in quarterly_dates:
            # Find the nearest date in the available rates
            nearest_date = min(sorted_rates, key=lambda d: abs(d - marker))
            # Convert the nearest date back to string format
            nearest_str = nearest_date.strftime("%Y-%m-%d")
            
            # Create the label for the x-axis
            # Find the year and month of the nearest date for the label
            year = nearest_date.year
            month = nearest_date.strftime("%b")            
            label = f"{year}-{month}"

            # Add the rate for the nearest date to the quarterly rates dictionary
            quarterly_rates[label] = rates[nearest_str][to_currency]

        # Return the quarterly rates dictionary
        return quarterly_rates
    
    # Otherwise return an empty dictionary
    else:
        return {}
        
