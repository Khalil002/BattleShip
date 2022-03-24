import numpy as np
import random

class Player:
    def __init__(self, fieldSize, pieces):
        self.fieldSize = fieldSize
        self.field = np.zeroes(fieldSize, fieldSize)
        #Code to place pieces
    
    def attack(self, enemyField, x, y):
        if(enemyField[x][y]==2 or enemyField[x][y]==3):
            return 0
        if(enemyField[x][y] == 0):
            enemyField[x][y] = 2
            return 1
        else:
            enemyField[x][y] = 3
            return 2
            
    
    def isDefeated(self):
        isDefeated = True
        for i in range(self.fieldSize):
            for j in range(self.fieldSize):
                if(self.field == 1):
                    isDefeated = False
                    break
            if(isDefeated == False):
                break
        return isDefeated