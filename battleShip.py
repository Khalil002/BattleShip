from errno import ELOOP
import json
from tracemalloc import Trace
from NumpyArrayEncoder import NumpyArrayEncoder
from bot import Bot
from player import Player
from ship import Ship
import eel
import math
ships = []
@eel.expose
def setShipValues(values):
    global ships
    ships = values
    print(ships)

@eel.expose
def pvb():
    print("hello")
    global ships
    s1 = Ship("Submarino", int(ships[0]))
    s2 = Ship("Destructor", int(ships[1]))
    s3 = Ship("crucero", int(ships[2]))
    s4 = Ship("porta aviones", int(ships[3]))
    s5 = Ship("Submarino", int(ships[0]))
    s6 = Ship("Destructor", int(ships[1]))
    s7 = Ship("crucero", int(ships[2]))
    s8 = Ship("porta aviones", int(ships[3]))
    p.addShip(s1)
    p.addShip(s2)
    p.addShip(s3)
    p.addShip(s4)

    b.addShip(s5)
    b.addShip(s6)
    b.addShip(s7)
    b.addShip(s8)

    

@eel.expose
def getBoard():
    eel.mapBoard(json.dumps(p.board, cls=NumpyArrayEncoder), 0)
    eel.mapBoard(json.dumps(b.board, cls=NumpyArrayEncoder), 1)

@eel.expose
def attack(xCoord, yCoord):
    global playerTurn
    if playerTurn == True and b.isDefeated()==False:
        result = 0
        x = int(xCoord)-1
        y = int(yCoord)-1
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
        b.updateShips()
        getBoard()
        if (b.isDefeated() == True):
            eel.showWinner("The Player Wins.")
    else: 
        eel.gameAlert("Game already Ended.")

@eel.expose
def botAttack():
    global playerTurn
    if playerTurn == False and p.isDefeated()==False:
        if(b.targeting == True):
            if(b.targetedShip.isSinked == True):
                b.targeting = False
                b.targetedShip = None
                b.hitX = []
                b.hitY = []
        result = 0
        result = b.attack(p)
        if(result == 1):
            eel.gameAlert("The bot missed")
            playerTurn = True
        else:
            eel.gameAlert("The bot hit!!!")
            playerTurn = False
            botAttack()
        p.updateShips()
        getBoard()
    if (p.isDefeated() == True):
        eel.showWinner("The Bot Wins.")
    
p = Player(10)
b = Bot(10)
playerTurn = True

eel.init('ui')
eel.start('index.html')