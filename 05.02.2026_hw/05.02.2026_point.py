class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_left(self, value):
        self.x -= value

    def move_right(self, value):
        self.x += value

    def move_up(self, value):
        self.y += value

    def move_down(self, value):
        self.y -= value

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"
