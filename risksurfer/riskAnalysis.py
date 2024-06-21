import yfinance as yf
import pandas as pd
import numpy as np

def compareStockPerformance(tickers, period='1y'):
    """
    Fetch stock data and compare the performance of multiple stocks over a specified period.

    Parameters:
    tickers (list): List of stock tickers to compare.
    period (str): The time period over which to fetch and compare performance.

    Returns:
    pd.DataFrame: DataFrame with the performance of each stock, ordered from best to worst cumulative return.
    """
    stockData = yf.download(tickers, period=period, group_by='ticker')
    performanceData = {}
    for ticker in tickers:
        if (ticker, 'Close') in stockData.columns:
            cumulativeReturn = (stockData[ticker, 'Close'][-1] / stockData[ticker, 'Close'][0] - 1) * 100
            performanceData[ticker] = cumulativeReturn

    performanceDf = pd.DataFrame.from_dict(performanceData, orient='index', columns=['Cumulative Return'])
    performanceDf = performanceDf.sort_values(by='Cumulative Return', ascending=False)

    return performanceDf

def calculateRiskMetrics(tickers, period='1y'):
    """
    Fetch stock data and calculate risk metrics for multiple stocks using the S&P 500 as a market benchmark.

    Parameters:
    tickers (list): List of stock tickers to analyze.
    period (str): The time period over which to fetch stock and market data.

    Returns:
    pd.DataFrame: DataFrame containing Beta, Sharpe Ratio, and Maximum Drawdown for each ticker.
    """
    stockData = yf.download(tickers, period=period, group_by='ticker')
    marketData = yf.download('^GSPC', period=period)['Close']
    marketReturns = marketData.pct_change().dropna()
    results = {}

    for ticker in tickers:
        if (ticker, 'Close') in stockData.columns:
            dailyReturns = stockData[ticker, 'Close'].pct_change().dropna()
            beta = dailyReturns.cov(marketReturns) / marketReturns.var()
            sharpeRatio = (dailyReturns.mean() / dailyReturns.std()) * np.sqrt(252)
            maxDrawdown = (stockData[ticker, 'Close'] / stockData[ticker, 'Close'].cummax() - 1).min()
            results[ticker] = {
                'Beta': beta,
                'Sharpe Ratio': sharpeRatio,
                'Maximum Drawdown': maxDrawdown
            }

    return pd.DataFrame(results).T

def calculateVaR(tickers, confidenceLevel=0.95, period='1y'):
    """
    Fetch stock data and calculate Value at Risk (VaR) for multiple stocks at a given confidence level.

    Parameters:
    tickers (list): List of stock tickers to analyze.
    confidenceLevel (float): Confidence level for VaR.
    period (str): The time period over which to fetch stock data.

    Returns:
    pd.Series: Series with VaR values for each ticker.
    """
    stockData = yf.download(tickers, period=period, group_by='ticker')
    varResults = {}
    for ticker in tickers:
        if (ticker, 'Close') in stockData.columns:
            dailyReturns = stockData[ticker, 'Close'].pct_change().dropna()
            VaR = np.percentile(dailyReturns, (1 - confidenceLevel) * 100)
            varResults[ticker] = VaR

    return pd.Series(varResults, name='VaR')

def calculateCVaR(tickers, confidenceLevel=0.95, period='1y'):
    """
    Fetch stock data and calculate Conditional Value at Risk (CVaR) for multiple stocks at a given confidence level.

    Parameters:
    tickers (list): List of stock tickers to analyze.
    confidenceLevel (float): Confidence level for CVaR.
    period (str): The time period over which to fetch stock data.

    Returns:
    pd.Series: Series with CVaR values for each ticker.
    """
    stockData = yf.download(tickers, period=period, group_by='ticker')
    cvarResults = {}
    for ticker in tickers:
        if (ticker, 'Close') in stockData.columns:
            dailyReturns = stockData[ticker, 'Close'].pct_change().dropna()
            VaR = np.percentile(dailyReturns, (1 - confidenceLevel) * 100)
            CVaR = dailyReturns[dailyReturns <= VaR].mean()
            cvarResults[ticker] = CVaR

    return pd.Series(cvarResults, name='CVaR')
