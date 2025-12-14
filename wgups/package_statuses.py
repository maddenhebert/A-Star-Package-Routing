# function for aquiring all package statuses at a given time 
def package_statuses(packages_table, selected_time, event_log, truck1, truck2, truck3):
    status = {}

    # extracts the delivery time from each package event 
    delivery_times = {event["package_id"] : event["time"] for event in event_log}

    # loops through every package id
    for package_id in range(1, 41):

        # this sequence of conditionals checks which truck the package is on, and finds departure time 
        if package_id in truck1.starting_load:
            departure = truck1.departure_time
            truck = "Truck 1"

        elif package_id in truck2.starting_load:
            departure = truck2.departure_time
            truck = "Truck 2"

        elif package_id in truck3.starting_load:
            departure = truck3.departure_time
            truck = "Truck 3"
        
        # extracts delivery time for package 
        delivery_time = delivery_times.get(package_id, None)

        # these conditionals check time constraints to determine package status 
        if selected_time < departure:
            status[package_id] = f"Package {package_id} At HUB on {truck}"

        elif delivery_time <= selected_time:
            status[package_id] = f"Package {package_id} Delivered at {delivery_time} on {truck}"

        else:
            status[package_id] = f"Package {package_id} En Route on {truck}"

    return status 