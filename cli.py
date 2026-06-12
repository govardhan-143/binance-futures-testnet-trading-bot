import argparse

from bot.orders import OrderService
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


def display_response(response):

    print("\nOrder Response")
    print("-" * 40)

    print(f"Order ID    : {response.get('orderId')}")
    print(f"Status      : {response.get('status')}")
    print(f"ExecutedQty : {response.get('executedQty')}")

    if response.get("avgPrice"):
        print(f"Avg Price   : {response.get('avgPrice')}")


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol (e.g. BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        help="BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        help="MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        help="Required for LIMIT orders"
    )

    args = parser.parse_args()

    try:

        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        print("\nOrder Request")
        print("-" * 40)
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")

        order_service = OrderService()

        if order_type == "MARKET":

            response = order_service.place_market_order(
                symbol,
                side,
                quantity
            )

        else:

            if not args.price:
                raise ValueError(
                    "Price is required for LIMIT order"
                )

            price = validate_price(args.price)

            response = order_service.place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        display_response(response)

        print("\nOrder placed successfully.")

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()