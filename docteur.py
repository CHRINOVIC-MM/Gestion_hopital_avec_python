import os
from clear_consol import clear_consol


"""définition de fonction Enregistrer un docteur : nom, prenom, postnom, téléphone
, matricule, spécialisation (ex: pédiatre, gynecologue, etc.)"""
docteurs = []

def enregistre_docteur(prenom, nom, postnom, tel, specialisation, genre):
    clear_consol()
    print("################################################################")
    print("##                                                            ##")
    print("##                    ENREGISTRER UN DOCTEURS                 ##")
    print("##                                                            ##")
    print("################################################################")
    identites_docteur= []
    matricule = nom[0]+postnom[0]+prenom[0:4]+tel[-1:-4:-1]
    identites_docteur.append(prenom.upper())
    identites_docteur.append(nom.upper())
    identites_docteur.append(postnom.upper())
    identites_docteur.append(specialisation.upper())
    identites_docteur.append(tel)
    identites_docteur.append(matricule.upper())
    identites_docteur.append(genre.upper())
    docteurs.append(identites_docteur)


"""Afficher tous les docteurs"""
def afficher_docteur():
    clear_consol()
    print("################################################################")
    print("##                                                            ##")
    print("##        VOICI LA LISTE DE TOUS LES DOCTEURS                ##")
    print("##                                                            ##")
    print("################################################################")
    if len(docteurs) > 0:
        for i in range(len(docteurs)):
            print(f'\nPrénom : {docteurs[i][0]}\nNom: {docteurs[i][1]}\nPostnom: {docteurs[i][2]}\nSpécialité : {docteurs[i][3]}\nNuméro de téléphone : {docteurs[i][4]}\nMatricule : {docteurs[i][5]}\nGenre : {docteurs[i][6]}\n')
    else :
        print("La liste est encore vide !")


def afficher_horaire(prenom, nom, postnom):
    clear_consol()
    chercher_docteur = []
    for i in range(len(docteurs)):
        if len(docteurs[i]) >= 8:
            chercher_docteur.append(prenom.upper())
            chercher_docteur.append(nom.upper())
            chercher_docteur.append(postnom.upper())
            for i in range(len(docteurs)):
                for j in docteurs[i]:
                    if chercher_docteur[0] == docteurs[i][0] and chercher_docteur[1] == docteurs[i][1] and chercher_docteur[2] == docteurs[i][2]:
                        print(f'Prénom : {docteurs[i][0]}\nNom: {docteurs[i][1]}\nPostnom : {docteurs[i][2]}\nVoici son horaire :\n     Lundi :{docteurs[i][7][0]}\n       Mardi :{docteurs[i][7][1]}\n       Mercredi :{docteurs[i][7][2]}\n        Jeudi :{docteurs[i][7][3]}\n      Vendredi :{docteurs[i][7][4]}\n       Samedi{docteurs[i][7][5]}\n       Dimanche :{docteurs[i][7][6]}')
                        break
                    else :
                        print("Ses identifiants ne sont pas dans la liste des docteurs")
                        break
        else:
            print("Pour ce médecin l'horaire n'est pas encore enregistre")




def enregistrer_horaire(prenom, nom, postnom):
    clear_consol()
    print("################################################################")
    print("##                                                            ##")
    print("##             ENREGISTRER L'HORAIRE D'UN DOCTEUR               ##")
    print("##                                                            ##")
    print("################################################################")
    horaire = []
    identifiants = []
    identifiants.append(prenom.upper())
    identifiants.append(nom.upper())
    identifiants.append(postnom.upper())
    for i in range(len(docteurs)):
        #find = False
        for j in docteurs[i]:
            if  identifiants[0] ==docteurs [i][0] and  identifiants[1] ==docteurs [i][1] and  identifiants[2] ==docteurs [i][2] :
                jour1 = input("Entrez son horaire du lundi: ")
                jour2 = input("Entrez son horaire du mardi: ")
                jour3 = input("Entrez son horaire du mercredi: ")
                jour4 = input("Entrez son horaire du jeudi: ")
                jour5 = input("Entrez son horaire du vendredi: ")
                jour6 = input("Entrez son horaire du samedi: ")
                jour7 = input("Entrez son horaire du dimanche: ")
                horaire.append(jour1)
                horaire.append(jour2)
                horaire.append(jour3)
                horaire.append(jour4)
                horaire.append(jour5)
                horaire.append(jour6)
                horaire.append(jour7)
                docteurs[i].append(horaire)
                #find = True
                break
            else:
                print("Ses identifiants ne sont pas dans la liste des Docteurs")
                break

#CHRINOVIC MUKEBA



def ajouter_horaire(jour, nomDocteur):
    clear_consol()
    for i in range(len(docteurs)):
        if len(docteurs[i]) >= 8:
            for j in range(len(docteurs[i])):
                if  docteurs[i][1] == nomDocteur:
                    
                    if jour.lower() == "lundi":
                        action = input("Entrez la tâche à ajouter du lundi: ")
                        docteurs[i][7][0].append(action)
                                    
                    elif jour.lower() == "mardi":
                        action = input("Entrez la tâche à ajouter du mardi: ")
                        docteurs[i][7][1].append(action)
                                    
                    elif jour.lower() == "mercredi":
                        action = input("Entrez la tâche à ajouter du mercredi: ")
                        docteurs[i][7][2].append(action)
                                    
                    elif jour.lower() == "jeudi":
                        action = input("Entrez la tâche à ajouter à celle du jeudi: ")
                        docteurs[i][7][3].append(action)
                                    
                    elif jour.lower() == "vendredi":
                        action = input("Entrez la tâche à ajouter à celle du vendredi: ")
                        docteurs[i][7][4].append(action)
                                    
                    elif jour.lower() == "samedi":
                        action = input("Entrez la tâche à ajouter à celle du samedi: ")
                        docteurs[i][7][5].append(action)
                                    
                    elif jour.lower() == "dimanche":
                        action = input("Entrez la tâche à ajouter à celle du dimanche: ")
                        docteurs[i][7][6].append(action)
                                    
                    else:
                        print("Le jour que vous avez saisi n'existe pas !!")
            else:
                print("Ce nom n'est pas dans notre liste")




def changer_horaire(jour, nomDocteur):
    clear_consol()
    for i in range(len(docteurs)):
        if len(docteurs[i]) >= 8:
            for j in range(len(docteurs[i])):
                if nomDocteur == docteurs[i][1]:
                    if jour.lower() == "lundi":
                        action = input("Entrez la nouvelle tâche du lundi: ")
                        docteurs[i][7][0] = action
                                    
                    elif jour.lower() == "mardi":
                        action = input("Entrez la nouvelle tâche du mardi: ")
                        docteurs[i][7][1] = action
                                    
                    elif jour.lower() == "mercredi":
                        action = input("Entrez la nouvelle tâche du mercredi: ")
                        docteurs[i][7][2] = action
                                    
                    elif jour.lower() == "jeudi":
                        action = input("Entrez la nouvelle tâche du jeudi: ")
                        docteurs[i][7][3] = action
                                    
                    elif jour.lower() == "vendredi":
                        action = input("Entrez la nouvelle tâche du vendredi: ")
                        docteurs[i][7][4] = action
                                    
                    elif jour.lower() == "samedi":
                        action = input("Entrez la nouvelle tâche du samedi: ")
                        docteurs[i][7][5] = action
                                    
                    elif jour.lower() == "dimanche":
                        action = input("Entrez la nouvelle tâche du dimanche: ")
                        docteurs[i][7][6] = action
                                    
                    else:
                        print("Le jour que vous avez saisi n'existe pas !!")
