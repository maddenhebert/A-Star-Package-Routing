# truck class for storing package ids, time and mileage
class truck:
    def __init__(self, truck_id, departure_time, packages):
        self.truck_id = truck_id
        self.departure_time = departure_time 
        self.packages = packages.copy()
        self.starting_load = packages.copy()
        self.mileage = 0.0
        self.time = departure_time
        self.location = "HUB" # default starting location

    