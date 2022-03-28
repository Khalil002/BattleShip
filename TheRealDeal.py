import numpy
import random

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
                x = x-1
                result = super().attack(x, y, enemy)
            elif(x+1 < self.boardSize and enemy.board[x+1][y] < 2):
                x = x+1
                result = super().attack(x, y, enemy)
            elif(y-1 > -1 and enemy.board[x][y-1] < 2):
                y = y-1
                result = super().attack(x, y, enemy)
            elif(y+1 < self.boardSize):
                y = y+1
                result = super().attack(x, y, enemy)
        else:
            if(self.hitY[0] == self.hitY[1]):
                #Bot finds out the ship is in rotation 0
                found = False
                y = self.hitY[0]
                for i in range(self.hitX):
                    x = self.hitX[i]-1
                    if(x >= 0 and enemy.board[x][y] < 2):
                        found = True
                        break
                if(found):
                    result = super().attack(x, y, enemy)
                else:
                    found2 = False
                    for i in range(self.hitX):
                        x = self.hitX[i]+1
                        if(x < self.boardSize and enemy.board[x][y] < 2):
                            break
                    
                    result = super().attack(x, y, enemy)
                        
            else:
                #Bot finds out the ship is in rotation 1
                found = False
                x = self.hitX[0]
                for i in range(self.hitY):
                    y = self.hitY[i]-1
                    if(y >= 0 and enemy.board[x][y] < 2):
                        found = True
                        break
                if(found):
                    result = super().attack(x, y, enemy)
                else:
                    found2 = False
                    for i in range(self.hitY):
                        y = self.hitY[i]+1
                        if(y < self.boardSize and enemy.board[x][y] < 2):
                            break
                    
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
        
    
    
p = Player(10)

b = Bot(10)

s1 = Ship("Submarino", 1)
s2 = Ship("Destructor", 2)
s3 = Ship("crucero", 3)
s4 = Ship("porta aviones", 4)
s5 = Ship("Submarino", 1)
s6 = Ship("Destructor", 2)
s7 = Ship("crucero", 3)
s8 = Ship("porta aviones", 4)

#p.addShip(s1)
p.addShip(s2)
#p.addShip(s3)
#p.addShip(s4)


#b.addShip(s5)
b.addShip(s6)
#b.addShip(s7)
#b.addShip(s8)

playerTurn = True
while(True):
    if(p.isDefeated() == True):
      print("player looses")
      break
    elif(b.isDefeated() == True):
      print("player wins")
      break
    
    print("Player board")
    s = ""
    for i in range(p.boardSize):
        for j in range(p.boardSize):
            s = s + str(p.board[i][j]) + " "
        s = s + "\n"
    print(s)
    print("")

    print("Bot board")
    s = ""
    for i in range(b.boardSize):
        for j in range(b.boardSize):
            s = s + str(b.board[i][j]) + " "
        s = s + "\n"
    print(s)
    print("")

    
    
    if(playerTurn == True):
        result = 0
        print("X position to attack (0 to 9)")
        x = int(input())
        print("Y position to attack (0 to 9)")
        y = int(input())
        result = p.attack(x, y, b)
        if(result == 0):
            print("you hit there before")
            playerTurn = True
            
        elif(result == 1):
            print("miss")
            playerTurn = False
            
        elif(result == 2):
            print("hit!!!")
            playerTurn = True
            
    if(playerTurn == False):
        if(b.targeting == True):
            if(b.targetedShip.isSunken == True):
                b.targeting = False
                b.targetedShip = None
                b.hitX = []
                b.hitY = []
        result = 0
        result = b.attack(p)
        
        if(result == 0):
            print("That spot has already been attacked")
            playerTurn = True
        elif(result == 1):
            print("The bot missed")
            playerTurn = True
        else:
            print("The bot hit!!!")
            playerTurn  = False
            if(result == None):
              break

    p.updateShips()
    b.updateShips()