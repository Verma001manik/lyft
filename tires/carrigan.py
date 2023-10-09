from tires.tires import Tires

class Carrigan(Tires):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array
        self.tire_array = []
        pass 
    def needs_service(self):
        for tire in self.tire_wear_array:
            if tire >= 0.9:
                return True
            else:
                return False
        
