from errno import ELOOP
import json
from tracemalloc import Trace
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

p.addShip(s1)
p.addShip(s2)
p.addShip(s3)
p.addShip(s4)

b.addShip(s1)
b.addShip(s2)
b.addShip(s3)
b.addShip(s4)
#eel.mapBoard(json.dumps(p.board, cls=NumpyArrayEncoder), 0)
#eel.mapBoard(json.dumps(b.board, cls=NumpyArrayEncoder), 1)
playerTurn = True


@eel.expose
def getBoard():
    print("hello")
    eel.mapBoard(json.dumps(p.board, cls=NumpyArrayEncoder), 0)
    eel.mapBoard(json.dumps(b.board, cls=NumpyArrayEncoder), 1)


@eel.expose
def attack(xCoord, yCoord):
    global playerTurn
    

    
    if playerTurn == True and (p.isDefeated() == False or b.isDefeated() == False):
        result = 0
        x = int(xCoord)
        y = int(yCoord)
        result = p.attack(x, y, b)
        if(result == 0):
            eel.gameAlert("you hit there before")
            playerTurn = True
        elif(result == 1):
            eel.gameAlert("miss")
            playerTurn = False
            botAttack()
        elif(result == 2):
            eel.gameAlert("hit!!!")
            playerTurn = True
    elif playerTurn == False:
        eel.gameAlert("Not your turn")
    elif playerTurn == False and (p.isDefeated() == True or b.isDefeated() == True):
        eel.gameAlert("Game Ended.");
    p.updateShips()
    b.updateShips()
    getBoard()

def botAttack():
    global playerTurn
    if(b.targeting == True):
            if(b.targetedShip.isSunken == True):
                b.targeting = False
                b.targetedShip = None
                b.hitX = []
                b.hitY = []
                result = 0
                result = b.attack(p)
                if(result == 0):
                    eel.gameAlert("That spot has already been attacked")
                    playerTurn = True
                elif(result == 1):
                    eel.gameAlert("The bot missed")
                    playerTurn = True
                else:
                    eel.gameAlert("The bot hit!!!")
                    playerTurn = False
eel.init('ui')
eel.start('index.html')
