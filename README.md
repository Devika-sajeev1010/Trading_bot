# Simplified Binance Futures Trading Bot

This is a clean, modular Python-based CLI tool designed to connect with the Binance Futures Testnet (USDT-M). I built it to handle order creation securely, validate input arguments locally to prevent broken network calls, and log every server response cleanly into a tracking file.



# How the Project is Structured

To keep the code clean and easy to maintain, I broke the logic down into distinct modules rather than piling everything into one massive script:

**`cli.py`**: The main entry point. It parses arguments from the command line, and if no arguments are provided, it automatically launches an interactive wizard menu to guide the user step-by-step.
**`bot/client.py`**: Handles authentication. It pulls the API credentials safely from a hidden `.env` file and initializes the connection explicitly targeting the Binance sandbox environment (`testnet=True`).
**`bot/validators.py`**: The local gatekeeper. It checks that the user has provided valid symbols, correct positioning sides (BUY/SELL), and that numbers like quantity and price actually make sense before sending requests over the internet.
**`bot/orders.py`**: The execution layer. This formats the parameters into a payload, calls the specific USDT-M Futures endpoint, and catches any real-time API exceptions returned by the exchange.
**`bot/logging_config.py`**: Manages tracking. It streams human-readable status updates to the terminal screen while writing complete, timestamped JSON/text logs to an external file.

---

#  Setup & Installation

# 1. Configure the Keys
Clone the project and create a `.env` file in the root directory to store your Testnet keys securely:
```text
BINANCE_API_KEY=your_binance_testnet_api_key
BINANCE_API_SECRET=your_binance_testnet_secret_key
