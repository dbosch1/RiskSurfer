import yfinance as yf
import pandas as pd

def getStockData(tickers, period='1y'):
    """
    Fetches historical stock price data for the given tickers from Yahoo Finance.

    Parameters:
    tickers (list of str): List of stock tickers.
    period (str): The time period for which to fetch data, defaults to '1y' (1 year).

    Returns:
    pd.DataFrame: A DataFrame containing the stock price data for the given tickers over the specified period.
    """
    data = yf.download(tickers, period=period, group_by='ticker')
    return data
