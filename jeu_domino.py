import numpy as np
from dominos import Domino
from joueurs import Joueurs
from random import *

## Exécuter ce programme pour lancer le jeu de domino dans la console python ##

class Jeu(Joueurs):
    """classe fille qui hérite de la classe mère 'Joueurs' et donc à accés à ses méthodes et ses attributs"""
    
    def __init__(self,points_max,n_joueurs,computer):
        Joueurs.__init__(self,points_max,n_joueurs,computer)
        self.liste_domino=[]
    
    def affichage_liste_domino(self):
        """affiche la liste en ligne des dominos sur la table"""
        print("")
        print("Les dominos posés sur la table sont:")
        print("")
        L=[]
        for i in range(len(self.liste_domino)):
            L.append(self.liste_domino[i].affichage())
        
        print ("\033[34m{}\033[0m".format(L))

            
        
          
    def premier_joueur(self,n_joueurs):
        """renvoie le joueur qui commence à jouer en premier et le domino qu'il va poser"""
        
        double=[[] for i in range(n_joueurs)]
        maxdouble=[[] for i in range(n_joueurs)] #liste contenant le plus grand double de chaque joueur
        for i in range(n_joueurs):
            for j in range(Joueurs.taille_pioche_joueur(b,i)):
                if Domino.double(Joueurs.pioche_joueurs(b,i)[j]):
                    double[i].append(Joueurs.pioche_joueurs(b,i)[j])

        
        if double[0]!=[] and double[1]!=[]:
            for i in range(n_joueurs):
                max=double[i][0]
                for j in range(len(double[i])):
                    if Domino.plusgrandstrict(double[i][j],max):
                        max=double[i][j]
                maxdouble[i].append(max)
                
            if Domino.plusgrandstrict(maxdouble[0][0],maxdouble[1][0]):
                return(0,maxdouble[0][0])
            else:
                return(1,maxdouble[1][0])
        
            
        elif double[0]==[] and double[1]!=[]:
            return(1,double[1][0])
        
        elif double[0]!=[] and double[1]==[]:
            return(0,double[0][0])
            
        else:
            return(0,Joueurs.pioche_joueurs(b,0)[0]) # si personne n'a de double c'est le premier joueur qui pose son premier domino
              
    
    def permutation1(self,domino):
        """permute un domino"""
        a,b=Domino.tuple_domino(domino)
        dominopermute=Domino(b,a)
        return(dominopermute)
    
    def suivant(self,bool,num_joueur,num_domino,emplacement):  
        """  Fonction récursive:
            bool= true si le joueur peut jouer
             emplacement= 0 si c'est a gauche
                        =1 si c'est a droite
            si bool = true alors la fonction change la liste de domino et la liste de domino du joueur qui joue
            si bool= false alors la la fonction fait piocher le joueur      """

        if bool== True:   #si le joueur peut jouer
            domino=b.pioche_joueur[num_joueur][num_domino]
            if emplacement==0:  #si c'est a gauche
                domino_a_cote=self.liste_domino[0]
                
                if domino.b==domino_a_cote.a:
                    self.liste_domino.insert(0,domino)
                    
                elif domino.a==domino_a_cote.a:
                    self.liste_domino.insert(0,b.permutation1(domino))      #permutation
                    
                else:   
                    print("")                                            #le joueur s'est trompé
                    print("ATTENTION VOUS VOUS ÊTES TROMPÉS DANS LE CHOIX DU DOMINO")
                    print("")
                    num_domino,emplacement=b.interaction(num_joueur,bool)
                    b.suivant(bool,num_joueur,num_domino,emplacement)
                
            else:  #si c'est a droite
                domino_a_cote=self.liste_domino[-1]
                if domino.a==domino_a_cote.b:
                    self.liste_domino.append(domino)
                
                elif domino.b==domino_a_cote.b:
                    self.liste_domino.append(b.permutation1(domino))        #permutation
                    
                else: 
                    print("")                                            #le joueur s'est trompé
                    print("ATTENTION VOUS VOUS ÊTES TROMPÉS DANS LE CHOIX DU DOMINO")
                    print("")
                    num_domino,emplacement=b.interaction(num_joueur,bool)
                    b.suivant(bool,num_joueur,num_domino,emplacement)       #récursivité
                        
            
            b.pioche_joueur[num_joueur].remove(domino)  #suppression du domino dans la liste de domino du joueur
            
        else:                                           #si le joueur ne peut pas jouer
            if len(b.pioche)>1:
                domino_pioche=b.pioche[randint(0,len(b.pioche)-1)]       #il pioche un domino et le met dans sa liste
                b.pioche.remove(domino_pioche)
                b.pioche_joueur[num_joueur].append(domino_pioche)
            elif len(b.pioche)==1:                                                   #si il ne reste plus qu'un element dans la pioche
                domino_pioche=b.pioche[0]
                b.pioche.remove(domino_pioche)
                b.pioche_joueur[num_joueur].append(domino_pioche)
            else:
                return(True)
                
    
    def possible_jouer(self, num_joueur):
        """return true si le joueur peut jouer et false sinon"""
        if b.fini(num_joueur)==True:
            return(False)
            
        domino_gauche,domino_droite=self.liste_domino[0], self.liste_domino[-1]
        chiffre_gauche,chiffre_droite=Domino.tuple_domino(domino_gauche)[0],Domino.tuple_domino(domino_droite)[1]
        for i in range(b.taille_pioche_joueur(num_joueur)):
            domino=b.pioche_joueur[num_joueur][i]
            A,B=Domino.tuple_domino(domino)
            if A==chiffre_gauche or A==chiffre_droite or B==chiffre_gauche or B==chiffre_droite:
                return(True)
        return(False)
    
        
    
    def interaction(self,num_joueur,bool):
        """intéragie avec le joueur avant chaque coup"""
        b.affichage_liste_domino()
        print("")
        print("la pioche du joueur {} est :".format(b.joueurs[num_joueur]))
        print("")
        b.pioche_joueurs2(num_joueur)
        if bool==True:                  #si le joeur peut jouer
            print("")
            num_domino=int(input("quel numéro de domino veux-tu poser sur la table? "))
            emplacement=int(input("Ou veux tu le placer? Gauche (0)? Droite (1) ? "))
            return(num_domino,emplacement)
        else:                           #si il ne peut pas
            return(-1,-1)
            
            
    def ordinateur(self,bool):
        """méthode qui choisit le domino que l'ordinateur va placer et où il va le placer"""
        b.affichage_liste_domino()
        print("")
        print("la pioche du joueur {} est :".format(b.joueurs[1]))
        print("")
        b.pioche_joueurs2(1)
        if bool==True:
            liste_domino_possible=[]
            
            domino_gauche,domino_droite=self.liste_domino[0], self.liste_domino[-1]
            chiffre_gauche,chiffre_droite=Domino.tuple_domino(domino_gauche)[0],Domino.tuple_domino(domino_droite)[1]
            for i in range(b.taille_pioche_joueur(1)): #on regarde dans la pioche de l'ordinateur (joueur 1)
                domino=b.pioche_joueur[1][i]
                A,B=Domino.tuple_domino(domino)
                if A==chiffre_gauche or B==chiffre_gauche:   # On regarde si on peut placer le domino à gauche de la liste des dominos placés sur la table
                    emplacement=0
                    liste_domino_possible.append((domino,emplacement,Domino.somme(domino)))
                elif A==chiffre_droite or B==chiffre_droite:       # On regarde si on peut placer le domino à droite de la liste des dominos placés sur la table
                    emplacement=1
                    liste_domino_possible.append((domino,emplacement,Domino.somme(domino)))
            
            max_somme=0
            for i in range(len(liste_domino_possible)):         # On récupère le plus grand domino de la pioche du joueur
                k=liste_domino_possible[i][2]
                if k>max_somme:                 
                    max_somme=k
                    domino=liste_domino_possible[i][0]
                    emplacement=liste_domino_possible[i][1]
                    
            num_domino=b.pioche_joueurs(1).index(domino)
            print("")
            print("L'ordinateur pose le domino: {}".format(domino.affichage()))
            print("")
           
            return(num_domino,emplacement)
        else:
            return(-1,-1)
        
    def fini(self,num_joueur):
        """renvoie true si le jeu est fini et false sinon
           pioche vide&joueur 0 peut pas jouer
           pioche vide&joueur 1 peut pas jouer   
           pioche jouer1 vide
           pioche joueur2 vide                                  
                                                """
         
        if num_joueur==0:                   #joueur a suivre
            num_joueura=1
        else:
            num_joueura=0     
                                           
        if b.taille_pioche==0: # condition d'arret
            return(True)
        
        elif b.taille_pioche_joueur(0)==0:      # condition d'arret
            return(True)
            
        elif b.taille_pioche_joueur(1)==0:       # condition d'arret
            return(True)
        else:
            return(False)
    
    def points(self, num_joueur):
        """renvoie le nombre de points du joueur num_joueur"""
        x=0
        for i in range(b.taille_pioche_joueur(num_joueur)):
            A,B=b.pioche_joueurs_tuple(num_joueur)[i]
            x=x+A+B
        return(x)
        
        
            
    def vainqueur(self):
        """affiche le vainqueur de la partie"""
        if b.taille_pioche==0:
            points0,points1=b.points(0),b.points(1)  #nombre de points des deux joueurs
            if points0>points1:
                print("")
                print ("\033[36mLE VAINQUEUR EST {}  \033[0m".format(b.joueurs[1]))
            elif points1>points0:
                print("")
                print ("\033[36mLE VAINQUEUR EST {}  \033[0m".format(b.joueurs[0]))
            else:
                print("")
                print("MATCH NUL, AUCUN VAINQUEUR")       #match nul si ils ont le même nombre de points
        
        if b.taille_pioche_joueur(0)==0:
            print("")
            print("LE VAINQUEUR EST {}  ".format(b.joueurs[0]))
            
        if b.taille_pioche_joueur(1)==0:
            print("")
            print("LE VAINQUEUR EST {}  ".format(b.joueurs[1]))
        


    def jeu_final(self,n_joueurs,computer):
        num_joueur,domino=b.premier_joueur(n_joueurs)
        
        if computer==True and num_joueur==1:
            print("")
            print("C'est l'ordinateur qui commence la partie car il a le plus grand double. Il pose alors ce domino.")
            print("")
        
        else:
            print("")
            print("Le joueur qui commence la partie est : {}  et tu es obligé de poser ton plus grand double".format(b.joueurs[num_joueur]))
            print("")
            
        self.liste_domino.append(domino)
        b.pioche_joueur[num_joueur].remove(domino)
        b.affichage_liste_domino()
        #ca ne joue plus quand soit: la pioche du joueur 0 est vide, quand la pioche du joueur 1 est vide ou quand la pioche est vide et que le joueur à suivre ne peut pas joueur.
        k=1
        while b.fini(num_joueur)==False:

            if num_joueur==0:                   #changement de joueur
                num_joueur=1
            else:
                num_joueur=0
            

            bool=b.possible_jouer(num_joueur) 
            
            if bool==True and num_joueur==1 and computer==True:
                print("------------------------------------")
                print("\033[31m------------------------------------\033[0m")
                print("\033[31mTOUR SUIVANT {}: L'ordinateur peut jouer\033[0m".format(k))
                print("\033[31m------------------------------------\033[0m")
           
            elif bool==False and num_joueur==1 and computer==True:
                print("\033[31m------------------------------------\033[0m")
                print("\033[31mTOUR SUIVANT {}: L'ordinateur ne peut pas jouer\033[0m".format(k))
                print("\033[31m------------------------------------\033[0m")
                
            elif bool==True:
                print("\033[31m------------------------------------\033[0m")
                print("\033[31mTOUR SUIVANT {}: Le joueur {} peut jouer\033[0m".format(k,b.joueurs[num_joueur]))
                print("\033[31m------------------------------------\033[0m")
                
            else:
                print("\033[31m------------------------------------\033[0m")
                print("\033[31mTOUR SUIVANT {}: Le joueur {} ne peut pas jouer, il doit piocher\033[0m".format(k,b.joueurs[num_joueur]))
                print("\033[31m------------------------------------\033[0m")
       
                                                                    
            if computer==False or (computer==True and num_joueur==0):                                                        
                num_domino,emplacement=b.interaction(num_joueur,bool)

            else:
                num_domino,emplacement=b.ordinateur(bool)
                
            
            b.suivant(bool,num_joueur,num_domino,emplacement)
            k=k+1
        b.vainqueur()
        
            
## L'exécution de ce programme permet de jouer au jeu de domino dans la console python

if __name__ == "__main__":
    
    question=int(input("Si tu veux jouer en 1 contre 1 tape 0 et si tu veux jouer contre l'ordinateur tape 1 : "))
    if question==0:
        computer=False
    elif question==1:
        computer=True
        
    points_max,n_joueurs=6,2
    
    b=Jeu(points_max,n_joueurs,computer)
    b.jeu_final(n_joueurs,computer)




