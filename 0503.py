class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def setx(self, x):
        self.x = x
    def setx(self, y):
        self.y = y
    def get(self):
        return  (self.x, self.y)
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

a = point(3,3)
a.get()

