import os
import sys
import argparse
from dotenv import load_dotenv
from bot.logging_config import setup_logging
from bot.client import BinanceFuturesClient
from bot.validators import validate_inputs
from bot.orders import place_futures_order

load_dotenv()

def run_interactive_menu():
    """Launches an interactive console walkthrough interface for enhanced UX."""
    print("=" * 50)
    print("       BINANCE FUTURES INTERACTIVE TERMINAL")
    print("=" * 50)
    
    
    print("\n[Step 1/5] Select Trading Pair Asset:")
    print("1. BTCUSDT (Bitcoin)")
    print("2. XRPUSDT (Ripple)")
    print("3. Custom Symbol")
    choice = input("Enter choice (1-3): ").strip()
    if choice == '1': symbol = "BTCUSDT"
    elif choice == '2': symbol = "XRPUSDT"
    else: symbol = input("Enter custom asset pair (e.g., ETHUSDT): ").strip().upper()

    
    print("\n[Step 2/5] Select Market Positioning Side:")
    print("1. BUY (Long Position)")
    print("2. SELL (Short Position)")
    side_choice = input("Enter choice (1-2): ").strip()
    side = "BUY" if side_choice == '1' else "SELL"

    
    print("\n[Step 3/5] Select Order Type:")
    print("1. MARKET Order")
    print("2. LIMIT Order")
    type_choice = input("Enter choice (1-2): ").strip()
    order_type = "MARKET" if type_choice == '1' else "LIMIT"

    
    print("\n[Step 4/5] Configure Trade Asset Constraints:")
    try:
        quantity = float(input(f"Enter target quantity execution volume for {symbol}: ").strip())
    except ValueError:
        print("\n[!] Input Validation Error: Quantity volume must be an active numeric decimal.")
        return None

    price = None
    if order_type == "LIMIT":
        try:
            price = float(input("Enter targeted LIMIT execution strike price (USDT): ").strip())
        except ValueError:
            print("\n[!] Input Validation Error: Price value must be an active numeric decimal.")
            return None

    print("\n" + "-" * 50)
    print(f"Executing: {side} {order_type} | {quantity} {symbol}" + (f" @ ${price}" if price else ""))
    print("-" * 50)
    
    return argparse.Namespace(symbol=symbol, side=side, type=order_type, quantity=quantity, price=price)


def main():
    logger = setup_logging()
    if len(sys.argv) == 1:
        args = run_interactive_menu()
        if not args:
            return
    else:
        parser = argparse.ArgumentParser(description="Modular Binance Futures Testnet Trading Bot")
        parser.add_argument("--symbol", type=str, required=True, help="Pair Symbol (e.g., BTCUSDT)")
        parser.add_argument("--side", type=str, required=True, choices=["BUY", "SELL", "buy", "sell"])
        parser.add_argument("--type", type=str, required=True, choices=["MARKET", "LIMIT", "market", "limit"])
        parser.add_argument("--quantity", type=float, required=True)
        parser.add_argument("--price", type=float, default=None)
        args = parser.parse_args()
    
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    try:
        validate_inputs(args.symbol, args.side, args.type, args.quantity, args.price)
        bot_client = BinanceFuturesClient(api_key, api_secret)
        
        place_futures_order(
            client_wrapper=bot_client,
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )
    except Exception as e:
        logger.error(f"Process pipeline failed: {str(e)}")

if __name__ == "__main__":
    main()