class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.x = 0
        self.y = 0
        self.rotated = False
        self.isSinked = False
        
    def locate(self, x, y, rotated):
        self.x = x
        self.y = y
        self.rotated = rotated

    def setSize(self, size):
        self.size = size
        
    def contains(self, x, y):
        contains = False
        
        if(self.rotated == False and self.y == y):
            for i in range(self.size):
                if(self.x + i == x):
                    contains = True
                    break
        elif(self.x == x):
            for i in range(self.size):
                if(self.y + i == y):
                    contains = True
                    break
        
        return contains