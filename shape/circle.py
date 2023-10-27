class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    
    def __contains__(self, point):
        x,y = point
        x0, y0 = self.center
        return ((x0 - x)**2 + (y0 - y)**2 <self.radius **2)