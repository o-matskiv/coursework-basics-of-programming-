# coursework-basics-of-programming 
The purpose of the program is to find the dependence of the number of crimes from the price of housing and the number of schools in certain Ward.

Input: database of schools, average housing prices and crimes in each Ward.
Output:Ward_name,Price,Schools_number,Crimes_number and two graphs.

The structure of the main module:

  filter_prices.main () # Collecting and filtering prices
  # The module works with the file info / land-registry-house-prices-ward.csv
  # and writes to the filtred / ward-price-2016.csv file all relevant information

  filter_schools.main () #Collecting and filtering schools
  # The module works with the info / all_schools_2016.csv file
  # and writes all the relevant information to the filtred / all_schools_2016.csv file

  create_wards.main () # Collecting and filing districts
  # The module works with files filtred / all_schools_2016.csv, filtred / ward-price-2016.csv and with police UK API
  # to create an array of Ward objects and filtred / Wards.csv file with a structure
  #Ward_name,Price,Schools_number,Crimes_number

  draw_graph.main () # Draw graphs
  # The module works with info / Wards.csv file and draws graphs
  
Quick instruction for using the program: run draw_graph.py, if all information is collected and filtered, main.py - if the information is in its original form.

To test the performance of the program, I only took part of the databases (up to 50 Wards) and checked if the program could make an array of Ward objects and draw a graph on those data.
