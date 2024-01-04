class Joueur:
    def __init__(self, nom, numero, position):
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__nb_but = 0
        self.__nb_passe = 0
        self.__nb_carton_jaune = 0
        self.__nb_carton_rouge = 0

    def get_nom(self):
        return self.__nom
    def get_numero(self):
        return self.__numero
    def get_position(self):
        return self.__position
    def get_nb_but(self):
        return self.__nb_but
    def get_nb_passe(self):
        return self.__nb_passe
    def get_nb_carton_jaune(self):
        return self.__nb_carton_jaune
    def get_nb_carton_rouge(self):
        return self.__nb_carton_rouge
    
    def set_nom(self,nom):
        self.__nom = nom
    def set_numero(self,numero):
        self.__numero = numero
    def set_position(self,position):
        self.__position = position
    def set_nb_but(self,nb_but):
        self.__nb_but = nb_but
    def set_nb_passe(self,nb_passe):
        self.__nb_passe = nb_passe
    def set_nb_carton_jaune(self,nb_carton_jaune):
        self.__nb_carton_jaune = nb_carton_jaune
    def set_nb_carton_rouge(self,nb_carton_rouge):
        self.__nb_carton_rouge = nb_carton_rouge

    def marquerUnBut(self):
        self.set_nb_but(self.__nb_but + 1)
        print(f"[--But--]{self.__nom} a marqué un but !")

    def effectuerUnePasseDecisive(self):
        self.set_nb_passe(self.__nb_passe +1)
        print(f"[--PassD--]{self.__nom} a fait la passe décisive.")
    
    def recevoirUnCartonJaune(self):
        self.set_nb_carton_jaune(self.__nb_carton_jaune +1)
        print(f"[--CartJ--]{self.__nom} a reçu un carton jaune.")
        if self.__nb_carton_jaune == 2:
            self.__nb_carton_jaune = 0
            self.recevoirUnCartonRouge()
            print(f"[--CartR--] Deuxième carton jaune pour {self.__nom}! Il obtient un carton rouge !")

    def recevoirUnCartonRouge(self):
        self.set_nb_carton_rouge(self.get_nb_but() +1)
        print(f"[--CartR--]{self.__nom} a reçu un carton rouge.")
    def afficherStatistiques(self):
        print(f"""
              Nom: {self.__nom}  Numéro: {self.__numero}  Position: {self.__position}
              Nombre de but marqués: {self.__nb_but}
              Nombre de passe décisives: {self.__nb_passe}
              Nombre cartons jaune: {self.__nb_carton_jaune}
              Nombre cartons rouge: {self.__nb_carton_rouge}""")
        
class Equipe:
    def __init__(self, nom):
        self.__nom = nom
        self.__list_joueur = []
    
    def get_nom(self):
        return self.__nom
    def get_list_joueur(self):
        return self.__list_joueur
    
    def set_list_joueur(self, list_joueur):
        self.__list_joueur = list_joueur
    
    def ajouterJoueur(self,joueur):
        self.__list_joueur.append(joueur)
        print(f"[--ADD--]Le joueur {joueur.get_nom()} a été ajouter à l'{self.get_nom()}")
    def AfficherStatistiquesJoueurs(self):
        print("\n",self.get_nom())
        for joueur in self.__list_joueur:
            joueur.afficherStatistiques()
    def mettreAJourStatistiquesJoueur(self,joueur,but_marquer,passe_decisive,carton_jaune,carton_rouge):
        joueur.set_nb_but(but_marquer)
        joueur.set_nb_passe(passe_decisive)
        joueur.set_nb_carton_jaune(carton_jaune)
        joueur.set_nb_carton_rouge(carton_rouge)
        print("[--MaJ--]Mis à jour des statistiques des joueurs.")


equipe1 = Equipe("équipe 1")
joueur1 = Joueur("bob",68,"Attaquant")
joueur2 = Joueur("bobby",12,"gardien")
equipe2 = Equipe("équipe 2")
joueur3 = Joueur("Gary",17,"Attaquant")
joueur4 = Joueur("Jack",55,"gardien")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur4)


equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()

print("Le match commence !!!")

joueur2.effectuerUnePasseDecisive()
joueur1.marquerUnBut()
joueur4.recevoirUnCartonJaune()
joueur4.recevoirUnCartonJaune()
joueur3.recevoirUnCartonRouge()
joueur1.marquerUnBut()
joueur1.marquerUnBut()

equipe1.mettreAJourStatistiquesJoueur(joueur1,3,2,0,0)
equipe1.mettreAJourStatistiquesJoueur(joueur2,0,2,1,0)
equipe2.mettreAJourStatistiquesJoueur(joueur3,0,5,0,1)
equipe2.mettreAJourStatistiquesJoueur(joueur4,2,2,0,0)

equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()

print("Le match est terminée !")
print("L'équipe 1 à gagné !")