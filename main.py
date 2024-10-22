from tkinter import * 


class CentreFormation:
    def __init__(self,nom,addresse):
        self.nom = nom
        self.adresse=addresse
        self.sessions = []
    def ajout_session(self,sess):
        self.sessions.append(sess) 
        return True
    def recherche_formation_num_session(self,num):
        for session in self.sessions:
          if(session.num == num):
              return session.affiche_info()
    def recherche_formation_id_formateur(self,id):
        for session in self.sessions:
          if(session.formateur.id == id):
              return session.affiche_info()
          
    def recherche_formation_nb_jour_supnb(self,nb_jours):
        for session in self.sessions:
          if(session.nb_jours >= nb_jours ):
              return session.affiche_info()
    def recherche_stagiaire_par_parcours(self, num,mot_cle):
        for session in self.sessions:
           if(session.num == num):
               for stagiaire in session.stagiaires:
                    if(mot_cle.lower() in stagiaire.parcours.lower()):
                       return f'{stagiaire.id}   {stagiaire.parcours}'

    def recherche_f_par_financeur(self,financeur):
        for session in self.sessions:
            if(session.financeur.nom.lower() == financeur.lower()):
             return session.affiche_info() +" financeur :"+ financeur
    def recherche_f_par_mot_cle(self,mot_cle):
        for session in self.sessions:
            if(mot_cle.lower() in session.nom.lower()):
                return session

    def nombre_de_session(self):
        return len(self.sessions)
    def formations(self):
        tab = []
        for session in self.sessions:   
            # return == un break      
            tab.append(session.nom)
        return tab
    def nb_moyenne_stagiaire_parsession(self):
           return self.nbr_stagieres()/self.nombre_de_session()

    def nbr_stagieres(self):
        nb_stagiaire = 0
        for session in self.sessions:
             nb_stagiaire += len(session.stagiaires)
        return nb_stagiaire
    def nbr_stagiere_par_formation(self,nom):
        for session in self.sessions:
            if( session.nom.lower() == nom.lower()):
                return len(session.stagiaires)
class Personne:
    def __init__(self,id,email):
        self.id = id
        self.email = email
    def affiche_info(self):
        return f'{self.id}  {self.email}'
class Administrateur(Personne):
    def __init__(self, id, email,post):
        super().__init__(id, email)
        self.post = post
    def affiche_info(self):
        return super().affiche_info() +" "+ self.post
    
class Formateur(Personne):
    def __init__(self, id, email,specialite):
        super().__init__(id, email)
        self.specialite = specialite
    def affiche_info(self):
        return super().affiche_info() +" "+ self.specialite
    

class Stagiaire(Personne):
    def __init__(self, id, email,parcours):
        super().__init__(id, email)
        self.parcours = parcours
    def affiche_info(self):
        return super().affiche_info() +" "+ self.parcours
class Financeur:
    def __init__(self,nom):
        self.nom = nom

class SessionDeFormation:
    max = 8
    def __init__(self,nom,num,formateur,presentiel, nb_jours,financeur):
        self.nom = nom
        self.num = num
        self.formateur = formateur
        self.stagiaires = []
        self.presentiel = presentiel
        self.nb_jours = nb_jours
        self.financeur = financeur
    def ajouter_stagiaire(self,stagiaire):
        if (len(self.stagiaires) < SessionDeFormation.max):
            self.stagiaires.append(stagiaire)
            return "Tout va bien ;)"
        else: 
            return "Vous ne pouvez pas ajouter un nouveau stagiaire le nombre limité de stagiaire dans une session est 8 "    
    def supprimer_stagiaire(self,id_stagiaire):
         for stagiaire in self.stagiaires:
             if(stagiaire.id == id_stagiaire):
                 self.stagiaires.remove(stagiaire)
                 return True
             else:
                 return False
    def affiche_info(self):
        return f'session {self.nom} numero {self.num} avec le formateur {self.formateur.id} distanciel = {self.presentiel} dure {self.nb_jours} jours le nombre de  stagiaire est :{len(self.stagiaires)}'
    def __str__(self):
       return f'session {self.nom} numero {self.num} avec le formateur {self.formateur.id} distanciel = {self.presentiel} dure {self.nb_jours} jours le nombre de  stagiaire est :{len(self.stagiaires)}'  
 

