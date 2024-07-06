import unittest
from unittest.mock import patch
from src.tradingbot import run_trading_bot

class TestTradingBot(unittest.TestCase):
    @patch('src.trading_bot.monitor_wallet_transactions')
    def test_run_trading_bot(self, mock_monitor):
        run_trading_bot()
        mock_monitor.assert_called()

if __name__ == '__main__':
    unittest.main()
