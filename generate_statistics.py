import csv

with open('crypto_daily_prices_365.csv', 'r', encoding='utf8') as data:
    crypto_data = csv.DictReader(data)
    print(crypto_data)