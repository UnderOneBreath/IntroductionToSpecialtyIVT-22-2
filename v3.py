import math
class triangle(object):
    def __init__(self):
        self.x1 = 0
        self.y1 = 15
        self.x2 = -10
        self.y2 = 10
        self.x3 = 0
        self.y3 = 0
    def get_half_petimeter(self, d1, d2, d3):
        return (d1 + d2 + d3) / 2
    def get_distance(self, x1, x2, y1, y2):
        return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    def get_area(self):
        d1 = self.get_distance(self.x1, self.x2, self.y1, self.y2)
        d2 = self.get_distance(self.x1, self.x3, self.y1, self.y3)
        d3 = self.get_distance(self.x2, self.x3, self.y2, self.y3)
        half_perimeter = self.get_half_petimeter(d1, d2, d3)
        ### calculate triangle area by Heron's formula
        return math.sqrt( half_perimeter * (half_perimeter - d1) * (half_perimeter - d2) * (half_perimeter - d3))
print(triangle().get_area())