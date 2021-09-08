                            # *** 2D list and Dictinnaries ***

#096
liste=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]


#097
liste=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
ligne=int(input("Sélectionner une ligne: "))
col=int(input("Sélectionner une colonne: "))
print(liste [ligne] [col])


#098
liste=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
ligne=int(input("Sélectionner une ligne: "))
print(liste[ligne])
nv=int(input("Entrer un nouveau nombre : "))
liste[ligne].append(nv)
print(liste[ligne])


#099
liste=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
ligne=int(input("Sélectionner une ligne: "))
print(liste[ligne])
col=int(input("sélectionner une colonne : "))
print([ligne][col])
modifier=input("Voulez-vous modifier la valeur ? (oui / non)")
if modifier == "oui":
  nv=int(input("Entrer une nouvelle valeur : "))
liste[ligne][col]=nv
print(liste[ligne])


#100
ventes={"john":{"N":3056,"S":8463,"E":8441, "W":2694},"Tom":{"N":4832,"S": 6786,"E":5820, "W":1859},"Anne":{"N":5239,"S": 4802,"E":5820,"W":1859},"Fiona":{"N":3904,"S":3645,"E":8821,"W":2451}}


#101
ventes={"john":{"N":3056,"S":8463,"E":8441, "W":2694},"Tom":{"N":4832,"S": 6786,"E":5820, "W":1859},"Anne":{"N":5239,"S": 4802,"E":5820,"W":1859},"Fiona":{"N":3904,"S":3645,"E":8821,"W":2451}}
personne=input("Entrer le nom d'un client: ")
region=input("Sélectionner une région: ")
print(ventes[personne][region])
nd=input("Entrer une nouvelle donnée: ")
ventes[personne][region]=nd
print(ventes[personne])


#102
list={}
for i in range(0,5): 
  nom=input("Entrer le nom: ")
  age=input("Entrer votre âge: ")
  chass=int(input("Entrer votre pointure: "))
  list[nom]={"Âge":age,"Pointure":chass}

poser=input("Entrer un nom: ")
print(list[poser])


#103
list={}
for i in range(0,4):
  nom=input("Entrer le nom: ")
  age=input("Entrer votre âge: ")
  chass=int(input("Entrer votre pointure: "))
  list[nom]={"Âge":age,"Pointure":chass}

for nom in list:
  print((nom),list[nom] ["Âge"])
  

#104
list={}
for i in range(0,4):
  nom=input("Entrer le nom: ")
  age=input("Entrer votre âge: ")
  chass=int(input("Entrer votre pointure: "))
  list[nom]={"Âge":age,"Pointure":chass}
  
supp=input("Qu'est-ce que vous voulez supprimer à partir de la liste? ")
del list[supp]

for nom in list:
  print((nom),list[nom]["Âge"],list[nom],["pointure"])