import csv
from adt import *


def opn_csv(f_name, year):
    """
    (str,str) ->list
    Returns list of dicts from csv-file
    """
    ar = Array()
    with open(f_name) as f_obj:
        reader = csv.DictReader(f_obj, delimiter=',')
        for line in reader:
            if year in line['Year'] and line['Measure'] == 'Mean':
                ar.add({'Ward_name': line['Ward_name'], 'Mean Value': line['Value']})
    return ar


def wrte_csv(f_name, ar):
    """
    (str, list) -> None
    Saves information into csv-file
    """
    csv_columns = ['Ward_name', 'Mean Value']
    with open(f_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in ar:
            writer.writerow(data.item)


def main():
    """
    The main function of this module
    """
    year = input()
    lst = opn_csv('land-registry-house-prices-ward.csv', year)
    print(lst)
    wrte_csv('ward-price.csv', lst)


if __name__ == '__main__':
    main()
