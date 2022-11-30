import requests
import numpy as np

def get_history(crypto, key):
    request_url = f'https://api.basecampcrypto.nl/v1/coin/{crypto}/history?key={key}'
    try:
        r = requests.get(request_url)
    except requests.exceptions.HTTPError as err:
        print(SystemExit(err))
    json_return =  r.json()
    history = json_return['history']
    dt=np.dtype([('day',int),('value', float)]) # datatypes v/d waarden
    values = [tuple(each.values()) for each in history] # shamelessly gepikt van stackoverflow "https://stackoverflow.com/questions/24792690/easiest-way-to-create-a-numpy-record-array-from-a-list-of-dictionaries"
    crypto_history_data = np.array(values, dtype=dt)
    return crypto_history_data


def get_current_value(crypto, key):
    request_url = f'https://api.basecampcrypto.nl/v1/coin/{crypto}?key={key}'

    try:
        r = requests.get(request_url)
    except requests.exceptions.HTTPError as err:
        print(SystemExit(err))
    return r.json()


def get_positions(key):
    request_url = f'https://api.basecampcrypto.nl/v1/positions?key={key}'
    try:
        r = requests.get(request_url)
    except requests.exceptions.HTTPError as err:
        print(SystemExit(err))
    return r.json()


def get_team(key):
    request_url = f'https://api.basecampcrypto.nl/v1/team?key={key}'
        
    try:
        r = requests.get(request_url)
    except requests.exceptions.HTTPError as err:
            print(SystemExit(err))
    return r.json()


def get_orders(key):
    request_url = f'https://api.basecampcrypto.nl/v1/orders?key={key}'
        
    try:
        r = requests.get(request_url)
    except requests.exceptions.HTTPError as err:
            print(SystemExit(err))
    return r.json()  

