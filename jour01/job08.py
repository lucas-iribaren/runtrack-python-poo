class Cercle:
    def __init__(self,rayon):
        self.cercle_rayon = rayon
    
        
    def changerRayon(self, nouveau_rayon):
        self.cercle_rayon = nouveau_rayon
        self.afficherInfos()
        

    def afficherInfos(self):
        print(f'Le rayon est de {self.cercle_rayon}')
        print(f"La circonference est de {self.circonference()}")        
        print(f"La circonference est de {self.aire()}")
        print(f"La circonference est de {self.diametre()}")

    def circonference(self):
        cercle_circonference = self.cercle_rayon * 2 * 3.14
        return cercle_circonference
        
    def aire(self):
        cercle_aire = 3.14 * self.cercle_rayon * self.cercle_rayon
        return cercle_aire

    def diametre(self):
        cercle_diametre= self.cercle_rayon * 2
        return cercle_diametre
        
cercle1 = Cercle(4)
cercle1.afficherInfos()

cercle2 = Cercle(7)
cercle2.changerRayon(7)
