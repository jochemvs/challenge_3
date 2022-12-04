from get_crypto_data import get_history
import numpy as np
import matplotlib.pyplot as plt
from get_crypto_data import get_history

key = "Exiq4NbNJg6m9z5N"
days = get_history("ALB", key)['day']
albireo = get_history("ALB", key)['value']
bharani = get_history("BHA", key)['value']
castula = get_history("CAS", key)['value']
dubhe = get_history("DUB", key)['value']    
elgafar = get_history("ELG", key)['value']
fawaris = get_history("FAW", key)['value']
boxplots_created = 0

def generate_boxplot(crypto, crypto_name):
    fig1 = plt.figure()

    fig1.suptitle(f'Boxplot for {crypto_name}', fontsize=14, fontweight='bold')
    axs = fig1.subplots()

    axs.boxplot(crypto)

    axs.set_title('Price spread')
    axs.set_ylabel('Price')
    plt.savefig(f'{crypto_name}_boxplot.png')
    plt.show()

def generate_histogram(crypto, crypto_name):
    fig1 = plt.figure()

    fig1.suptitle(f'Histogram for {crypto_name}', fontsize=14, fontweight='bold')
    axs = fig1.subplots()

    axs.hist(crypto)

    axs.set_title('Frequency of a certain price')
    axs.set_xlabel('Price')
    axs.set_ylabel('Frequency')
    plt.savefig(f'{crypto_name}_histogram.png')
    plt.show()

generate_boxplot(albireo, "Albireo")
generate_boxplot(bharani, "Bharani")
generate_boxplot(castula, "Castula")
generate_boxplot(dubhe, "Dubhe")
generate_boxplot(elgafar, "Elgafar")
generate_boxplot(fawaris, "Fawaris")

generate_histogram(albireo, "Albireo")
generate_histogram(bharani, "Bharani")
generate_histogram(castula, "Castula")
generate_histogram(dubhe, "Dubhe")
generate_histogram(elgafar, "Elgafar")
generate_histogram(fawaris, "Fawaris")




