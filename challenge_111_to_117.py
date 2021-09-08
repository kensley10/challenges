                # *** Reading and Writing to a .csv File ***

#111
import csv
fichier=open("livre.csv","w")
nven="La famille pitite-caille,Justin Lhérisson,1904\n"
fichier.write(str(nven))
nven="Thémistocle Épaminondas labasterre, Frédéric Marcelin,1910\n"
fichier.write(str(nven))
nven="Zoune chez sa ninaine,Justin Lhérisson,1901\n"
fichier.write(str(nven))
nven="Gouveurneur de la rosée, Jacques Roumain,1950\n"
fichier.write(str(nven))
fichier.close()



#112
import csv
fichier=open("livre.csv","a")
titre=input("Entrer un titre: ")
auteur=input("Entrer l'auteur: ")
annee=input("Entrer l'année de publication : ")
nven=titre + "," + auteur + "," + annee + "\n"
fichier.write(str(nven))
fichier.close()

fichier = open("livres.csv","r")
for ligne in fichier:
  print(ligne)
fichier.close()


#113
import csv
qte=int(input("Combien de livre voulez-vous ajouter à la liste? "))
fichier=open("livre.csv",'a')
for x in range(0,qte):
  titre= input("Entrer un titre : ")
  auteur=input("Entrer l'auteur : ")
  annee=input ("L'année de publication : ")
  

  nven=titre+","+auteur+","+annee+"\n"
  fichier.write(str(nven))
fichier.close()

recherche_auteur=input("Entrer le nom de l'auteur que vous recherchez : ")

fichier=open("livres.csv","r")
compteur=0
for ligne in fichier :
  if recherche_auteur in str(ligne):
    print(ligne)
    compteur=compteur+1
if compteur == 0:
  print("Nous n'avons aucun livres qui correspond à cet auteur")
    
fichier.close()



#114
import csv

debut=int(input ("Entrer une année de départ: "))
fin =int(input("Entrer une année de fin: "))


fichier=list(csv.reader(open("livres.csv")))

rep=[]
for ligne in fichier:
  rep.append(ligne)
  
q=0
for ligne in rep:
  if int(tmp[q] [2]) >= debut and int (tmp[q] [2]) <=fin :
    print(rep[q])
  q=q+1


#115
import csv
fichier=open("livres.csv","r")
q=0
for ligne in fichier:
  afficher="Ligne: "+str(q)+"-"+ligne
  print(afficher)
  q=q+1


#116

import csv
fichier=list(csv.reader(open("livres.csv")))
liste_livre=[]
for ligne in fichier :
  liste_livre.append(ligne)

q=0
for ligns in liste_livre: 
  afficher=q,liste_livre[q]
  print(afficher)
  q=q+1
sup=int(input("Entrer la ligne à supprimer: "))
del liste_livre[sup]
  

q=0
for ligne in liste_livre: 
  afficher=q,liste_livre[q]
  print(afficher)
  q=q+1
  
mod=int(input("Entrer le numéro de la ligne à modifier : "))
q=0

for ligne in liste_livre[mod]: 
  afficher=q,liste_livre [mod] [q]
  print(afficher)
  q=q+1
  
partie=int("Quelle partie voulez-vous modifier? ")
nvin=input("Entrer une nouvelle information: ")
liste_livre[mod][partie]=nvin
print(liste_livre[mod])

fichier=open("livres.csv",'w')
q=0
for ligne in liste_livre: 
  nven=liste_livre[q][0] + "," + liste_livre [q][1] + "," + liste_livre[q][2]+"\n"
  fichier.write(nven)
  q=q+1
fichier.close()
  
  
#117

import csv
import random

score=0
nom=input("Quel est vôtre nom: ")
q1_num1=random.randint(10,50)
q1_num2=random.randint(10,50)

question1=str(q1_num1)+"+"+str(q1_num2)+"="
rep1=int(input(question1))
rea1=q1_num1+q1_num2
if rep1== rea1:
  score=score+1
q2_num1=random.randint(10,50)
q2_num2=random.randint(10,50)
question2=str(q2_nun1)+"+"+str(q2_num2)+"="
rep2=int(input(question2))
rea2=q2_num1+q2_num2
if rep2 == score + 1:

fichier=open("question.csv","a")
nven=nom+","+question1+","+str(rep1)+","+question2+","+str(rep2)+","+str(score)+"\b"
fichier.write(str(nven))

fichier.close()