from tkinter import *
import tkinter.font as font


def main():
    fenetre_principale()


def fenetre_principale():

    def vers_explication():
        fen.destroy()
        fenetre_explication()

    def vers_jouer():
        fen.destroy()
        fenetre_jouer()

    fen = Tk()

    fen.title("Interface")
    fen.geometry("1000x700")
    fen.resizable(False, False)

    f = font.Font(size=35)

    bouton_explication = Button(fen, text="Explication des règles", height=3, width=30, font=f, bg="green",
                                command=vers_explication)
    bouton_explication.pack(pady=100)

    bouton_jouer = Button(fen, text="Jouer", height=3, width=30, font=f, bg="orange", command=vers_jouer)
    bouton_jouer.pack()

    fen.mainloop()


def fenetre_explication():

    def vers_principale():
        fen.destroy()
        fenetre_principale()

    def vers_jouer():
        fen.destroy()
        fenetre_jouer()

    fen = Tk()

    fen.title("Interface")
    fen.geometry("1000x700")
    fen.resizable(False, False)

    f = font.Font(size=25)
    h = 2
    w = 40
    y = 10

    bouton_explication = Button(fen, text="Explication entières", height=h, width=w, font=f, bg="green")
    bouton_explication.pack(pady=y)

    bouton_mise_en_place = Button(fen, text="Mise en place", height=h, width=w, font=f, bg="#55B4D1")
    bouton_mise_en_place.pack()

    bouton_deroulement = Button(fen, text="Déroulement d'un tour", height=h, width=w, font=f, bg="#55B4D1")
    bouton_deroulement.pack(pady=y)

    bouton_fin = Button(fen, text="Fin du jeu", height=h, width=w, font=f, bg="#55B4D1")
    bouton_fin.pack()

    bouton_de = Button(fen, text="Explication du dé spécial", height=h, width=w, font=f, bg="#55B4D1")
    bouton_de.pack(pady=y)

    bouton_jouer = Button(fen, text="Jouer", height=h, width=w, font=f, bg="orange", command=vers_jouer)
    bouton_jouer.pack()

    fen.mainloop()


def fenetre_jouer():

    def vers_principale():
        fen.destroy()
        fenetre_principale()

    def vers_explication():
        fen.destroy()
        fenetre_explication()

    fen = Tk()
    h = 2
    w = 40
    y = 10

    fen.title("Interface")
    fen.geometry("1000x700")
    fen.resizable(False, False)

    f = font.Font(size=25)
    h_droit = 6

    x_droit = 10
    y_droit = 15

    h_gauche = 3
    w_gauche = 19

    x_gauche = 2
    y_gauche = 2

    pane_gauche = Frame()
    pane_droit = Frame()

    pane_gauche.pack(side=LEFT, padx=10, pady=10)
    pane_droit.pack(side=RIGHT, padx=15, pady=10)

    bouton_regle = Button(pane_droit, text="Règles du jeu", bg="green", font=font.Font(size=24), height=h_droit, command=vers_explication)
    bouton_regle.pack(side=TOP, fill=BOTH, pady=y_droit)

    bouton_quiiter = Button(pane_droit, text="Quitter le jeu", bg="red", font=font.Font(size=24), height=h_droit, command=vers_principale)
    bouton_quiiter.pack(side=BOTTOM, fill=BOTH, pady=y_droit)

    bouton_art = Button(pane_gauche, text="Arts", bg="pink", font=f, height=h_gauche, width=w_gauche)
    bouton_art.grid(row=1, column=1, padx=x_gauche, pady=y_gauche)

    bouton_environnement = Button(pane_gauche, text="Environnement", bg="green", font=f, height=h_gauche, width=w_gauche)
    bouton_environnement.grid(row=1, column=2, padx=x_gauche, pady=y_gauche)

    bouton_chronologie = Button(pane_gauche, text="Chronologie", bg="brown", font=f, height=h_gauche, width=w_gauche)
    bouton_chronologie.grid(row=2, column=1, padx=x_gauche, pady=y_gauche)

    bouton_geo = Button(pane_gauche, text="Géographie", bg="blue", font=f, height=h_gauche, width=w_gauche)
    bouton_geo.grid(row=2, column=2, padx=x_gauche, pady=y_gauche)

    bouton_culture_g = Button(pane_gauche, text="Culture générale", bg="white", font=f, height=h_gauche, width=w_gauche)
    bouton_culture_g.grid(row=3, column=1, padx=x_gauche, pady=y_gauche)

    bouton_sciences = Button(pane_gauche, text="Sciences", bg="orange", font=f, height=h_gauche, width=w_gauche)
    bouton_sciences.grid(row=3, column=2, padx=x_gauche, pady=y_gauche)

    bouton_culture_populaire = Button(pane_gauche, text="Culture populaire", bg="grey", font=f, height=h_gauche, width=w_gauche)
    bouton_culture_populaire.grid(row=4, column=1, padx=x_gauche, pady=y_gauche)

    bouton_sports = Button(pane_gauche, text="Sports", bg="purple", font=f, height=h_gauche,
                        width=w_gauche)
    bouton_sports.grid(row=4, column=2, padx=x_gauche, pady=y_gauche)

    fen.mainloop()


if __name__ == "__main__":
    main()
