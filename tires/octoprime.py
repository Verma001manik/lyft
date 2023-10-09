from tires.tires import Tires

class Octoprime(Tires):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array
        self.sum = 0 


    def needs_service(self):
        for tire in self.tire_wear_array:
            self.sum += tire 
            if self.sum >= 3:
                return True 
            else : 
                return False
            