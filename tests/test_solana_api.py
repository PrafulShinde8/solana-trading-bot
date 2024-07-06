
import unittest
from unittest.mock import patch
from solana_api import SolanaAPI 

class TestSolanaAPI(unittest.TestCase):
    @patch('solana_api.requests.get')
    def test_get_hero_token_holders(self, mock_get):
        mock_get.return_value.json.return_value = {'data': ['wallet1', 'wallet2']}
        solana_api = SolanaAPI("https://api.solana.com")
        holders = solana_api.get_hero_token_holders()
        self.assertEqual(holders, ['wallet1', 'wallet2'])


if __name__ == '__main__':
    unittest.main()

