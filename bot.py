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
        result = 0
        x = 0
        y = 0
        if(len(self.hitX) == 1):
            x = self.hitX[0]
            y = self.hitY[0]
            if(x-1 > -1 and enemy.board[x-1][y] < 2):
                print("AT 00000000")
                print(self.boardSize)
                print(x-1)
                print(y)
                x = x-1
                result = super().attack(x, y, enemy)
            elif(x+1 < self.boardSize and enemy.board[x+1][y] < 2):
                print("AT 111111111")
                print(self.boardSize)
                print(x+1)
                print(y)
                x = x+1
                result = super().attack(x, y, enemy)
            elif(y-1 > -1 and enemy.board[x][y-1] < 2):
                print("AT 2222222222")
                print(self.boardSize)
                print(x)
                print(y-1)
                
                y = y-1
                result = super().attack(x, y, enemy)
            elif(y+1 < self.boardSize):
                print("AT 3333333333")
                print(self.boardSize)
                print(x)
                print(y+1)
                y = y+1
                result = super().attack(x, y, enemy)
        else:
            if(self.hitY[0] == self.hitY[1]):
                #Bot finds out the ship is in rotation 0
                found = False
                y = self.hitY[0]
                for i in range(len(self.hitX)):
                    x = self.hitX[i]-1
                    if(x >= 0 and enemy.board[x][y] < 2):
                        found = True
                        break
                if(found):
                    print("AT 4444444444")
                    print(self.boardSize)
                    print(x)
                    print(y)
                    result = super().attack(x, y, enemy)
                    
                else:
                    found2 = False
                    for i in range(len(self.hitX)):
                        x = self.hitX[i]+1
                        if(x < self.boardSize and enemy.board[x][y] < 2):
                            found2= True
                            break
                    if(found2):
                        print("AT 5555555555")
                        print(self.boardSize)
                        print(x)
                        print(y)
                        result = super().attack(x, y, enemy)

                    
                    
                        
            else:
                #Bot finds out the ship is in rotation 1
                found = False
                x = self.hitX[0]
                for i in range(len(self.hitY)):
                    y = self.hitY[i]-1
                    if(y >= 0 and enemy.board[x][y] < 2):
                        found = True
                        break
                if(found):
                    print("AT 6666666665")
                    print(self.boardSize)
                    print(x)
                    print(y)
                    result = super().attack(x, y, enemy)
                    
                else:
                    found2 = False
                    for i in range(len(self.hitY)):
                        y = self.hitY[i]+1
                        if(y < self.boardSize and enemy.board[x][y] < 2):
                            found2 = True
                            break
                    
                    if(found2):
                        print("AT 777777777777")
                        print(self.boardSize)
                        print(x)
                        print(y)
                        result = super().attack(x, y, enemy)
        
        if(result == 2):
            self.hitX.append(x)
            self.hitY.append(y)
        return result

    def attack(self, enemy):
        if(self.targeting == True):
            return self.targetedAttack(enemy)
        else:
            return self.randomAttack(enemy)
  