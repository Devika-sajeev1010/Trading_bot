# Simplified Binance Futures Trading Bot

This is a modular Python command-line utility engineered to connect securely with the Binance Futures Testnet (USDT-M) API engine. The application implements local data constraint processing, environment-driven security authentication, structured trace logging, and an interactive operational configuration menu.

---

## How the Project is Structured

To keep the application highly maintainable, the codebase follows a strict separation of concerns, dividing tasks across dedicated files rather than using a single massive script:

### Entry Point
*   **`cli.py`**  
    The primary interface gateway. It interprets trailing runtime command flags. If no configuration arguments are provided at execution, it automatically launches an interactive walkthrough wizard menu to guide the user step-by-step.

### The Bot Package (`bot/`)
*   **`bot/client.py`**  
    Manages API connectivity and credentials isolation. It extracts configuration profiles securely from a local hidden environment environment and safely initialises the client instance target configuration explicitly geared towards the sandbox networks (`testnet=True`).

*   **`bot/validators.py`**  
    The local data validation layer. It checks that target trading pairs, positioning directions (BUY/SELL), and numerical values (quantity/price) conform to standard validation profiles *before* an expensive network round-trip request is ever dispatched.

*   **`bot/orders.py`**  
    The core order execution engine. It structures the verified parameters into proper transaction API payloads, routes them directly to the matching engine endpoints, and intercepts real-time exchange error structures gracefully.

*   **`bot/logging_config.py`**  
    The central monitoring engine. It handles formatting runtime traces, pushing real-time operations text onto the terminal panel while tracking timestamped records to an external tracing output file.

---

## Setup & Installation Steps

Follow these steps to configure the application environment and isolate dependencies locally:

### 1. Configure Environment Credentials
Create a hidden configuration file named `.env` in the root folder of the project to securely house your active API credentials:
BINANCE_API_KEY=your_binance_testnet_api_key
BINANCE_API_SECRET=your_binance_testnet_secret_key

### 2. Initialize and Activate Virtual Environment
Set up an isolated environment to manage execution dependencies without cluttering global system packages:
# Create the environment
python -m venv venv

# Activate the environment
venv\Scripts\activate

### 3. Install Required Dependencies
Use Python's package manager to sync down the precise third-party connectivity hooks:
pip install -r requirements.txt

### How to Run (Execution Examples)
The system supports two distinct runtime modes to facilitate testing:

# Mode 1: The Interactive Menu Wizard (Enhanced UX Bonus)
If you execute the script directly without attaching trailing configuration flags, the system automatically launches an interactive, step-by-step terminal wizard:
python cli.py

# Mode 2: Direct Command Line Interface (CLI) Flags
For automated or programmatic script executions, pass explicit runtime arguments directly:
# 1. Execute a MARKET Buy Order
python cli.py --symbol XRPUSDT --side BUY --type MARKET --quantity 15

# 2. Execute a LIMIT Buy Order
python cli.py --symbol XRPUSDT --side BUY --type LIMIT --quantity 15 --price 2.0

# 3. Execute a MARKET Short (SELL) Order
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.01

### Technical & System Assumptions
During the architectural design and structural implementation of this project, the following core assumptions were made:

Isolated Testing Scope (testnet=True): It is assumed that this application is strictly running inside a development sandbox. The client network layer explicitly routes all payloads to the Binance Futures Testnet (USDT-M) matching engines to safeguard against accidental live capital deployment.

External Credential Storage: The application assumes the presence of a valid .env configuration template file at runtime. It relies entirely on the local system reading these strings into memory rather than hardcoding credentials into source components.

Pre-Validated Server Rules: Local parameters filtering acts as a structural sanity check (ensuring numeric validation, side match syntax, etc.). However, the bot assumes that downstream financial thresholds (such as minimum $5 USDT trade values or available wallet margin accounts) are dynamically validated and governed by the live Binance API response payload.

### Error Handling & Live Testing Traces
Here is an explicit snapshot snippet extracted directly from the system's trading.log tracking output:
2026-07-03 23:58:25,586 - INFO - Binance Futures Testnet client session established.
2026-07-03 23:58:25,587 - INFO - [ORDER SUMMARY] Attempting BUY MARKET | 0.01 BTCUSDT
2026-07-03 23:58:26,678 - ERROR - Process pipeline failed: APIError(code=-2019): Margin is insufficient.
2026-07-04 11:46:39,281 - INFO - Binance Futures Testnet client session established.
2026-07-04 11:46:39,284 - INFO - [ORDER SUMMARY] Attempting SELL MARKET | 15.0 XRPUSDT
2026-07-04 11:46:40,163 - INFO - [RESPONSE SUCCESS] OrderID: 2312415558 | Status: NEW


