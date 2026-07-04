from binance.client import Client
import logging

logger = logging.getLogger("trading_bot")

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        if not api_key or not api_secret:
            logger.error("API Key or Secret missing in .env configuration file.")
            raise ValueError("API Key and Secret Key are required.")
        try:
            
            self.client = Client(api_key, api_secret, testnet=True)
            logger.info("Binance Futures Testnet client session established.")
        except Exception as e:
            logger.error(f"Failed to initialize Binance Client: {str(e)}")
            raise e