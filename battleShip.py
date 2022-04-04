from errno import ELOOP
import json
from tracemalloc import Trace
from NumpyArrayEncoder import NumpyArrayEncoder
from bot import Bot
from player import Player
from ship import Ship
import eel
import math
import time

game = 0

@eel.expose
def pvb():
    global game
    game = 0

@eel.expose
def pvp():
    global game
    game = 1
    print("pvp")

    

@eel.expose
def getBoard():
    eel.mapBoard(json.dumps(p[0].board, cls=NumpyArrayEncoder), 0)
    eel.mapBoard(json.dumps(p[1].board, cls=NumpyArrayEncoder), 1)

@eel.expose
def attack(xCoord, yCoord, player):
    global playerTurn
    global game


    if playerTurn == player and p[0].isDefeated()==False and p[1].isDefeated()==False:
        result = 0
        x = int(xCoord)-1
        y = int(yCoord)-1
        result = 0
        if(player == 0):
            result = p[0].attack(x, y, p[1])
        else:
            result = p[1].attack(x, y, p[0])
        if(result == 0):
            eel.gameAlert("you hit there before")
        elif(result == 1):
            eel.gameAlert("miss")
            if(player == 0):
                playerTurn = 1
            else:
                playerTurn = 0
            if(game == 0):
                botAttack()
        elif(result == 2):
            eel.gameAlert("hit!!!")
        p[1].updateShips()
        p[0].updateShips()
        getBoard()
        if (p[0].isDefeated() == True):
            eel.showWinner("Player "+str(2)+" Wins.")
        elif (p[1].isDefeated() == True):
            eel.showWinner("Player "+str(1)+" Wins.")
    elif playerTurn != player:
        if(playerTurn == 0):
            eel.gameAlert("This is player "+str(1)+ "s turn")
        else:
            eel.gameAlert("This is player "+str(2)+ "s turn")
    else: 
        eel.gameAlert("Game already Ended.")

@eel.expose
def botAttack():
    global playerTurn
    if playerTurn == 1 and p[0].isDefeated()==False:
        if(p[1].targeting == True):
            if(p[1].targetedShip.isSinked == True):
                p[1].targeting = False
                p[1].targetedShip = None
                p[1].hitX = []
                p[1].hitY = []
        result = 0
        result = p[1].attack(p[0])
        if(result == 0):
            eel.gameAlert("The bot hit that place before")
            time.sleep(2)
            #botAttack()
        if(result == 1):
            eel.gameAlert("The bot missed")
            playerTurn = 0
            p[0].updateShips()
            getBoard()
        else:
            eel.gameAlert("The bot hit!!!")
            playerTurn = 1
            p[0].updateShips()
            getBoard()
            time.sleep(2)
            botAttack()

        
    if (p[0].isDefeated() == True):
        eel.showWinner("The Bot Wins.")

@eel.expose
def createboard(a, be, c, d):
    global p
    global playerturn
    global game
    playerturn = 0
    aa = int(a)
    bb = int(be)
    cc = int(c)
    dd = int(d)

    n = aa*1 + bb*2 + cc*3 + dd*4
    
    size = 10*10
    if(n > size*0.75):
        size =  int(n*2)
    print("a")
    if(game == 0):
        print("player vs c")
        size = math.isqrt(size)
        p[0] = Player(size)
        p[1] = Bot(size)
    else:
        print("player vs player")
        size = math.isqrt(size)
        p[0] = Player(size)
        p[1] = Player(size)
    

    for i in range(aa):
        p[0].addShip(Ship("Submarino"+str(i), 1))
        p[1].addShip(Ship("Submarinob"+str(i), 1))
    for i in range(bb):
        p[0].addShip(Ship("Destructor"+str(i), 2))
        p[1].addShip(Ship("Destructorb"+str(i), 2))
    for i in range(cc):
        p[0].addShip(Ship("crucero"+str(i), 3))
        p[1].addShip(Ship("crucerob"+str(i), 3))
    for i in range(dd):
        p[0].addShip(Ship("porta aviones"+str(i), 4))
        p[1].addShip(Ship("porta avionesb"+str(i), 4))

p = [Player(10), Bot(10)]
playerTurn = 0

eel.init('ui')
eel.start('index.html')