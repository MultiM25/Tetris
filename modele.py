from random import randint
LES_FORMES = [[(-1,1),(-1,0),(0,0),(1,0)],[(0,-1),(0,0),(0,1),(0,2)],[(0,0),(1,0),(1,1),(0,1)],[(-1,0),(0,0),(0,-1),(1,-1)],[(-1,0),(0,0),(0,1),(1,1)],[(-1,0),(0,0),(0,-1),(1,0)],[(-1,0),(0,0),(1,0),(1,1)]]

class ModeleTetris:

    def __init__(self,lig=24,col=14):
        self.__haut = lig
        self.__larg = col
        self.__base = 3
        terrain = []
        for i in range(self.__haut):
            ligne = []
            if  0 <= i and i <= self.__base :
                for i in range(self.__larg):
                    ligne.append(-2)
                terrain.append(ligne)
            else :
                for i in range(self.__larg):
                    ligne.append(-1)
                terrain.append(ligne)
        self.__terrain = terrain
        self.__forme = Forme(self)

    def get_largeur(self):
        return self.__larg

    def get_hauteur(self):
        return self.__haut
    
    def get_valeur(self,lig,col):
        return self.__terrain[lig][col]

    def est_occupe(self,lig,col):
        return not self.get_valeur(lig,col) < 0

    def fini(self):
        for j in range(self.__larg):
            if self.est_occupe(self.__base,j):
                return True
        return False

    def ajoute_forme(self):
        for i in self.__forme.get_coords():
            self.__terrain[i[1]][i[0]] = self.__forme.get_couleur()

    def forme_tombe(self):
        if not self.__forme.tombe() :
            return False
            
        else :
            self.ajoute_forme()
            self.__forme = Forme(self)
            return True

    def get_couleur_forme(self):
        return self.__forme.get_couleur()

    def get_coords_forme(self):
        return self.__forme.get_coords()

    def forme_a_gauche(self):
        self.__forme.a_gauche()

    def forme_a_droite(self):
        self.__forme.a_droite()

    def forme_tourne(self):
        self.__forme.tourne()
        
class Forme:
    
    def __init__(self,modele):
        forme = randint(0,len(LES_FORMES)-1)
        self.__modele = modele
        self.__couleur = forme
        self.__forme = LES_FORMES[forme]
        self.__x0 = randint(2,self.__modele.get_largeur()-2)
        self.__y0 = 0
    
    def get_couleur(self):
        return self.__couleur
    
    def get_coords(self):
        self.__liste_coord=[]
        for i in range (0,len(self.__forme)) :
            self.__liste_coord.append(((self.__forme[i][0])+(self.__x0),(self.__forme[i][1])+(self.__y0)))
        return self.__liste_coord
    
    def collision(self):
        for couple_coord in self.get_coords():
            if couple_coord[1]+1 == self.__modele.get_hauteur():
               
                return True
            if  (self.__modele.est_occupe(couple_coord[1]+1,couple_coord[0]) ):
                return True
        return False

    def tombe(self):
        if not(self.collision()):
            self.__y0 += 1
            return False
        return True 

    def position_valide(self):
        coords = self.get_coords()
        for i in coords:
            if not(0 <= i[0]) and not(i[0] < 14):
                if self.__modele.est_occupe(i[0],i[1]):
                    return False
        return True
    
    def a_gauche(self):
        self.__x0 -= 1
        if not self.position_valide():
            print(lol)
            self.__x0 += 1

    def a_droite(self):
        self.__x0 += 1
        if not self.position_valide():
            self.__x0 -= 1
            
    def tourne(self):
        forme_prec = self.get_coords()
        coord = []
        for i in self.__forme:
            x = -i[1]
            y = i[0]
            coord.append((x,y))
        self.__forme = coord
        if not(self.position_valide()):
            self.__forme = forme_prec
