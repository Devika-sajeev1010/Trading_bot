import logging
from binance.exceptions import BinanceAPIException, BinanceRequestException

logger = logging.getLogger("trading_bot")

def place_futures_order(client_wrapper, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    client = client_wrapper.client
    
    params = {
        'symbol': symbol.upper(),
        'side': side.upper(),
        'type': order_type.upper(),
        'quantity': quantity
    }
    
    if order_type.upper() == 'LIMIT':
        params['price'] = str(price)
        params['timeInForce'] = 'GTC'
        
    logger.info(f"[ORDER SUMMARY] Attempting {side.upper()} {order_type.upper()} | {quantity} {symbol.upper()}")
    
    try:
        response = client.futures_create_order(**params)
        
        logger.info(f"[RESPONSE SUCCESS] OrderID: {response.get('orderId')} | Status: {response.get('status')}")
        print("\n✅ SUCCESS: Order placed successfully on Binance Futures Testnet.")
        return response
        
    except BinanceAPIException as api_err:
        logger.error(f"❌ API Error: Code {api_err.status_code} - {api_err.message}")
        print(f"\n❌ API ERROR: {api_err.message}")
        raise api_err
    except BinanceRequestException as req_err:
        logger.error(f"❌ Connection Error: {str(req_err)}")
        print("\n❌ NETWORK ERROR: Problem reaching Binance Testnet.")
        raise req_err
    except Exception as general_err:
        logger.error(f"❌ Unexpected Event: {str(general_err)}")
        print(f"\n❌ UNEXPECTED ERROR: {str(general_err)}")
        raise general_err