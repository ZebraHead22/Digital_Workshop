class Point2D:
    __slots__ = ('x', 'y')
    MAX_COORD = 100 # При сравнении убрать

    def __init__(self, x, y):
        self.x = x
        self.y = y

pt = Point(1, 2)
# pt2 = Point2D(10, 20)

pt.MAX_COORD