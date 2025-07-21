from bibliotheque import Bibliotheque

def afficher_menu():
    print("\n=== Gestion de Bibliothèque ===")
    print("1. Afficher tous les livres")
    print("2. Ajouter un livre")
    print("3. Modifier un livre")
    print("4. Supprimer un livre")
    print("5. Rechercher par titre")
    print("6. Rechercher par auteur")
    print("7. Trier par date d'ajout")
    print("8. Trier par catégorie")
    print("0. Quitter")

def main():
    bibliotheque = Bibliotheque()

    while True:
        afficher_menu()
        choix = input("Votre choix: ")

        if choix == "1":
            print("\n--- Liste des livres ---")
            bibliotheque.afficher_livres()

        elif choix == "2":
            print("\n--- Ajouter un livre ---")
            titre = input("Titre: ")
            auteur = input("Auteur: ")
            categorie = input("Catégorie: ")
            bibliotheque.ajouter_livre(titre, auteur, categorie)
            print("Livre ajouté avec succès!")

        elif choix == "3":
            print("\n--- Modifier un livre ---")
            bibliotheque.afficher_livres()
            try:
                index = int(input("Numéro du livre à modifier: "))
                titre = input("Nouveau titre (laisser vide pour ne pas modifier): ")
                auteur = input("Nouvel auteur (laisser vide pour ne pas modifier): ")
                categorie = input("Nouvelle catégorie (laisser vide pour ne pas modifier): ")

                if not any([titre, auteur, categorie]):
                    print("Aucune modification apportée.")
                    continue

                result = bibliotheque.modifier_livre(
                    index,
                    titre if titre else None,
                    auteur if auteur else None,
                    categorie if categorie else None
                )

                if result:
                    print("Livre modifié avec succès!")
                else:
                    print("Numéro de livre invalide.")
            except ValueError:
                print("Veuillez entrer un numéro valide.")

        elif choix == "4":
            print("\n--- Supprimer un livre ---")
            bibliotheque.afficher_livres()
            try:
                index = int(input("Numéro du livre à supprimer: "))
                result = bibliotheque.supprimer_livre(index)
                if result:
                    print(f"Livre '{result.titre}' supprimé avec succès!")
                else:
                    print("Numéro de livre invalide.")
            except ValueError:
                print("Veuillez entrer un numéro valide.")

        elif choix == "5":
            print("\n--- Rechercher par titre ---")
            titre = input("Titre à rechercher: ")
            resultats = bibliotheque.rechercher_par_titre(titre)
            if resultats:
                for livre in resultats:
                    print(livre)
            else:
                print("Aucun livre trouvé avec ce titre.")

        elif choix == "6":
            print("\n--- Rechercher par auteur ---")
            auteur = input("Auteur à rechercher: ")
            resultats = bibliotheque.rechercher_par_auteur(auteur)
            if resultats:
                for livre in resultats:
                    print(livre)
            else:
                print("Aucun livre trouvé avec cet auteur.")

        elif choix == "7":
            print("\n--- Trier par date d'ajout ---")
            bibliotheque.trier_par_date()
            print("Livres triés par date d'ajout (plus ancien d'abord).")

        elif choix == "8":
            print("\n--- Trier par catégorie ---")
            bibliotheque.trier_par_categorie()
            print("Livres triés par catégorie.")

        elif choix == "0":
            print("Merci d'avoir utilisé le gestionnaire de bibliothèque. Au revoir!")
            break

        else:
            print("Choix invalide. Veuillez sélectionner une option entre 0 et 8.")

if __name__ == "__main__":
    main()
