from errno import ELOOP
import json
from tracemalloc import Trace
from NumpyArrayEncoder import NumpyArrayEncoder
from bot import Bot
from player import Player
from ship import Ship
import eel
import math





@eel.expose
def pvb():
    print("hello")
    
    s1 = Ship("Submarino", 1)
    s2 = Ship("Destructor", 2)
    s3 = Ship("crucero", 3)
    s4 = Ship("porta aviones", 4)
    s5 = Ship("Submarino", 1)
    s6 = Ship("Destructor", 2)
    s7 = Ship("crucero", 3)
    s8 = Ship("porta aviones", 4)
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
            eel.gameAlert("The Player Wins.")
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
        eel.gameAlert("The Bot Wins.")

@eel.expose
def createboard(a, b, c, d):
    n = a*1 + b*2 + c*3 + d*4
    
    size = 10*10
    if(n > size*0.75):
        size = n + n*0.5
    
    size = math.isqrt(size)
    p = Player(size)
    b = Bot(size)

    for i in range(a):
        p.addShip(Ship("Submarino"+i, 1))
        b.addShip(Ship("Submarinob"+i, 1))
    for i in range(b):
        p.addShip(Ship("Destructor"+i, 2))
        b.addShip(Ship("Destructorb"+i, 2))
    for i in range(c):
        p.addShip(Ship("crucero"+i, 3))
        b.addShip(Ship("crucerob"+i, 3))
    for i in range(d):
        p.addShip(Ship("porta aviones"+i, 4))
        b.addShip(Ship("porta avionesb"+i, 4))



    
    



p = Player(10)
b = Bot(10)
playerTurn = True

eel.init('ui')
eel.start('index.html')