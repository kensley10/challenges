                              # *** Numeric Arrays ***

#088
from array import *

valeur= array('i',[])

for i in range(0,5):
  val=int(input("Entrer un nombre: "))
  valeur.append(val)
valeur=sorted(valeur)
valeur.reverse()

print(valeur)


#089
from array import *
import random

valr=array("i",[])

for i in range (0,5):
  nb=random.randint(1,100)
  valr.append(nb)

for i in nb:
  print(i)
  
  
#090
from array import *

valr= array("i",[])

while len (valr) < 5:
  nb=int(input("Entrer un nombre entre 10 et 20: "))
  if nb >= 10 and nb <= 20:
    valr.append(nb)
  else:
    print("En déhors de l'ensemble")

for i in valr:
  print(i)
  
  
#091
from array import *
val=array ("i",[5,7,9,2,9])

for x in val:
  print(x)
  
nb=int(input("Entrer un nombre: "))

if val.count(nb) == 1:
    print(nb,"est dans la liste qu'une fois")
else:
    print(nb,"est dans la liste",val.count(nb),"fois")


#092
from array import *
import random 

nbre1= array ("i",[])
nbre2=array("i",[ ])

for x in range(0,3):
  val= int(input("Entrer un nombre: "))
  nbre1.append(val)
  
for x in range(0,5): 
  val=random.randint(1,100)
  nbre2.append(val)
  
nbre1.extend(nbre2)
nbre1=sorted(nbre1)

#093
from array import *
val = array("i",[])
 
for i in range(0,5):
   nb=int(input("Entrer un nombre: "))
   val.append(nb)
   
val= sorted(val)

for x in val:
  prit(x)
  
nb=int(input("Sélectionner un nombre qui vient du tableau: ")

if nb in val:
  val.remove(nb)
  nb1=array("i",[])
  nb1.append(nb)
  print("val")
  print(nb1)
else:
  print("Ce n'est pas un valeur du tableau")
  
#094
from array import *
val=array("i",[4,6,8,2,5])

for x in val:
  print(i)
  
nb=int(input("sélectionner un de ces nombres : "))

ess_a_nou=True
while ess_a_nou=True:
  if nb in val:
    print("This is in position",val.index(nb)
  else:
    print("Il n'est pas dans le tableau")
    nb=int(input("Sélectionner l'un de ces nombres: "))
 
#095
from array import *
import math

val= array("f",[34.75,27.23,99.58,45.26,28.65])
ess_a_nou=True:
  while ess_a_nou== True:
    nb=int(input("Entrer un nombre entre 2 et 5: "))
    if nb < 2 or nb > 5:
      print("valeur incorrect, essayer à nouveau.")
    else:
      ess_a_nou== False
      
  for x in range(0,5):
    bbb=val[x]/nb
    print(round(bbb,2))