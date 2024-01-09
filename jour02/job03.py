class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True    

    def get_titre(self):
        return self.__titre 

    def get_auteur(self):
        return self.__auteur
    
    def get_nb_pages(self):
        return self.__nb_pages
    
    def get_disponible(self):
        return self.__disponible
    
    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nb_pages(self, nb_pages):
        self.__nb_pages = nb_pages
        if isinstance(nb_pages, int) and nb_pages > 0:
            print("Changement du nombre de page :", nb_pages)
        else:
            print("Erreur, veuillez mettre un nombre positif ou un nombre entier")

    def set_disponible(self):
        self.__disponible = True
    
    def verification(self):
        return self.__disponible 
    
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print(f"Vous avez emprunter {self.__titre}, veuillez le rendez avant 7 jours.")
        else:
            print(f"{self.__titre} n'est pas disponible pour le moment, repassez plus tard.")
            
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu avec succès.")
        else:
            print("Le livre n'a pas été emprunté. Impossible de le rendre.")

        
mon_livre= Livre("Pokémon","Céline",205)

mon_livre.emprunter()
mon_livre.emprunter()
mon_livre.rendre()
mon_livre.rendre()