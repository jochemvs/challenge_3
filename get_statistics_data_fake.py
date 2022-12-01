import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from get_crypto_data import get_history

key = "github's not getting this"
days_xuange = get_history("XUA", key)['day']
days_yildum = get_history("YIL", key)['day']
days_zosma = get_history("ZOS", key)['day']
xuange = get_history("XUA", key)['value']
yildum = get_history("YIL", key)['value']
zosma = get_history("ZOS", key)['value']
print(len(zosma))
print(len(xuange))
print(len(yildum))

def ups_downs(crypto):
    lup = 0
    ldown = 0
    temp_lup = 0
    temp_ldown =  0
    up_days = 0
    down_days = 0
    current_value = ''
    prev_value = ''

    for i in range(len(crypto)):
        if i == 0:
            current_value = crypto[i]
            prev_value = 0
        elif i > 0:
            prev_value = crypto[i-1]
            current_value = crypto[i]
            if prev_value > current_value:
                down_days +=1
            elif prev_value < current_value:
                up_days +=1
    return [up_days, down_days]

table = PrettyTable()
table.field_names = ["Name","AVG", "MIN", "MAX", "SD", "Q1", "Q2", "Q3", "RNG", "IQR", "UPS", "DOWNS"]
table.add_row(["Xuange", np.average(xuange), np.min(xuange), np.max(xuange), np.std(xuange), np.percentile(xuange, 25), np.percentile(xuange, 50), np.percentile(xuange, 75), np.ptp(xuange), np.subtract(*np.percentile(xuange, [75, 25])), ups_downs(xuange)[0], ups_downs(xuange)[1]])
table.add_row(["Yildum", np.average(yildum), np.min(yildum), np.max(yildum), np.std(yildum), np.percentile(yildum, 25), np.percentile(yildum, 50), np.percentile(yildum, 75), np.ptp(yildum), np.subtract(*np.percentile(yildum, [75, 25])), ups_downs(yildum)[0], ups_downs(yildum)[1]])
table.add_row(["Zosma", np.average(zosma), np.min(zosma), np.max(zosma), np.std(zosma), np.percentile(zosma, 25), np.percentile(zosma, 50), np.percentile(zosma, 75), np.ptp(zosma), np.subtract(*np.percentile(zosma, [75, 25])), ups_downs(zosma)[0], ups_downs(zosma)[1]])
print(table)


plt.rcParams["figure.autolayout"] = True
fig, axs = plt.subplots(sharey=False)
plt.title("Line graph of multuple currencies")
plt.xlabel("Day")
plt.ylabel("Price (euro)")
axs.plot(days_xuange, xuange, color='red', label="Xuange")
axs.plot(days_yildum, yildum, color='purple', label="Yildum")
axs.plot(days_zosma, zosma, color="green", label="Zosma")
axs.legend()
fig.tight_layout()
plt.show()