class Shape:
    # set up
    def __init__(self, length):
        self.length = length
        self._area = 0
        self._perim = 0 # it should only be called in the class
    
    def calculate(self):
        self._area = 3.14159265358979323846264338327950288415 * self.length ** 2
        self._perim = 2 * 3.14159265358979323846264338327950288415 * self.length
    
    def get_area(self):
        return self.area
    
    def get_perim(self):
        return self.perim
    
    def main():
        legth = int(input,"set legth")
        shape = shape(legth)
        print("area: ",Shape.get_area())
        print("perimiter: ", shape.get_perim())