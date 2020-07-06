#Getters and setters are here.
#Helps in implementing constraints. 

class celsius:
    def __init__(self,temperature = 0):
        self.set_temperature(temperature)
    def to_farenheit(self):
        return (self.get_temperature()*1.8)+32
    def get_temperature(self):
        print("Getting the value...")
        return self._temperature #private variable 
    def set_temperature(self,value):
        if value < -273.15:
            raise ValueError("Temperature cannot go below absolute zero 0K...") 
        print("Setting values...")
        self._temperature = value #here underscore means private variable in python

temperature = property(get_temperature, set_temperature)
c = celsius(25)
c.get_temperature()
c.set_temperature(10)
c.to_farenheit()