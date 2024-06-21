import yfinance as yf
import pandas as pd
import numpy as np

def getTickerEsgScores(tickers):
    """
    Generate random ESG scores for the given tickers.

    Parameters:
    tickers (list): The list of stock tickers.

    Returns:
    pd.DataFrame: DataFrame of tickers with their ESG scores.
    """
    np.random.seed(42)  # For reproducible random results
    esg_scores = np.random.randint(50, 100, size=len(tickers))
    esgDf = pd.DataFrame({'Ticker': tickers, 'ESG Score': esg_scores})
    esgDf = esgDf.set_index('Ticker')
    return esgDf.mean()['ESG Score'], esgDf
