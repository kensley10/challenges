                        # *** More String Manipulation ***

#080
prenom = input("Saisir votre prénom: ")
print("Il y a ", len(prenom),"caractères dans votre prenom")
nom = input("saisir votre nom: ")
print("Il y a", len(nom),"caractères dans votre nom")
nom_complet= prenom+""+nom
print("votre nom complet est",nom_complet)
print("il a",len(nom_complet),"caractère dans votre nom complet")


#081
matiere = input("Entrer votre favorite matière: ")
for lettre in matiere:
  print(lettre,end="-")
  
  
#082
poeme = "Si votre ramage se rapporte à votre plumage vous êtes le phénix des hôtes de ces bois"
debut= int(input("Entrer le nombre de départ: "))
fin= int(input("Entrer le nombre de fin: "))
print(poeme[debut:fin])


#083
msg=input("Entrer un message en majuscule : ")
ess_a_nouv=False
while ess_a_nouv==False:
  if msg.isupper(): 
    print("Merci !")
    ess_a_nouv = True
  else:
    print("Essayer à nouveau")
    msg=input("Entrer un message en majuscule")
    
#084    
codepostal=input("Entrer votre code postal: ")
debut=codepostal[0:2]
print(debut.upper())

#085
nom=input("Entrer votre nom : ")
compteur=0
nom=nom.lower()
for lettre in nom:
  if lettre == "a" or lettre =="e" or lettre == "o" or lettre =="u":
    compteur= compteur+1
    print("Les voyelles vaut",compteur)
    
#086
mp1=input("Entrer un mot de passe: ")
mp2=input("Entrer le à nouveau: ")
if mp1==mp2:
  print("Merci !")
elif mp1.lower== mp2.lower():
  print("il ne s'agit plus du même cas")
else:
  print("non valide")
 
  
#087
mot=input("Entrer un mot: ")
longueur=len(mot)
num=1
for i in mot:
  position = longueur - num
  lettre= mot[position]
  print(lettre)
  num=num+1