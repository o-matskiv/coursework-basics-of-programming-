import matplotlib.pyplot as plt
import numpy as np
import csv
from math import *


def my_plotter(ax, x, y, param_dict):
    """
    Points a dot with coordinates (x, y) on canvas.
    """
    out = ax.plot(x, y, **param_dict)
    return out


def create_dicts(f_name):
    """
    Create dictionaries {Schools_number:Crimes_number} and {Price:Crimes_number}.
    (str) -> dict,dict
    """
    schools_dict = {}
    price_dict = {}
    with open(f_name) as f_obj:
        reader = csv.DictReader(f_obj, delimiter=',')
        for line in reader:
            crimes = int(line['Crimes_number'])
            price = round(int(line['Price']), -5)
            schools = int(line['Schools_number'])
            if schools in schools_dict:
                schools_dict[schools].append(crimes)
            else:
                schools_dict.update({schools: [crimes]})
            if price in price_dict:
                price_dict[price].append(crimes)
            else:
                price_dict.update({price: [crimes]})
    for i in schools_dict:
        schools_dict[i] = sum(schools_dict[i])/len(schools_dict[i])
    for i in price_dict:
        price_dict[i] = max(price_dict[i])
    return schools_dict, price_dict


def main():
    """
    The main function of this modules.
    Draws graphes Crimes number/Schools and Crimes number/Price.
    """
    schools_dict, price_dict = create_dicts('filtred/Wards1.csv')

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_ylabel('Crimes number')
    ax1.set_xlabel('Schools')
    ax2.set_ylabel('Crimes number')
    ax2.set_xlabel('Price')
    for i in schools_dict:
        my_plotter(ax1, i, schools_dict[i], {'marker': 'x'})
    for i in price_dict:
        my_plotter(ax2, i, price_dict[i], {'marker': 'x'})
    plt.show()


if __name__ == '__main__':
    main()
