from footprint import *

class Map():
    Level=[
        "       GGG    GG    ",
        " XXXX      X        ",
        " X      XX X XXXXX  ",
        " X               XG ",
        "   X X X  XX XXX    ",
        "XX X XXX  X    X  XX",
        " X X X X  X   XX GXG",
        "          XXXXX   XX",
        "    GX              ",
        "  X GXXX  X XXX  X G",
        "  X       X X X  X G",
        "  X  XXX  X   X  X G",
        "G X  X X  X  XX XX G",
        "G    X             G",
        "GG           GGGGGGG"
    ]
    Walls = []
    Grass = []
    Space = []
    UseSpace = []


    def wall(self):
        for x in range(len(Map.Level)):
            for y in range(len(Map.Level[x])):
                character = Map.Level[x][y]
                if character == "X":
                    coordX = x * 40 + 10
                    coordY = y * 40 + 10
                    Map.Walls.append((coordY, coordX))
                if character == "G":
                    coordX = x * 40 + 10
                    coordY = y * 40 + 10
                    Map.Grass.append((coordY, coordX))
                if character == " ":
                    coordX = x * 40 + 10
                    coordY = y * 40 + 10
                    Map.Space.append((coordY, coordX))
                    #ft = footPrint(self, coordY, coordX)
                   # Map.UseSpace.append(ft)



    def addPict(self, x, y, id):
        print(id)
        print(x)
        print(y)
        for s in range(len(Map.UseSpace)):
            if Map.UseSpace[s].pX == x and Map.UseSpace[s].pY== y:
                if id == 0:
                    Map.UseSpace[s].picture.setText('wwwww')


                else:
                    #Map.UseSpace[s].addPicture('images\imgfoot2_small.png')
                    Map.UseSpace[s].picture2.setText('wwwwsdasdasdawsdww')



