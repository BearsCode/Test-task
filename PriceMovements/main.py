import numpy as np
import pandas as pd
from binance.client import Client

# Ключи для доступа к API Binance 
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"

# Создание экземпляра клиента Binance API 
client = Client(API_KEY, API_SECRET)

# Получение исторических данных цены фьючерсов ETHUSDT и BTCUSDT
ethusdt_klines = client.futures_historical_klines("ETHUSDT", Client.KLINE_INTERVAL_1HOUR, "60 hours ago UTC")
btcusdt_klines = client.futures_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, "60 hours ago UTC")

# Создание pandas DataFrame для цены фьючерсов ETHUSDT и BTCUSDT
ethusdt_df = pd.DataFrame(ethusdt_klines, columns=["timestamp", "open", "high", "low", "close", "volume", "close_time", "quote_asset_volume", "number_of_trades", "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"])
ethusdt_df["timestamp"] = pd.to_datetime(ethusdt_df["timestamp"], unit="ms")
ethusdt_df.set_index("timestamp", inplace=True)
ethusdt_df["close"] = ethusdt_df["close"].astype(float)

btcusdt_df = pd.DataFrame(btcusdt_klines, columns=["timestamp", "open", "high", "low", "close", "volume", "close_time", "quote_asset_volume", "number_of_trades", "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"])
