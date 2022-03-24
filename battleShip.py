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

class bot(Player):
    def __init__(self, fieldSize, pieces):
        self.fieldSize = fieldSize
        self.field = np.zeroes(fieldSize, fieldSize)
        #Code to place pieces
        
    def attack(self, enemy, x, y, n):
        if(n==0):
            while(True):
                x = random.randint(0, self.fieldSize)
                y = random.randint(0, self.fieldSize)
                if(enemy.field[x][y]<2):
                    break
        else:
            if(enemy.field[x][y] == 0):
                enemy.field[x][y] = 2
            else: 
                enemy.field[x][y] = 3
                if(enemy.isDefeated()== False):
                    if(n%4 == 0 and x-1 > 0 and enemy.field[x-1][y] < 2):
                        self(enemy.field, x-1, y, n+1 )
                    elif(n%4 == 1 and x+1 < self.fieldSize and enemy.field[x+1][y] < 2):
                        self(enemy.field, x+1, y, n+1)
                    elif(n%4 == 2 and y-1 > 0 and enemy.field[x][y-1] < 2):
                        self(enemy.field, x, y-1, n+1)
                    elif(n%4 == 3 and y+1 < self.fieldSize and enemy.field[x][y+1] < 2):
                        self(enemy.field, x, y+1, n+1)


                



            
            
        
        


        
        
        
        
        
    
    
                
            
        
    
    
  
    
    