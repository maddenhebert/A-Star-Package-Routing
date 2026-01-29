# ROUTING A* FUNCTIONS

import datetime as dt
import heapq

# Function for getting distance between two addresses
def get_distance(package_address, curr_address, distance_matrix, address_dict):
    destination_index = address_dict[package_address]
    curr_index = address_dict[curr_address]

    distance = distance_matrix[destination_index][curr_index]
    if distance == "":
        distance = distance_matrix[curr_index][destination_index]

    return float(distance)

# Heuristic 
def heuristic(curr_address, remaining_packages, distance_matrix, address_dict, packages_table):
    # handles goal state
    if not remaining_packages:
        return 0
    
    # determines min distances
    min_distance = float('inf')
    for id in remaining_packages:
        package = packages_table.lookup(id)
        address = package.address
        distance = get_distance(address, curr_address, distance_matrix, address_dict)

        min_distance = min(min_distance, distance)
    
    return min_distance

# Path reconstruction
def reconstruct_path(parents, state):
    pass
# A* routing structure 
def a_star_routing(truck, distance_matrix, address_dict, packages_table):
    # initial state
    start_state = (truck.location, frozenset(truck.packages))

    pq = []

    # initial 
    g_score = {start_state : 0}
    h = heuristic(truck.location, truck.packages, distance_matrix, address_dict, packages_table)

    # intializes heap and pushes starting state
    heapq.heappush(pq, (h, 0, start_state))

    while pq:
        f, g, (curr_address, remaining) = heapq.heappop(pq) 

        # checks goal (no packages left)
        if not remaining:
            return g 
        
        for next_stop in remaining:
            # creates new remaining set 
            new_remaining = set(remaining)
            new_remaining.remove(next_stop)
            new_remaining = frozenset(new_remaining)

            new_state = (next_stop, new_remaining)

            # calculating new g score 
            distance = get_distance(next_stop, curr_address, distance_matrix, address_dict)
            new_g = g + distance 

            if new_state not in g_score or new_g < g_score[new_state]:
                g_score[new_state] = new_g
                h = heuristic(next_stop, new_remaining, distance_matrix, address_dict, packages_table)
                f = new_g + h
                heapq.heappush(pq, (f, new_g, new_state))
            
    return float('inf')

''' 
OLD NEAREST NEIGHBOR FOR REFERENCE 
# nearest neighbor 
def nearest_neighbor(truck, distance_matrix, address_dict, event_log, packages_table):
    # at function start address is HUB
    current_address = truck.location

    # while there are still packages on the truck
    while truck.packages:
        # ensures there will be a shorter distance
        shortest_distance = float('inf')
        next_address = None

        # loop for finding package with shortest distance to address 
        for package_id in truck.packages:
            package = packages_table.lookup(package_id)
            package_address = package.address
            distance = get_distance(package_address, current_address, distance_matrix, address_dict)

            if distance < shortest_distance:
                shortest_distance = distance
                next_address = package_address

        # list to hold all packages at next address 
        packages_to_deliver = []

        # loop for finding all packages at the next address 
        for package_id in truck.packages:
            package = packages_table.lookup(package_id)
            if next_address == package.address:
                packages_to_deliver.append(package)

        # updates package status and remove from truck 
        for package in packages_to_deliver: 
            package.status = "Delivered"
            truck.packages.remove(package.package_id)

        # time calculations and formatting 
        travel_time = shortest_distance / 18
        travel_time = dt.timedelta(hours=travel_time)
        truck.time += travel_time

        # adds mileage to truck 
        truck.mileage += shortest_distance
        truck.mileage = round(truck.mileage, 2)
        
        # updates current location
        truck.location = next_address

        # prints completion message/s with time 
        for package in packages_to_deliver:
            event_log.append({
                "truck_id" : truck.truck_id,
                "time" : truck.time,
                "mileage" : truck.mileage,
                "package_id" : package.package_id,
                "status" : package.status 
            })

    return truck.time 
'''