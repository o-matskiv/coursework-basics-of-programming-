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
            ar.add({'Ward_name': line['WARD_NAME'], 'School_name': line['SCHOOL_NAM']})
    return ar


def wrte_csv(f_name, ar):
    """
    Saves information into csv-file.
    (str, list) -> None
    """
    csv_columns = ['Ward_name', 'School_name']
    with open(f_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in ar:
            writer.writerow(data.item)


def main():
    """
    The main function of this module
    """
    arr = opn_csv('info/all_schools_2016.csv')
    wrte_csv('filtred/all_schools_2016.csv', arr)


if __name__ == '__main__':
    main()
