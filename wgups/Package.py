# package object used to store package data
class Package:
    def __init__ (self, package_id, address, city, state, zip_code, deadline, weight, special_notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes
        self.status = "At Hub"  # default  
        self.delivery_time = None  # set on a per package basis 
    
    def __str__(self):
        return (f"Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, "
                f"State: {self.state}, Zip: {self.zip_code}, Deadline: {self.deadline}, "
                f"Weight: {self.weight}, Special Notes: {self.special_notes}, "
                f"Status: {self.status}, Delivery Time: {self.delivery_time}")

        