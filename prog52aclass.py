class Shape:
    # set up
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self._area = 0
        self._perim = 0 # it should only be called in the class
    
    def calculate(self):
        self._area = self.length * self.width
        self._perim = (self.legth * 2) + (self.width * 2)
    
    def get_area(self):
        return self.area
    
    def get_perim(self):
        return self.perim
    
    def main():
        legth = int(input,"set legth")
        width = int(input, "set width")
        shape = shape(legth,width)
        print("area: ",Shape.get_area())
        print("perimiter: ", shape.get_perimeter())
        pass