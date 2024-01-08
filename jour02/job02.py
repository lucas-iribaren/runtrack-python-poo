class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
    
    def get_titre(self):
        return self.__titre 

    def get_auteur(self):
        return self.__auteur
    
    def get_nb_pages(self):
        return self.__nb_pages
    
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
    

mon_livre= Livre("Pokémon","Céline",205)

mon_livre.set_nb_pages(1.5)
mon_livre.set_nb_pages(-1)
mon_livre.set_nb_pages(100)
