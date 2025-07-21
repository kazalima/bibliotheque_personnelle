
class Livre:
    def __init__(self, titre, auteur, categorie, date_ajout):
        self.titre = titre
        self.auteur = auteur
        self.categorie = categorie
        self.date_ajout = date_ajout

    def __str__(self):
        return f"{self.titre} par {self.auteur} ({self.categorie}) - ajouté le {self.date_ajout}"

    def to_dict(self):
        return {
            "titre": self.titre,
            "auteur": self.auteur,
            "categorie": self.categorie,
            "date_ajout": self.date_ajout
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            titre=data["titre"],
            auteur=data["auteur"],
            categorie=data["categorie"],
            date_ajout=data["date_ajout"]
        )
