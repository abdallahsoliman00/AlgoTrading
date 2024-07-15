import yfinance as yf
# import pandas as pd
import matplotlib.pyplot as plt


def get_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data


def calculate_moving_average(data, window_size):
    return data['Open'].rolling(window=window_size).mean()


def plot_stock_data(stock_data, moving_average1, moving_average2, symbol):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(moving_average1, color='#FFA500')
    ax1.set_ylabel('Price')
    ax2.plot(moving_average2, color='k')
    plt.xlabel("Date")
    ax1.legend()
    ax2.legend()
    # plt.show()

    # plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label=f'{symbol} Close Price')
    # plt.plot(moving_average, label=f'{symbol} Moving Average')
    plt.title(f'{symbol} Stock Price and Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()


def main():
    # Input parameters
    # symbol = input("Enter ticker symbol (e.g., AAPL): ")
    # start_date = input("Enter start date (YYYY-MM-DD): ")
    # end_date = input("Enter end date (YYYY-MM-DD): ")
    # window_size1 = int(input("Enter moving average 1 window size: "))
    # window_size2 = int(input("Enter moving average 2 window size: "))
    symbol = 'AAPL'
    start_date = '2003-01-01'
    end_date = '2024-03-15'
    window_size1 = 14
    window_size2 = 50

    # Fetch stock data
    stock_data = get_stock_data(symbol, start_date, end_date)

    # Calculate moving average
    moving_average1 = calculate_moving_average(stock_data, window_size1)
    moving_average2 = calculate_moving_average(stock_data, window_size2)

    # Plot stock data and moving average
    plot_stock_data(stock_data, moving_average1, moving_average2, symbol)


main()
