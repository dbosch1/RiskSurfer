import matplotlib.pyplot as plt
from risksurfer.riskAnalysis import compareStockPerformance, calculateRiskMetrics, calculateVaR, calculateCVaR

def plotStockPerformance(tickers, period='1y'):
    performanceDf = compareStockPerformance(tickers, period)
    plt.figure(figsize=(10, 6))
    performanceDf['Cumulative Return'].plot(kind='bar', color='skyblue')
    plt.title('Stock Performance Comparison')
    plt.xlabel('Ticker')
    plt.ylabel('Cumulative Return (%)')
    plt.grid(True)
    plt.show()

def plotRiskMetrics(tickers, period='1y'):
    riskMetrics = calculateRiskMetrics(tickers, period)
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 12))

    riskMetrics['Beta'].plot(ax=axes[0], kind='bar', color='orange')
    axes[0].set_title('Beta of Each Stock')
    axes[0].set_ylabel('Beta')

    riskMetrics['Sharpe Ratio'].plot(ax=axes[1], kind='bar', color='green')
    axes[1].set_title('Sharpe Ratio of Each Stock')
    axes[1].set_ylabel('Sharpe Ratio')

    riskMetrics['Maximum Drawdown'].plot(ax=axes[2], kind='bar', color='red')
    axes[2].set_title('Maximum Drawdown of Each Stock')
    axes[2].set_ylabel('Maximum Drawdown')

    plt.tight_layout()
    plt.show()

def plotVaRAndCVaR(tickers, confidenceLevel=0.95, period='1y'):
    varValues = calculateVaR(tickers, confidenceLevel, period)
    cvarValues = calculateCVaR(tickers, confidenceLevel, period)

    fig, ax = plt.subplots(figsize=(10, 6))
    varValues.plot(ax=ax, kind='bar', color='blue', label='VaR')
    cvarValues.plot(ax=ax, kind='bar', color='red', alpha=0.7, label='CVaR')
    plt.title('VaR and CVaR Comparison')
    plt.xlabel('Ticker')
    plt.ylabel('Value at Risk / Conditional VaR')
    plt.legend()
    plt.grid(True)
    plt.show()
