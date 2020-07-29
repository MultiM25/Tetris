import tkinter
import modele

DIM = 30
COULEURS = ["red","pink","purple","green","blue","yellow","orange","dark grey","black"]
class VueTetris :
    
    
    def __init__(self,modele):
        self.__modele = modele
        fenetre = tkinter.Tk()
        self.__fenetre = fenetre
        fenetre.title("Tetris")
        
        btn_quitter = tkinter.Button(fenetre,text="Au revoir", command = fenetre.destroy)
        btn_quitter.pack(side='right')
        frame= tkinter.Frame(self.__fenetre , bg ='white')
        frame.pack()
        self.__can_terrain = tkinter.Canvas(self.__fenetre,width=self.__modele.get_largeur() * DIM,height= self.__modele.get_hauteur() * DIM)
        self.__can_terrain.pack(side='left')
        
        self.__les_cases = []
        for i in range(self.__modele.get_hauteur()):
            les_cases =[]
            for j in range (self.__modele.get_largeur()):
                elt = self.__can_terrain.create_rectangle(j*DIM,i*DIM,(j+1)*DIM,(i+1)*DIM,outline='grey',fill=COULEURS[self.__modele.get_valeur(i,j)])
                les_cases.append(elt)
            self.__les_cases.append(les_cases)
        
        
        
    def fenetre(self):
        return self.__fenetre
    
    def dessine_case(self,i,j,coul):
        self.__can_terrain.itemconfig(self.__les_cases[i][j],fill=COULEURS[coul])
    
    def dessine_terrain(self):
        for lignes in range(0,self.__modele.get_hauteur()):
            ligne=[]
            for colonne in range(0,self.__modele.get_largeur()):
                self.__can_terrain.itemconfigure(self.__les_cases[lignes][colonne],fill=COULEURS[self.__modele.get_valeur(lignes,colonne)])
                
        
    def dessine_forme(self,coords,couleur):
        for i in coords:
            self.dessine_case(i[1],i[0],couleur)
        

