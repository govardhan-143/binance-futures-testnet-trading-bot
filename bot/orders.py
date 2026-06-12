from binance.enums import (
    FUTURE_ORDER_TYPE_MARKET,
    FUTURE_ORDER_TYPE_LIMIT
)

from bot.client import BinanceClient
from bot.logging_config import logger


class OrderService:

    def __init__(self):
        self.client = BinanceClient()

    def place_market_order(
        self,
        symbol,
        side,
        quantity
    ):

        logger.info(
            f"MARKET ORDER | Symbol={symbol} Side={side} Quantity={quantity}"
        )

        response = self.client.create_order(
            symbol=symbol,
            side=side,
            order_type=FUTURE_ORDER_TYPE_MARKET,
            quantity=quantity
        )

        logger.info(f"Response: {response}")

        return response

    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):

        logger.info(
            f"LIMIT ORDER | Symbol={symbol} Side={side} Quantity={quantity} Price={price}"
        )

        response = self.client.create_order(
            symbol=symbol,
            side=side,
            order_type=FUTURE_ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            time_in_force="GTC"
        )

        logger.info(f"Response: {response}")

        return response