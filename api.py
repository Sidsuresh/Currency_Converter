import requests

def get_url(url: str) -> int | str:
    """
    Function that will call a provided GET API endpoint url and return its status code and either its content or error message as a string

    Parameters
    ----------
    url : str
        URL of the GET API endpoint to be called

    Returns
    -------
    int
        API call response status code
    str
        Text from API call response
    """
    try:
        # Make the GET API call
        response = requests.get(url)
        # Return the status code and content of the response as JSON
        return response.status_code, response.json()
    except Exception as e:
        # In case of error, return status code 500 and the error message as a string
        return 500, str(e)