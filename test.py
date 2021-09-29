import numpy as np
import unittest
from dominos import Domino
from jeu_domino import Jeu
from joueurs import Joueurs

computer=False
joueur=Joueurs(6,2,computer)

class Mytest(unittest.TestCase):
    """classe qui permet de tester certaines méthodes des différentes classes"""
    
    
    def test_egalite(self):
        """test si 2 dominos sont égaux"""
        
        self.assertTrue(Domino.egalite(Domino(2,3),Domino(3,2)))
        self.assertFalse(Domino.egalite(Domino(4,3),Domino(3,1)))
        
    def test_suite(self):
        """test si 2 dominos peuvent être placés à la suite"""
        
        self.assertTrue(Domino.suite(Domino(6,3),Domino(3,1)))
        self.assertFalse(Domino.suite(Domino(6,4),Domino(3,7)))
    
    def test_double(self):
        """test si un domino est double"""
        
        self.assertTrue(Domino.double(Domino(6,6)))
        self.assertFalse(Domino.double(Domino(5,6)))
        
    def test_plusgrandstrict(self):
        """vérifie qu'un domino est bien plus grand"""
        
        self.assertTrue(Domino.plusgrandstrict(Domino(6,6),Domino(5,6)))
        self.assertFalse(Domino.plusgrandstrict(Domino(2,6),Domino(5,6)))
        
    def test_permutation1(self):
        """vérifie la permutation de deux dominos (peu importe le premier domino dans permutation"""
        self.assertTrue(Domino.tuple_domino(Jeu.permutation1(Domino(4,6),Domino(3,6)))==(6,3))
        self.assertFalse(Domino.tuple_domino(Jeu.permutation1(Domino(4,6),Domino(5,6)))==(4,3))
        
    def test_somme(self):
        """test la méthode du calcul de la somme des points d'un domino"""
        self.assertTrue(Domino.somme(Domino(6,1))==7)
        self.assertFalse(Domino.somme(Domino(2,3))==2)

    def test_taille_pioche(self):
        """test la méthode de la taille de la pioche dans la classe joueur"""
        self.assertTrue(joueur.taille_pioche()==14)
        
    def test_taille_pioche_joueurs(self):
        """test la méthode de la taille de la pioche des joueurs"""
        self.assertTrue(joueur.taille_pioche_joueur(0)==7)
        self.assertFalse(joueur.taille_pioche_joueur(1)==6)
        
    def test_init1_class_joueur(self):
        """test si les deux joueurs ont le même nombre de dominos initialement"""
        self.assertTrue(len(joueur.pioche_joueur[0])==len(joueur.pioche_joueur[1]))
    
    def test_init2_class_joueur(self):
        """test si tous les dominos ne sont présents qu'une seule fois dans le jeu (si la suppression des dominos marche correctement une fois qu'on les a enlevé de la pioche pour le donner à un joueur"""
        bool=True
        for i in range(joueur.taille_pioche()):
            domino=joueur.pioche[i]
            if domino in joueur.pioche_joueur[0] or domino in joueur.pioche_joueur[1]:
                bool=False
        self.assertTrue(bool==True)

    
    
if __name__ == '__main__':
    unittest.main()
            