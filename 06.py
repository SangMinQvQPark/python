class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y
    def get(self):
        return (self.x, self.y)
    def move(self, dx,dy):
        self.x += dx
        self.y += dy

a = Point(3,3)
a.get()

a.set_x(4)
a.set_y(2)
a.get()

a.move(2,2)
a.get()
