import os

from dotenv import load_dotenv
from binance.client import Client

load_dotenv()


class BinanceClient:

    def __init__(self):

        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        self.client = Client(
            api_key,
            api_secret,
            testnet=True
        )

    def create_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None,
        time_in_force=None
    ):

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if price is not None:
            params["price"] = price

        if time_in_force:
            params["timeInForce"] = time_in_force

        return self.client.futures_create_order(**params)