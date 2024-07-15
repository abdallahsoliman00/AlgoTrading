import matplotlib.pyplot as plt
import numpy as np
import time
import yfinance as yf


def get_ticker_info(symbol, sort=True):
    ticker = yf.Ticker(symbol).info
    keys = list(ticker.keys())
    f_name = ticker['shortName']
    if sort:
        keys.sort()
    with open(f'{f_name}_info.txt', 'w') as file:
        for i in keys:
            file.write(f'{i}\n')


def get_current_price(symbol="AAPL") -> float:
    # The Ticker() command needs to be re-updated in order to have the new values
    ticker = yf.Ticker(symbol).info
    return ticker["currentPrice"]


def get_data(ticker, start_date, end_date):
    data = yf.download(ticker, start_date, end_date)
    return data


def print_price(symbol, iterations=10):
    for i in range(iterations):
        print(get_current_price(symbol))
        time.sleep(1)


def compare_plots(s1, s2, start, end, same_plot=True):
    t1 = get_data(s1, start, end)
    t2 = get_data(s2, start, end)
    n1 = yf.Ticker(s1).info['shortName']
    n2 = yf.Ticker(s2).info['shortName']
    if same_plot:
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
    else:
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    ax1.plot(t1['Adj Close'], label=f'{n1}', color='red')
    ax1.set_ylabel(f'{n1} Price')
    ax2.plot(t2['Adj Close'], label=f'{n2}', color='black')
    ax2.set_ylabel(f'{n2} Price')
    plt.xlabel("Date")
    ax1.legend()
    ax2.legend()
    plt.show()


def plot_symbol(symbol, start, end, color='black'):
    ticker = get_data(symbol, start, end)
    name = yf.Ticker(symbol).info['shortName']
    plt.plot(ticker['Adj Close'], color=color)
    plt.xlabel("Date")
    plt.ylabel(f"{name} Price")
    plt.title(f"{name} Over Time")
    plt.show()


# compare_plots('CL=F', '^GSPC', '2000-01-28', '2024-01-26', same_plot=True)
# plot_symbol('AAPL', '2000-01-28', '2024-01-26', 'b')

# print_price("AAPL", 20)

# get_ticker_info("AAPL")
# print(get_data('AAPL', '2000-01-28', '2024-01-26'))
