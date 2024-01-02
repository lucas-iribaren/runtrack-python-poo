class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom



    def SePresenter(self):
        return f"Bonjour je m'appelle {self.prenom}, mon nom est {self.nom}"



personne1 = Personne("Madec","Lucy")
personne2 = Personne("Iribaren","Lucas")
personne3 = Personne("Martinie de Maisonneuve","Lucas")
personne4 = Personne("Peretti","Kévin")

personne1.SePresenter()
personne2.SePresenter()
personne3.SePresenter()
personne4.SePresenter()

print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())
print(personne4.SePresenter())
