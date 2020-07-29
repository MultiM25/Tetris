import time,tkinter,vue,modele

class Controleur:

    def __init__(self,modele):
        self.__modele = modele
        self.__vue = vue.VueTetris(self.__modele)
        self.__fen = self.__vue.fenetre()
        self.__fen.bind("<Key-Left>",self.forme_a_gauche)
        self.__fen.bind("<Key-Right>",self.forme_a_droite)
        self.__fen.bind("<Key-Down>",self.forme_tombe)
        self.__fen.bind("<Key-Up>",self.forme_tourne)
        self.__delai = 320
        self.joue()
        self.__fen.mainloop()
        
        
    def joue(self):
        """Controleur -> None
        boucle principale du jeu. Fait tomber une forme d’une ligne.
        """
        if not self.__modele.fini() :
            self.affichage()
            self.__fen.after(self.__delai,self.joue)

    def affichage(self):
        n = self.__modele.forme_tombe()
        if n:
            self.__delai = 320
        self.__vue.dessine_terrain()
        self.__vue.dessine_forme(self.__modele.get_coords_forme(),self.__modele.get_couleur_forme())

    def forme_a_gauche(self,event):
        self.__modele.forme_a_gauche()

    def forme_a_droite(self,event):
        self.__modele.forme_a_droite()

    def forme_tourne(self,event):
        self.__modele.forme_tourne()
    
    def forme_tombe(self,event):
        self.__delai = 160
        
if __name__ == "__main__" :
    # création du modèle
    tetris = modele.ModeleTetris()
    # création du contrôleur. c’est lui qui créé la vue
    # et lance la boucle d’écoute des évts
    ctrl = Controleur(tetris)
