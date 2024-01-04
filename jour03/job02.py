class CompteBancaire:
    def __init__(self, num_compte, nom, prenom, money, decouvert):
        self.__num_compte=  num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__money = money
        self.__decouvert = decouvert

    def get_num_compte(self):
        return self.__num_compte
    def get_nom(self):
        return self.__nom
    def get_prenom(self):
        return self.__prenom
    def get_money(self):
        return self.__money
    def get_decouvert(self):
        return self.__decouvert

    def set_num_compte(self, num_compte):
        self.__num_compte=  num_compte
    def set_nom(self, nom):
        self.__nom = nom
    def set_prenom(self, prenom):
        self.__prenom = prenom
    def set_money(self, money):
        self.__money = money
    def set_decouvert(self, decouvert):
        self.__decouvert = decouvert

    def afficher(self):
        print(f"""              
Numéro du compte: {self.get_num_compte()}
Nom: {self.get_nom()}
Prénom: {self.get_prenom()}
                """)
    
    def afficherSolde(self):
        print(f"Votre money est de : {self.get_money()}\n")

    def versement(self, montant):
        self.set_money(self.get_money() + montant)
        print(f"Votre compte a été créditer de {montant}€.")
    
    def retrait(self, montant):
        if (self.get_money() - montant > 0 or self.get_decouvert()) and isinstance(montant,int):
            self.set_money(self.get_money() - montant)
            print(f"Votre compte a été débité de {montant}€.")
            self.agios()
        else:
            if montant % 1 != 0:
                print("Impossible de retirer un montant non entier.")

            elif montant > self.get_money():
                print("Solde insuffisant. Impossible de retirer le montant spécifié.")
    
    def agios(self):
        if self.get_money() < 0:
            self.set_money(self.get_money()-10)
            print("Agios effectué, retrait de 10€")
        
    def virement(self, reference, num_compte, montant):
        if (self.get_money() - montant > 0 or self.get_decouvert()) and isinstance(montant,int) :
            self.set_money(self.get_money() - montant)
            num_compte.versement(montant)
            print(f"Virement du compte {self.get_num_compte()} d'un montant de {montant} vers le compte {num_compte.get_num_compte()},")
        else:
            pass


compte_bob = CompteBancaire(568132,"Razowski","Bob",10000,True)
compte_sully = CompteBancaire(100412,"Jacques","Sully",-100,True)

compte_bob.afficher()
compte_bob.afficherSolde()

compte_bob.versement(1000)
compte_bob.afficherSolde()

compte_bob.retrait(15000)
compte_bob.afficherSolde()

compte_bob.retrait(500.1)
compte_bob.afficherSolde()

compte_bob.retrait(150)
compte_bob.afficherSolde()

compte_sully.afficher()
compte_sully.afficherSolde()
compte_bob.virement("128732",compte_sully, 100)
compte_bob.afficherSolde()
compte_sully.afficherSolde()