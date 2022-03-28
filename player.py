import numpy
import random

class Player:
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.board = numpy.zeros((boardSize, boardSize), int)
        self.ships = []
        
    def addShip(self, ship):
        xPos = []
        yPos = []
        rot = []
        
        sSize = ship.size
        bSize = self.boardSize
        for i in range(bSize):
            for j in range(bSize):
                possible = True
                for k in range(sSize):
                    if(i+k > bSize-1 or self.board[i+k][j]==1):
                        possible = False
                        break
                if(possible == True):
                    xPos.append(i)
                    yPos.append(j)
                    rot.append(False)
                else:
                    possible2 = True
                    for k in range(sSize):
                        if(j+k > bSize-1 or self.board[i][j+k]==1):
                            possible2 = False
                            break
                    if(possible2 == True):
                        xPos.append(i)
                        yPos.append(j)
                        rot.append(True)
                        
        if(len(xPos) > 0):
            r = random.randint(0, len(xPos)-1)
            x = xPos[r]
            y = yPos[r]
            rot = rot[r]
            if(rot==False):
                for i in range(sSize):
                    self.board[x+i][y] = 1
            else:
                for i in range(sSize):
                    self.board[x][y+i] = 1
            ship.locate(x, y, rot)
            self.ships.append(ship)
            return True
        else:
            return False
    
    def attack(self, x, y, enemy):
        #Board values:
        # 0 --> Empty
        # 1 --> contains a ship
        # 2 --> Miss
        # 3 --> Hit
        
        #Return values:
        # 0 --> That position has been attacked already
        # 1 --> Miss
        # 2 --> Hit
        result = 0
        if(enemy.board[x][y] > 1):
            result = 0
        elif(enemy.board[x][y] == 0):
            enemy.board[x][y] = 2
            result = 1
        else:
            enemy.board[x][y] = 3
            result = 2
            
        return result
        
    def isShipSinked(self, ship):
        

        sinked = True
        if(ship.rotated == False):
            for i in range(ship.size):
                
                if(self.board[ship.x+i][ship.y] == 1):
                    sinked = False
                    break
        else:
            for i in range(ship.size):
                
                if(self.board[ship.x][ship.y+i] == 1):
                    sinked = False
                    break
        
        return sinked

    
    def sunkenShips(self):
        count = 0
        for i in range(len(self.ships)):
            s = self.ships[i]
            if(s.isSinked == True):
                count = count + 1
        
        return count
                         
    def updateShips(self):
        for i in range(len(self.ships)):
            s = self.ships[i]
            s.isSinked = self.isShipSinked(s)
    
    def isDefeated(self):
        ships = len(self.ships)
        sinkedShips = self.sunkenShips()
        
        
        if(ships == sinkedShips):
            return True
        return False
    