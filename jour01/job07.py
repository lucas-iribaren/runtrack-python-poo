class Personnage:
    def __init__(self, x, y):
        self.co_x = x
        self.co_y = y

    def gauche(self): 
        self.co_x -=1
        print("La position de x allant vers la gauche est de :", self.co_x)
    
    def droite(self): 
        self.co_x +=1
        print("La position de x allant vers la droite est de :", self.co_x)
    
    def bas(self): 
        self.co_y -=1
        print("La position de x allant vers le bas est de :", self.co_y)
    
    def haut(self): 
        self.co_y +=1
        print("La position de x allant vers le haut est de :", self.co_y)

    def position(self):
        print(f"La position de x : {self.co_x}, la postion de y :{self.co_y}")
    

BOB= Personnage(0,0)


BOB.bas()
BOB.droite()
BOB.gauche()
BOB.haut()
BOB.droite()
BOB.position()