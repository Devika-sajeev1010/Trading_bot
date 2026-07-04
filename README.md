# Simplified Binance Futures Trading Bot

This is a clean, modular Python-based CLI tool designed to connect with the Binance Futures Testnet (USDT-M). I built it to handle order creation securely, validate input arguments locally to prevent broken network calls, and log every server response cleanly into a tracking file.



# How the Project is Structured

To keep the application highly maintainable, the codebase follows a strict separation of concerns, dividing tasks across dedicated files rather than using a single massive script:

### Entry Point
*   **`cli.py`**
    The core interface of the application. It handles parsing command-line arguments. If a user runs the script without any parameters, it automatically boots up an interactive wizard menu to guide them step-by-step.

### The Bot Package (`bot/`)
*   **`bot/client.py`**
    Manages authentication and connectivity. It securely pulls your API keys from a hidden local `.env` file and initializes the network instance explicitly configured for the Binance sandbox environment (`testnet=True`).

*   **`bot/validators.py`**
    The local data validation layer. It checks that target trading pairs, positioning directions (BUY/SELL), and numerical values (quantity/price) conform to standard rules *before* a network request is ever dispatched.

*   **`bot/orders.py`**
    The order execution engine. It structures the verified data parameters into an API payload, transmits the request to the live USDT-M Futures testnet endpoint, and safely catches any real-time server responses or exceptions.

*   **`bot/logging_config.py`**
    The central monitoring engine. It configures the logging system to stream human-readable execution snapshots directly onto your terminal screen while simultaneously writing permanent, timestamped trace receipts into your tracking file.

---

#  Setup & Installation

# 1. Configure the Keys
Clone the project and create a `.env` file in the root directory to store your Testnet keys securely:
```text
BINANCE_API_KEY=your_binance_testnet_api_key
BINANCE_API_SECRET=your_binance_testnet_secret_key
