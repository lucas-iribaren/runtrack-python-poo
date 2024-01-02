class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.produit_nom = nom
        self.produit_prixHT = prixHT
        self.produit_TVA = TVA
    
    def CalculerPrixTTC(self):
        return self.produit_prixHT + self.produit_prixHT * self.produit_TVA
    
    def afficher(self):
        return f"""
        Nom du produit : {self.produit_nom}
        Prix HT : {self.produit_prixHT}
        TVA: {self.produit_TVA}
        Prix TTC: {self.CalculerPrixTTC()}
        """
    
achat = Produit("cookie", 1, 0.28)
print(achat.afficher())

achat = Produit("brownie", 2, 0.5)
print(achat.afficher())

achat = Produit("cheesecake", 1.5, 0.38)
print(achat.afficher())


achat = Produit("chips", 2.6, 0.20)
print(achat.afficher())

