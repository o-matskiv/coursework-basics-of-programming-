import csv
from adt import *


def opn_csv(f_name):
    """
    Returns list of dicts from csv-file.
    (str,str) ->list
    """
    ar = Array()
    with open(f_name) as f_obj:
        reader = csv.DictReader(f_obj, delimiter=',')
        for line in reader:
            if '2016' in line['Year'] and line['Measure'] == 'Mean' and line['Value'] != '-':
                ar.add({'Ward_name': line['Ward_name'],
                        'Mean_Value': int(line['Value'].replace(',', ''))})
    return ar


def wrte_csv(f_name, ar):
    """
    Saves information into csv-file
    (str, list) -> None
    """
    csv_columns = ['Ward_name', 'Mean_Value']
    with open(f_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in ar:
            writer.writerow(data.item)


def main():
    """
    The main function of this module
    """
    lst = opn_csv('info/land-registry-house-prices-ward.csv')
    wrte_csv('filtred/ward-price-2016.csv', lst)


if __name__ == '__main__':
    main()
