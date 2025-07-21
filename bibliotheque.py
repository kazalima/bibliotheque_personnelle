
import json
from datetime import datetime
from livre import Livre

class Bibliotheque:
    def __init__(self, fichier_donnees="bibliotheque.json"):
        self.fichier_donnees = fichier_donnees
        self.livres = []
        self.charger()

    def ajouter_livre(self, titre, auteur, categorie):
        nouveau_livre = Livre(
            titre=titre,
            auteur=auteur,
            categorie=categorie,
            date_ajout=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        self.livres.append(nouveau_livre)
        self.sauvegarder()
        return nouveau_livre

    def modifier_livre(self, index, titre=None, auteur=None, categorie=None):
        if 0 <= index < len(self.livres):
            livre = self.livres[index]
            if titre:
                livre.titre = titre
            if auteur:
                livre.auteur = auteur
            if categorie:
                livre.categorie = categorie
            self.sauvegarder()
            return livre
        return None

    def supprimer_livre(self, index):
        if 0 <= index < len(self.livres):
            livre_supprime = self.livres.pop(index)
            self.sauvegarder()
            return livre_supprime
        return None

    def afficher_livres(self):
        for i, livre in enumerate(self.livres):
            print(f"{i}. {livre}")

    def rechercher_par_titre(self, titre):
        return [livre for livre in self.livres if titre.lower() in livre.titre.lower()]

    def rechercher_par_auteur(self, auteur):
        return [livre for livre in self.livres if auteur.lower() in livre.auteur.lower()]

    def trier_par_date(self, reverse=False):
        self.livres.sort(key=lambda x: x.date_ajout, reverse=reverse)

    def trier_par_categorie(self):
        self.livres.sort(key=lambda x: x.categorie)

    def sauvegarder(self):
        with open(self.fichier_donnees, 'w') as f:
            json.dump([livre.to_dict() for livre in self.livres], f, indent=4)

    def charger(self):
        try:
            with open(self.fichier_donnees, 'r') as f:
                data = json.load(f)
                self.livres = [Livre.from_dict(livre_data) for livre_data in data]
        except FileNotFoundError:
            self.livres = []
