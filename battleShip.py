import json
from NumpyArrayEncoder import NumpyArrayEncoder
from bot import Bot
from player import Player
from ship import Ship

import eel

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
            if(b.targetedShip.isSinked == True):
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