import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime

# instantiate vars to store stock data and times
prices = []
times = []

# fetch the latest stock price
def get_stock_price(stock_symbol):
  stock = yf.Ticker(stock_symbol)
  todays_data = stock.history(period='1d')
  return todays_data['Close'][0]

# update the graph
def update_graph(i, stock_symbol):
  current_price = get_stock_price(stock_symbol)
  prices.append(current_price)
  times.append(datetime.datetime.now())

  # cap number of points surfaced on graph
  if len(prices) > 50:
    prices.pop(0)
    times.pop(0)

  plt.cla() # clear current axes
  plt.plot(times, prices, label=f'Stock Price: {stock_symbol}', color='blue') ')

  # format graph
  plt.gcf().autofmt_xdate
  plt.xlable('Time')
  plt.ylabel('Price (USD)')
  plt.title(f'Real-Time Stock Price of {stock_symbol}')
  plt.legend(loc='upper left')
  plt.tight_layout()


# intialize the graph
def start_real_time_tracking(stock_symbol):
  global times, prices 
  times = []
  prices = []
  fig = plt.figure(figsize=(10, 5))

  ani = FuncAnimation(fig, update_graph, fargs=(stock_symbol,), interval=5000)
  plt.show()

# run the tracker
if __name__ == "__main__":
  stock_symbol = input("Enter the stock symbol (eg AAPL for Apple):  ")
  start_real_time_tracking(stock_symbol)