# stock-api-project-in-python
This program fetches the latest stock price data for a given stock symbol (in this case, "TSLA" for Tesla Inc) using the Alpha Vantage API. The program also uses the News API to fetch the latest news articles related to the company.

The program first defines the endpoints for the two APIs and sets the required parameters for the Alpha Vantage API, such as the function (intraday time series), the stock symbol, the interval (5 minutes), and the API key. The requests.get() method is then used to send an HTTP GET request to the API endpoint, passing in the parameters using the params argument. The raise_for_status() method is called on the response object to raise an exception if there was an error with the request.

The response object is then converted to a JSON object using the json() method, and the stock data is extracted from the response using a list comprehension. The data_list variable contains a list of values for each time interval, where each value is a dictionary containing the open, high, low, and close prices, as well as the volume and timestamp.

This program only fetches the stock price data, but you could modify it to fetch news articles using the News API and display the results in a more user-friendly way.
