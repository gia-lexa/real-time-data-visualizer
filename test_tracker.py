import unittest
from unittest.mock import patch, MagicMock
import yfinance as yf
from tracker import get_stock_price, update_graph

class TestTracker(unittest.TestCase):

    @patch('yfinance.Ticker')  # mock yfinance Ticker class
    def test_get_stock_price(self, mock_ticker):
        # set up mock response
        mock_history = MagicMock()
        mock_history.history.return_value = {'Close': [150.0]}  # simulate closing price of 150
        mock_ticker.return_value = mock_history
        
        price = get_stock_price('AAPL')
        
        mock_ticker.assert_called_with('AAPL')  # confirm right stock symbol was used
        self.assertEqual(price, 150.0)          # confirm returned price is correct

    @patch('tracker.get_stock_price')  # mock get_stock_price in tracker.py
    def test_update_graph(self, mock_get_stock_price):
        mock_get_stock_price.return_value = 150.0  # simulate a price of 150
        
        prices = []
        times = []

        # simulate updating graph
        try:
            update_graph(0, 'AAPL')
        except Exception as e:
            self.fail(f'update_graph raised an exception: {e}')
            
        # without being able to test the graphical output easily, 
        # this tests that no exception occurs - obvs would be different if 
        # this was production code

if __name__ == "__main__":
    unittest.main()
