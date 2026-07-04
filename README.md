Simplified Binance Futures Trading Bot
This is a clean, modular Python-based command-line interface (CLI) tool designed to connect securely with the Binance Futures Testnet (USDT-M). I built it to handle order creation smoothly, validate all input arguments locally to prevent broken or unnecessary network calls, and log every server response cleanly into a permanent tracking file.

How the Project is Structured
To keep the application highly maintainable, the codebase follows a strict separation of concerns, dividing tasks across dedicated files rather than using a single massive script:

Entry Point
cli.py
The core interface of the application. It handles parsing command-line arguments. If a user runs the script without any parameters, it automatically boots up an interactive wizard menu to guide them step-by-step.

The Bot Package (bot/)
bot/client.py
Manages authentication and connectivity. It securely pulls your API keys from a hidden local .env file and initializes the network instance explicitly configured for the Binance sandbox environment (testnet=True).

bot/validators.py
The local data validation layer. It checks that target trading pairs, positioning directions (BUY/SELL), and numerical values (quantity/price) conform to standard rules before a network request is ever dispatched.

bot/orders.py
The order execution engine. It structures the verified data parameters into an API payload, transmits the request to the live USDT-M Futures testnet endpoint, and safely catches any real-time server responses or exceptions.

bot/logging_config.py
The central monitoring engine. It configures the logging system to stream human-readable execution snapshots directly onto your terminal screen while simultaneously writing permanent, timestamped trace receipts into your tracking file.

Setup & Installation Steps
Follow these steps to configure the application environment and isolate dependencies locally:

1. Configure Environment Credentials
Create a hidden configuration file named .env in the root folder of the project to securely house your active API credentials:

BINANCE_API_KEY=your_binance_testnet_api_key
BINANCE_API_SECRET=your_binance_testnet_secret_key

2. Initialize and Activate Virtual Environment
Set up an isolated environment to manage execution dependencies without cluttering global system packages:

python -m venv venv
venv\Scripts\activate

3. Install Required Dependencies
Use Python's package manager to sync down the precise third-party connectivity hooks:

pip install -r requirements.txt

How to Run (Execution Examples)
The system supports two distinct runtime modes to facilitate testing:

Mode 1: The Interactive Menu Wizard (Enhanced UX Bonus)
If you execute the script directly without attaching trailing configuration flags, the system automatically launches an interactive, step-by-step terminal wizard:

python cli.py

Simply type the corresponding number selection or value and press Enter when prompted.

Mode 2: Direct Command Line Interface (CLI) Flags
For automated or programmatic script executions, pass explicit runtime arguments directly:

Execute a MARKET Buy Order:
python cli.py --symbol XRPUSDT --side BUY --type MARKET --quantity 15

Execute a LIMIT Buy Order:
python cli.py --symbol XRPUSDT --side BUY --type LIMIT --quantity 15 --price 2.0

Execute a MARKET Short (SELL) Order:
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.01

Technical & System Assumptions
During the architectural design and structural implementation of this project, the following core assumptions were made:

Isolated Testing Scope (testnet=True): It is assumed that this application is strictly running inside a development sandbox. The client network layer explicitly routes all payloads to the Binance Futures Testnet (USDT-M) matching engines to safeguard against accidental live capital deployment.

External Credential Storage: The application assumes the presence of a valid .env configuration template file at runtime. It relies entirely on the local system reading these strings into memory rather than hardcoding credentials into source components.

Pre-Validated Server Rules: Local parameters filtering acts as a structural sanity check (ensuring numeric validation, side match syntax, etc.). However, the bot assumes that downstream financial thresholds (such as minimum $5 USDT trade values or available wallet margin accounts) are dynamically validated and governed by the live Binance API response payload.

Error Handling & Live Testing Traces
The system handles connectivity issues and exchange-specific rule variations gracefully. Because the Binance Testnet engine enforces strict capital and sizing rules, the bot cleanly intercepts structural API responses.

The application catches raw exceptions, writes them cleanly, and avoids system crashes. The presence of actual financial rejections from the exchange proves that the pipeline successfully contacts live matching systems, securely checks balance books, and parses real-time text structures.

Here is an explicit snapshot snippet extracted directly from the system's trading.log tracking output:

2026-07-04 00:03:20,499 - INFO - Binance Futures Testnet client session established.
2026-07-04 00:03:20,500 - INFO - [ORDER SUMMARY] Attempting BUY LIMIT | 10.0 XRPUSDT
2026-07-04 00:03:21,227 - ERROR - Process pipeline failed: APIError(code=-4164): Order's notional must be no smaller than 5 (unless you choose reduce only).
2026-07-04 11:46:39,281 - INFO - Binance Futures Testnet client session established.
2026-07-04 11:46:39,284 - INFO - [ORDER SUMMARY] Attempting SELL MARKET | 15.0 XRPUSDT
2026-07-04 11:46:40,163 - INFO - [RESPONSE SUCCESS] OrderID: 2312415558 | Status: NEW
2026-07-04 00:03:20,499 - INFO - Binance Futures Testnet client session established.
2026-07-04 00:03:20,500 - INFO - [ORDER SUMMARY] Attempting BUY LIMIT | 10.0 XRPUSDT
2026-07-04 00:03:21,227 - ERROR - Process pipeline failed: APIError(code=-4164): Order's notional must be no smaller than 5 (unless you choose reduce only).
