import numpy as np
from get_crypto_data import *
import time
trading = True
key = "Exiq4NbNJg6m9z5N"

#TODO: trading strategies + implementation
#see get_crypto data for function to use here
while trading:
    team = get_team(key)
    positions = get_positions(key)
    amount_positions = len(positions)
    current_details= get_current_value("ALB", key)
    day = current_details['day']
    current_value = current_details['value']
    print(positions)
    res = [d['value'] for d in positions if d['symbol'] == 'ALB']
    if len(positions) > 0:
        print(res[0])
    else:
        print("No current positions")
    if current_value > 1650 and  positions > 0:
        print("bonk")
        crypto_to_sell = 19,5
        sell_crypto_per_coin("ALB", crypto_to_sell, key)
    elif current_value <= 1575 and spending_on: 
        print("Buying 20 coins of Albireo")
        crypto_to_buy = 20
        buy_crypto_per_coin("ALB", crypto_to_buy, key)
    elif team['cash'] < 35000:
        spending_on = False
    else:
        print(day)
        print(team['cash'])
        time.sleep(10)
    