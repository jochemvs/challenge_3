import numpy as np
from get_crypto_data import *

key = "github's not getting this"
days = get_history("ALB", key)['day']
albireo = get_history("ALB", key)['value']
bharani = get_history("BHA", key)['value']
castula = get_history("CAS", key)['value']
dubhe = get_history("DUB", key)['value']    
elgafar = get_history("ELG", key)['value']
fawaris = get_history("FAW", key)['value']
xuange = get_history("XUA", key)['value']

#TODO: trading strategies + implementation
#see get_crypto data for function to use here
