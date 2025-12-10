import csv
import HashTable
import Package 

# DSA II - WGUPS Routing Program 
#Student ID: 012600680

# instantiates hash table with capacity of 40
packages = HashTable.HashTable(40)

# opens csv file with package data and reads each row
with open('packages.csv') as packages:
    reader = csv.reader(packages) 

    # for each row, data is stored in variables and a package is made 
    for row in reader:
        package_id = int(row[0])
        address = row[1]
        city = row[2]
        state = row[3]
        zip_code = row[4]
        deadline = row[5]
        weight = row[6]
        special_notes = row[7]

        # creates package object and inserts into hash table
        package = Package.Package(package_id, address, city, state, zip_code, deadline, weight, special_notes)
        packages.insert(package_id, package)

# lists for each truck's packages 
truck1 = []
truck2 = []
truck3 = []




    

    


