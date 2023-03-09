import time
from binance.client import Client

# Ключи для доступа к API Binance 
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"

# Создание экземпляра клиента Binance API 
client = Client(API_KEY, API_SECRET)

# Словарь для хранения предыдущих цен 
previous_prices = {}

# Определение метода расчета движения цены 
def calculate_movement(current_price, previous_price):
    movement = ((current_price - previous_price) / previous_price) * 100
    return movement

# Основной цикл программы 
while True:
    try:
        # Получение текущей цены фьючерса ETHUSDT 
        ticker = client.futures_symbol_ticker(symbol="ETHUSDT")

        # Сохранение текущей цены в переменную 
        current_price = float(ticker["price"])

        # Проверка, была ли сохранена предыдущая цена 
        if "ETHUSDT" in previous_prices:
            previous_price = previous_prices["ETHUSDT"]
            # Расчет движения цены за последний час 
            movement = calculate_movement(current_price, previous_price)
            if abs(movement) > 1:
                print("Цена ETHUSDT изменилась на {}% за последний час".format(round(movement, 2)))

        # Сохранение текущей цены в словарь 
        previous_prices["ETHUSDT"] = current_price

        # Задержка выполнения программы на 1 секунду 
        time.sleep(1)
    except Exception as e:
        print(e)
        # Задержка выполнения программы на 10 секунд в случае ошибки 
        time.sleep(10)
