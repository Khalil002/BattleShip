import random
import numpy as np
from player import Player

class Bot(Player):
    def __init__(self, boardSize):
        super().__init__(boardSize)
        self.targeting = False
        self.hitX = []
        self.hitY = []
    
    
    
    def randomAttack(self, enemy):
        while(True):
            x = random.randint(0, self.boardSize-1)
            y = random.randint(0, self.boardSize-1)
            if(enemy.board[x][y]<2):
                break
        result = super().attack(x, y, enemy)
            
        if(result == 2):
            self.targeting = True
            for i in range(len(enemy.ships)):
                if(enemy.ships[i].contains(x, y)):
                    self.targetedShip = enemy.ships[i]
                    self.hitX.append(x)
                    self.hitY.append(y)
                    break
        return result
        
    def targetedAttack(self, enemy):
        result = -1
        x = 0
        y = 0
        if(len(self.hitX) == 1):
            x = self.hitX[0]
            y = self.hitY[0]
            if(x-1 > -1 and enemy.board[x-1][y] < 2):
                
                x = x-1
                result = super().attack(x, y, enemy)
            elif(x+1 < self.boardSize and enemy.board[x+1][y] < 2):
                
                x = x+1
                result = super().attack(x, y, enemy)
            elif(y-1 > -1 and enemy.board[x][y-1] < 2):
                
                print(y-1)
                
                y = y-1
                result = super().attack(x, y, enemy)
            elif(y+1 < self.boardSize):
                
                y = y+1
                result = super().attack(x, y, enemy)
        else:
            if(self.targetedShip.rotated == False):
                
                found = False
                y = self.hitY[0]
                for i in range(len(self.hitX)):
                    x = self.hitX[i]-1
                    if(x >= 0 and enemy.board[x][y] < 2 and self.hitY[i] == y):
                        found = True
                        break
                if(found):
                    
                    result = super().attack(x, y, enemy)
                    
                else:
                    found2 = False
                    for i in range(len(self.hitX)):
                        x = self.hitX[i]+1
                        if(x < self.boardSize and enemy.board[x][y] < 2 and self.hitY[i] == y):
                            found2= True
                            break
                    if(found2):
                        
                        result = super().attack(x, y, enemy)

                    
                    
                        
            else:
                
                found = False
                x = self.hitX[0]
                for i in range(len(self.hitY)):
                    y = self.hitY[i]-1
                    if(y >= 0 and enemy.board[x][y] < 2 and self.hitX[i]==x):
                        found = True
                        break
                if(found):
                    
                    result = super().attack(x, y, enemy)
                    
                else:
                    found2 = False
                    for i in range(len(self.hitY)):
                        y = self.hitY[i]+1
                        if(y < self.boardSize and enemy.board[x][y] < 2  and self.hitX[i]==x):
                            found2 = True
                            break
                    
                    if(found2):
                        
                        result = super().attack(x, y, enemy)
        
        if(result == 2):
            self.hitX.append(x)
            self.hitY.append(y)
        elif(result == -1):
            self.targeting = False
            self.targetedShip = None
            self.hitX = []
            self.hitY = []
            self.randomAttack(enemy)
        return result

    def attack(self, enemy):
        if(self.targeting == True):
            return self.targetedAttack(enemy)
        else:
            return self.randomAttack(enemy)
  