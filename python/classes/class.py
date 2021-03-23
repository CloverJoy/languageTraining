class Point:
    # shared across instance
    default_color = "red"
    # magic method for constructor

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # magic method

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"{self.x}, {self.y}")


point = Point(1, 2)
other = Point(1, 2)
# pass by references, memory
# need magic method
# after magic method become true
print(point == other)
print(point == other)
combined = point + other
print(combined)
# print(isinstance(point, Point))
print(str(point))
