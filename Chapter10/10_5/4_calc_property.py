class Circle:
    def __init__(self, redius):
        self.redius = redius

    @property
    def diameter(self):
        return 2 * self.redius


c = Circle(5)
print(c.redius)

print(c.diameter)

c.redius = 7
print(c.diameter)

# error
# c.diameter = 20
