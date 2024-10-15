# (WIP) Real-Time Stock Price Tracker

Real-Time Stock Price Tracker is a Python-based application that tracks live stock prices using the Yahoo Finance API (yfinance) and visualizes the stock price movement in real-time using matplotlib. 
This project demonstrates real-time data handling, API integration, and live-updating data visualizations. This is in a WIP state, which
demonstrates POC, but more complex iterations are on the way.

### Key Features:
- Fetches live stock prices using the yfinance library.
- Displays a live-updating graph of stock price movements.
- Updates every 5 seconds to reflect the most current stock data.
- Easy-to-run Python script with minimal dependencies.

This project is designed to handle:

- Real-time API integration and data processing.
- Dynamic data visualization using matplotlib.
- Handling live data with Python.

To run this project, you’ll need the following dependencies:

- Python 3.x
- yfinance library for fetching stock prices.
- matplotlib for real-time data visualization.

You can install the required dependencies using pip:
```
pip install yfinance matplotlib
```

#### Getting Started
Clone the repository:
```
git clone https://github.com/yourusername/real-time-stock-tracker.git
cd real-time-stock-tracker
```

Run the tracker:
```
python3 tracker.py
```

Enter a stock symbol (e.g., AAPL for Apple) when prompted:
```
Enter the stock symbol (e.g., AAPL for Apple): AAPL
```

View the live-updating graph of the stock price, which refreshes every 5 seconds.
TODO: Add example screenshot


#### Project Structure
- tracker.py: The main Python script that fetches stock prices and displays the live-updating graph.
- test_tracker.py: Unit tests for the core functionality, ensuring the API integration and graph update logic work as expected.

#### Running the Tests
To run the tests, simply execute the following:
```
python3 -m unittest test_tracker.py
```
The tests currently ensure that:

- Stock prices are fetched correctly from the API.
- The graph updates correctly without errors.
- More to follow, these are in a WIP state

#### Future Enhancements
- Add more detailed stock information, such as volume, moving averages, and historical data.
- Allow users to track multiple stocks simultaneously.
- Implement a more advanced data visualization using plotly for interactive graphs.
