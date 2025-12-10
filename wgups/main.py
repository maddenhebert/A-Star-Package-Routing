import csv
import HashTable
import Package 

# DSA II - WGUPS Routing Program 
#Student ID: 012600680

# Distance Calculating Function 
def get_distance(package_address, current_address, distance_matrix, address_dict):
    destination_index = address_dict[package_address]
    current_index = address_dict[current_address]

    distance = distance_matrix[destination_index][current_index]
    if distance == "":
        distance = distance_matrix[current_index][destination_index]

    return float(distance)

# DATA PREP AND LOADING 
# instantiates hash table with capacity of 40
packages_table = HashTable.HashTable(40)

# opens csv file with package data
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
        weight = int(row[6])
        special_notes = row[7]

        # creates package object and inserts into hash table
        package = Package.Package(package_id, address, city, state, zip_code, deadline, weight, special_notes)
        packages.insert(package_id, package)
        
# address to index for distance lookup, read from csv file  
with open('addresses.csv') as addresses:
    reader = csv.reader(addresses)

    address_dict = {}
    index = 0

    for row in reader:
        address_dict[row[0]] = index
        index += 1


# opens csv file with distance data
with open('distances.csv') as distances:
    reader = csv.reader(distances)

    distance_matrix = []

    for row in reader:
        distance_row = []
        for item in row:
            if item == '':
                distance_row.append("")
            else:
                distance_row.append(float(item))
        distance_matrix.append(distance_row)


# LOADING TRUCKS 
# lists for each truck's packages 
truck1 = []
truck2 = []
truck3 = []




    

    


