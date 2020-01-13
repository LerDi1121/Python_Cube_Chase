

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
    Counter=0
    TrapAndForce=[]


    def wall(self):
        self.Walls = []
        self.Grass = []
        self.Space = []
        self.TrapAndForce=[]
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
                    Map.TrapAndForce.append((coordY, coordX))
                if character == " ":
                    coordX = x * 40 + 10
                    coordY = y * 40 + 10
                    Map.Space.append((coordY, coordX))
                    Map.TrapAndForce.append((coordY, coordX))
                    Map.Counter= Map.Counter+1