m2i =  CentreFormation("M2i formation","Mont saint aignan")
stagiaire_1 = Stagiaire("123","123@M2iformation.fr","Master Data")
stagiaire_2 = Stagiaire("124","123@M2iformation.fr","Master Finance & data")
stagiaire_3 = Stagiaire("125","123@M2iformation.fr","Master Data")
stagiaire_4 = Stagiaire("126","123@M2iformation.fr","Master Statistiques")
stagiaire_5 = Stagiaire("127","123@M2iformation.fr","Master Data")
stagiaire_6 = Stagiaire("128","123@M2iformation.fr","Master Finance & data")
stagiaire_7 = Stagiaire("129","123@M2iformation.fr","Master Data")
stagiaire_8 = Stagiaire("120","123@M2iformation.fr","Master Statistiques")
stagiaire_9 = Stagiaire("1211","123@M2iformation.fr","Master Data")
stagiaire_10 = Stagiaire("1222","123@M2iformation.fr","Master Finance & data")
stagiaire_11 = Stagiaire("1233","123@M2iformation.fr","Master Data")
stagiaire_12 = Stagiaire("1244","123@M2iformation.fr","Master Statistiques")


formateur_1 = Formateur("201","prof1@m2iformation.fr","Python")
formateur_2 = Formateur("202","prof2@m2iformation.fr","Java")
formateur_3 = Formateur("203","prof3@m2iformation.fr","Java")
formateur_4 = Formateur("204","prof4@m2iformation.fr","PHP")
financeur_1 = Financeur("Orange")
financeur_2 = Financeur("Region")

session_1 = SessionDeFormation("Python pour l'analyse des donnee ","1",formateur_1,False,30,financeur_1)
print(session_1.affiche_info())
session_1.ajouter_stagiaire(stagiaire_1)
session_1.ajouter_stagiaire(stagiaire_2)
session_1.ajouter_stagiaire(stagiaire_3)
print(session_1.affiche_info())

session_2 = SessionDeFormation("Java","2",formateur_3,True,100,financeur_2)
session_2.ajouter_stagiaire(stagiaire_1)
session_2.ajouter_stagiaire(stagiaire_2)
session_2.ajouter_stagiaire(stagiaire_3)
session_2.ajouter_stagiaire(stagiaire_4)
session_2.ajouter_stagiaire(stagiaire_5)
session_2.ajouter_stagiaire(stagiaire_6)
session_2.ajouter_stagiaire(stagiaire_7)
print(session_2.ajouter_stagiaire(stagiaire_8))
print(session_2.ajouter_stagiaire(stagiaire_9))
print(session_2.affiche_info())
m2i.ajout_session(session_1)
m2i.ajout_session(session_2)
print("trouver la formation session 2",m2i.recherche_formation_num_session("2"))
print()
print(m2i.recherche_formation_id_formateur("203"))
print(m2i.recherche_formation_nb_jour_supnb(40))
print(m2i.recherche_stagiaire_par_parcours("1","data"))
print(m2i.recherche_f_par_financeur("orange"))
print(m2i.recherche_f_par_mot_cle("java"))
print("le nombre des sessions : ",m2i.nombre_de_session())
print(session_1)
print(f"le nombre des stagiaires dans le centre de m2i {m2i.nbr_stagieres()}")
#print(f"le nombre des stagiaires de la formation java est {m2i.nbr_stagiere_par_formation("java")}")
print("Les formation proposé par le centre",m2i.formations())
print("le nombre moyen de stagiaire par formation",m2i.nb_moyenne_stagiaire_parsession())
session_2.supprimer_stagiaire("123")
print(session_2)

# interface graphique
fenetre = Tk()
fenetre.title("M2i")
fenetre.geometry("800x400")  
fenetre.iconbitmap("logo_m2iformation.ico")


label = Label(fenetre, text="Centre de Formation M2I", font=("Helvetica 20 bold"),fg="red")
label.pack()

fenetre.mainloop()