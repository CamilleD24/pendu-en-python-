# pendu python (projet 1)
import random

nom = input("tapez votre nom: ")
print ("Bonjour", nom, "!" "Prêt(e) à jouer?!")

with open(r".\words.txt", "r") as files:
    text = files.read()
    words = list(map(str, text.split()))
    mot = random.choice(words)
    print(mot)
 

tentative = -1
lettrecaché = ["_" for _ in mot ]
Lettretesté = []
pendu = [r""" 
   
 |__________|  
        `
""", r"""

 __ 
 |          | 
 |__________| 
        `
""", r"""
   
   
  _|_ 
 |   |______ 
 |          | 
 |__________| 
        `
""", r"""
   
     ____ 
   |          
   |          
   |        
   |   
   |   
  _|_ 
 |   |______ 
 |          | 
 |__________| 
        `
""", r"""
   
      ____ 
   |    |       
   |    o       
   |        
   |    
   |  
  _|_ 
 |   |______ 
 |          | 
 |__________| 
        ` 
""", r"""
   
     ____ 
   |    |       
   |    o       
   |   / \      
   |    
   |   
  _|_ 
 |   |______ 
 |          | 
 |__________|
""", r"""
   
     ____ 
   |    |       
   |    o       
   |   /|\      
   |    | 
   |  
  _|_ 
 |   |______ 
 |          | 
 |__________|
""", r"""
      ____ 
   |    |       
   |    o       
   |   /|\      
   |    | 
   |   / \ 
  _|_ 
 |   |______ 
 |          | 
 |__________|
"""]

print (" ".join(lettrecaché))





while tentative < 7 and list(mot) != lettrecaché:
    lettre = input("une lettre: ")

    if not lettre.isalpha():
        print("merci de choisir une lettre")
        continue

    if len(lettre) != 1:
        print(" Veuillez mettre qu'une seule lettre")
        continue

    if lettre in Lettretesté:
        print("veuillez choisir une autre lettre")
        continue

    for i in range(len(mot)):
        if mot[i] == lettre :
            lettrecaché[i] = lettre
    print(''.join(lettrecaché))
        
    if not lettre in mot:   
        tentative = tentative + 1
        Lettretesté.append(lettre)
        print(pendu[tentative])

    print (Lettretesté)

if list(mot) == lettrecaché:
    print("Victoire, bravo", nom )

else:
    print("Défaite, dommage une prochaine fois", nom, "!!")
    print(mot)






