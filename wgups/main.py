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

# Nearest Neighbor Routing Function 
def nearest_neighbor(truck, current_time, distance_matrix, address_dict):
    # at function start address is HUB
    current_address = "HUB"

    # while there are still packages on the truck
    while truck:
        # ensures there will be a shorter distance
        shortest_distance = float('inf')

        for package in truck:
            package = packages_table.lookup(package)
            package_address = package.address
            distance = get_distance(package_address, current_address, distance_matrix, address_dict)

            if distance < shortest_distance:
                shortest_distance = distance
                next_package = package
                
        next_package.status = "Delivered"
        travel_time = shortest_distance / 18
        current_time += travel_time
        print(current_time)
        truck.remove(next_package.package_id)

    print(f"Truck succesfully delivered all packages")
    return current_time


# DATA PREP AND LOADING 
# instantiates hash table with capacity of 40
packages_table = HashTable.HashTable(40)

# opens csv file with package data
with open("/Users/maddenhebert/Desktop/CS_Projects/wgups/wgups/packages.csv") as packages:
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
        packages_table.insert(package_id, package)
        
# address to index for distance lookup, read from csv file  
with open('/Users/maddenhebert/Desktop/CS_Projects/wgups/wgups/addresses.csv') as addresses:
    reader = csv.reader(addresses)

    address_dict = {}
    index = 0

    for row in reader:
        address_dict[row[0]] = index
        index += 1


# opens csv file with distance data
with open('/Users/maddenhebert/Desktop/CS_Projects/wgups/wgups/distances.csv') as distances:
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

# lists for each truck's packages 
Truck1 = [1, 13, 14, 15, 16, 19,  20, 29, 30, 31, 34, 26, 27] # Leaves first
Truck2 = [3, 6, 18, 36, 38, 25, 37, 40, 33, 35, 39] # Slightly Delayed for some packages
Truck3 = [9, 28, 32, 2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24] # Waits for one truck to finish

nearest_neighbor(Truck1, 8.0, distance_matrix, address_dict)





    




    

    


