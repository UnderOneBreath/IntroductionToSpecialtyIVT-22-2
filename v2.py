# a = int(input())
# b = int(input())
# p = 2*(a+b)
# print(p)

class rectangle:
    def get_perimeter(self):
        p = 2*(self.width + self.height)
        return p
    def __init__(self):
        self.width = 5
        self.height = 5

rect = rectangle()
print(rect.get_perimeter())