                  # *** Reading and Writing To a Text File ***

#105
fichier=open("nombres.txt","w")
fichier.write("23, ")
fichier.write("45, ")
fichier.write("11, ")
fichier.write("3, ")
fichier.write("59, ")
fichier.close()


#106
fichier=open("noms.txt","w")
fichier.write("Odson\n")
fichier.write("Saintilson\n")
fichier.write("Sandy\n")
fichier.write("Esther\n")
fichier.write("Taïna\n")
fichier.close()


#107
fichier=open("noms.txt","r")
print(fichier.read())
fichier.close()


#108
fichier=open("noms.txt","a")
nm=input("Entrer un nouveau nom : ")
fichier.write(nm + "\n")
fichier.close


fichier=open("noms.txt","r")
print(fichier.read())
fichier.close


#109
print("'c' Pour Créer un nouveau fichier")
print("'af' Pour afficher le fichier")
print("'aj'pour ajouter un nouveau élément dans le fichier")
choix=int(input("Faites votre choix 'c','af' ou 'aj': "))
if choix=="c": 
  matiere=input("Entrer une matière : ")
  fichier=open("matiere.txt","r")
  fichier.write(matiere+"\n")
elif choix=="af": 
  fichier=open("martiere.txt","r")
  print(fichier.read())
elif choix=="aj":
  fichier=open("mariere.txt","a")
  matiere=input("Entrer une matière : ")
  fichier.write(matiere + "\n")
  fichier.close()
  fichier=open ("matiere.txt","r")
  print(fichier.read())
else:
  print("choix invalide!")


#110
fichier=open("noms.txt","r")
print(fichier.read())
fichier.close()

fichier=open("noms.txt","r")
chnom=input("Entrer un qui vient de la liste: ")
for ligne in fichier:
  if ligne != chnom:
    fichier=open("noms2.txt","a")
    nven=ligne
    fichier.write(nven)
    fichier.close()
  
fichier.close()