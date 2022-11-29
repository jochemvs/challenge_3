import csv
import numpy as np
from prettytable import PrettyTable

with open('crypto_daily_prices_365.csv', 'r', encoding='utf8') as data:
    crypto_data = np.genfromtxt('crypto_daily_prices_365.csv', delimiter=';', names=True)
    days = crypto_data["0"]
    albireo = crypto_data["Albireo"]
    bharani = crypto_data["Bharani"]
    castula = crypto_data["Castula"]
    dubhe = crypto_data["Dubhe"]    
    elgafar = crypto_data["Elgafar"]
    fawaris = crypto_data["Fawaris"]
    table = PrettyTable()
    table.field_names = ["Name","AVG", "MIN", "MAX", "SD", "Q1", "Q2", "Q3", "RNG", "IQR"]
    table.add_row(["Albireo", np.average(albireo), np.min(albireo), np.max(albireo), np.std(albireo), np.percentile(albireo, 25), np.percentile(albireo, 50), np.percentile(albireo, 75), np.ptp(albireo), np.subtract(*np.percentile(albireo, [75, 25]))])
    table.add_row(["Bharani", np.average(bharani), np.min(bharani), np.max(bharani), np.std(bharani), np.percentile(bharani, 25), np.percentile(bharani, 50), np.percentile(bharani, 75), np.ptp(bharani), np.subtract(*np.percentile(bharani, [75, 25]))])
    table.add_row(["Castula", np.average(castula), np.min(castula), np.max(castula), np.std(castula), np.percentile(castula, 25), np.percentile(castula, 50), np.percentile(castula, 75), np.ptp(castula), np.subtract(*np.percentile(castula, [75, 25]))])
    table.add_row(["Dubhe", np.average(dubhe), np.min(dubhe), np.max(dubhe), np.std(dubhe), np.percentile(dubhe, 25), np.percentile(dubhe, 50), np.percentile(dubhe, 75), np.ptp(dubhe), np.subtract(*np.percentile(dubhe, [75, 25]))])
    table.add_row(["Elgafar", np.average(elgafar), np.min(elgafar), np.max(elgafar), np.std(elgafar), np.percentile(elgafar, 25), np.percentile(elgafar, 50), np.percentile(elgafar, 75), np.ptp(elgafar), np.subtract(*np.percentile(elgafar, [75, 25]))])
    table.add_row(["Fawaris", np.average(fawaris), np.min(fawaris), np.max(fawaris), np.std(fawaris), np.percentile(fawaris, 25), np.percentile(fawaris, 50), np.percentile(fawaris, 75), np.ptp(fawaris), np.subtract(*np.percentile(fawaris, [75, 25]))])
    print(table)