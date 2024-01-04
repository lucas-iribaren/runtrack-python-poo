class Tache:
    def __init__(self, titre, description):
        self.__titre = titre
        self.__description = description
        self.__status = "À faire"
    
    def get_titre(self):
        return self.__titre
    def get_description(self):
        return self.__description
    def get_status(self):
        return self.__status
    
    def set_titre(self, titre):
        self.__titre = titre
    def set_description(self, description):
        self.__description = description
    def set_status(self, status):
        self.__status = status


class ListeDeTaches:
    def __init__(self):
        self.tache = []
    def ajouterTache(self,tache):
        self.tache.append(tache)
        print(f"La tache {tache.get_titre()} a été ajouter")
    
    def supprimerTache(self, tache):
        self.tache.remove(tache)
        print(f"La tache {tache.get_titre()} a été supprimer")
    
    def marquerCommeFinie(self, tache):
        tache.set_status("Terminée")
        print(f"La tache {tache.get_titre()} a été marquer comme terminée")
    
    def afficherListe(self):
        print("Liste des taches:\n")
        for tache in self.tache:
            print(f"""{tache.get_titre()}
{tache.get_description()}: {tache.get_status()}
""")
    
    def filterListe(self):
        print("Liste des taches à faire:\n")
        for tache in self.tache:
            if tache.get_status() == "À faire":
                print(f"{tache.get_titre()},{tache.get_description()}")


tache1 = Tache("Vaiselle", "faire la vaiselle")
tache2 = Tache("Laver", "laver les fenetre et sol")
tache3 = Tache("Courses", "faire les courses pour la semaine")
tache4 = Tache("Révision", "revoir les notes du dernier cours")
tache5 = Tache("Jardinage", "arroser les plantes et tailler les buissons")

liste_taches = ListeDeTaches()

liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)
liste_taches.ajouterTache(tache4)
liste_taches.ajouterTache(tache5)


liste_taches.marquerCommeFinie(tache1)
liste_taches.marquerCommeFinie(tache4)

liste_taches.supprimerTache(tache4)

liste_taches.afficherListe()
liste_taches.filterListe()