
def round_rate(rate):
    """
    Function that will round an input float to 4 decimals places.

    Parameters
    ----------
    rate: float
        Rate to be rounded

    Returns
    -------
    float
        Rounded rate
    """
    # Round the input rate to 4 decimal places and return it
    return round(float(rate), 4)
    

def reverse_rate(rate):
    """
    Function that will calculate the inverse rate from the provided input rate.
    It will check if the provided input rate is not equal to zero.
    If it not the case, it will calculate the inverse rate and round it to 4 decimal places.
    Otherwise it will return zero.

    Parameters
    ----------
    rate: float
        FX conversion rate to be inverted

    Returns
    -------
    float
        Inverse of input FX conversion rate
    """
    # Check if the input rate is not equal to zero
    if rate != 0:
        # Calculate the inverse rate and round it to 4 decimal places
        inverse_rate = 1 / rate
        return round_rate(inverse_rate)
    
    # If the input rate is zero, return zero
    else:
        return 0.0
    
def format_output(date, from_currency, to_currency, rate, amount):
    """
    Function that will format the text to be displayed in the Streamlit app.

    Parameters
    ----------
    date: str
        Date of the conversion rate
    from_currency: str
        Origin currency code
    to_currency: str
        Destination currency code
    rate: float
        Conversion rate
    amount: float
        Amount to be converted

    Returns
    -------
    str
        Formatted text for display
    """
    # Round the input amount to 4 decimal places
    amount = round_rate(amount)
    # Round the input rate to 4 decimal places
    rate = round_rate(rate)
    # Calculate the converted amount
    converted_amount = round_rate(rate * amount)
    # Calculate the inverse rate
    inv_rate = round_rate(reverse_rate(rate))
    # Format the output string and return it
    output_str = f"The conversion rate on {date} from {from_currency} to {to_currency} was {rate}. So, {amount} in {from_currency} corresponds to {converted_amount} in {to_currency}. The inverse rate is {inv_rate}."
    return output_str


   