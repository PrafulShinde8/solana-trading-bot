
import json
from solana_api import SolanaAPI
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.account import Account
from solana.system_program import TransferParams, transfer

class SolanaAPI:
    def __init__(self, endpoint="https://api.mainnet-beta.solana.com"):
        self.client = Client(endpoint)
        self.load_secrets()

    def load_secrets(self):

        with open('config/secrets.json') as f:
            secrets = json.load(f)
            self.private_key = secrets["private_key"]
            self.public_key = secrets["public_key"]

    def buy_token(self, recipient, amount):
        sender = Account(self.private_key)
        params = TransferParams(
            from_pubkey=sender.public_key(),
            to_pubkey=recipient,
            lamports=amount
        )
        tx = Transaction().add(transfer(params))
        result = self.client.send_transaction(tx, sender)
        return result

    def sell_token(self, recipient, amount):

        return self.buy_token(recipient, amount)

    def get_wallet_transactions(self, wallet_address):
        result = self.client.get_confirmed_signature_for_address2(wallet_address)
        return result

    def get_wallet_balance(self, wallet_address):
        result = self.client.get_balance(wallet_address)
        return result


if __name__ == "__main__":
    api = SolanaAPI()
    print(api.get_wallet_balance(api.public_key))
