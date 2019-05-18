from Ward import *
from adt import *
from police_api import PoliceAPI
from police_api.forces import Force
from police_api.neighbourhoods import Neighbourhood

import csv


def create_price(f_name, Ward_array):
    """
    Creates Ward oblects and adds prices.
    (Array) -> None
    """
    with open(f_name) as f_obj:
        reader = csv.DictReader(f_obj, delimiter=',')
        for line in reader:
            wrd = Ward(line['Ward_name'])
            wrd.set_price(line['Mean_Value'])
            Ward_array.add(wrd)


def create_schools(f_name, Ward_array):
    """
    Adds schools to Ward objects.
    (Array) -> None
    """
    with open(f_name) as f_obj:
        reader = csv.DictReader(f_obj, delimiter=',')
        for line in reader:
            if Ward(line['Ward_name']) in Ward_array:
                wrd = Ward_array.get_element(Ward(line['Ward_name']))
                wrd.add_school(line['School_name'])


def filter_crimes(Ward_array):
    """
    Creates an Array of Neighbourhood objects.
    (Array) -> Array
    """
    api = PoliceAPI()
    neighbourhoods = Array()
    for force in api.get_forces():
        for neighbourhood in force.neighbourhoods:
            if Ward(neighbourhood.name) in Ward_array:
                neighbourhoods.add(neighbourhood)
    return neighbourhoods


def wrte_csv(f_name, element, i):
    """
    Saves information into csv-file.
    (str, dict, int) -> None
    """
    csv_columns = ['Ward_name', 'Price', 'Schools_number', 'Crimes_number']
    with open(f_name, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        if i == 0:
            writer.writeheader()
        writer.writerow(element)


def create_crimes(f_name, neighbourhoods, Ward_array):
    """
    Adds crimes to Ward objects.
    (str,Array,Array) -> None
    """
    api = PoliceAPI()
    i = 0
    csv_arr = Array()
    for neighbourhood in neighbourhoods:
        try:
            wrd = Ward_array.get_element(Ward(neighbourhood.item.name))
            mounthes = [str(i) for i in range(1, 13)]
            for m in mounthes:
                crimes = api.get_crimes_area(neighbourhood.item.boundary, date='2018-'+m)
                wrd.add_number_crimes(len(crimes))
            element = {'Ward_name': wrd.get_name(), 'Price': wrd.get_price(),
                       'Schools_number': wrd.get_number_of_schools(),
                       'Crimes_number': wrd.get_number_of_crimes()}
            wrte_csv(f_name, element, i)
            i += 1
            print(neighbourhood.item.name, end=' ')
            print(i, end=' out of ')
            print(len(neighbourhoods))
        except:
            pass


def main():
    """
    The main function of this module.
    """
    Ward_array = Array()
    create_price('filtred/ward-price-2016.csv', Ward_array)
    create_schools('filtred/all_schools_2016.csv', Ward_array)
    neighbourhoods = filter_crimes(Ward_array)
    create_crimes('filtred/Wards.csv', neighbourhoods, Ward_array)


if __name__ == '__main__':
    main()
