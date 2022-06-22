from tkinter import *
import tkinter.font as font


def main():
    fenetre_principale()


def fenetre_principale():
    def vers_explication():
        fen.destroy()
        fenetre_explication()

    fen = Tk()

    fen.title("Interface")
    fen.geometry("1000x700")
    fen.resizable(False, False)

    f = font.Font(size=35)

    bouton_explication = Button(fen, text="Explication des règles", height=3, width=30, font=f, bg="green",
                                command=vers_explication)
    bouton_explication.pack(pady=100)

    bouton_jouer = Button(fen, text="Jouer", height=3, width=30, font=f, bg="orange")
    bouton_jouer.pack()

    fen.mainloop()


def fenetre_explication():
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

    bouton_jouer = Button(fen, text="Jouer", height=h, width=w, font=f, bg="orange")
    bouton_jouer.pack()

    fen.mainloop()


def fenetre_jouer():
    fen = Tk()
    h = 2
    w = 40
    y = 10

    fen.title("Interface")
    fen.geometry("1000x700")
    fen.resizable(False, False)

    f = font.Font(size=25)
    h_droit = 8

    h_gauche = 2
    w_gauche = 18

    pane_gauche = Frame(bg="black")
    pane_droit = Frame(bg="grey")

    pane_gauche.pack(side=LEFT, padx=10, pady=10, fill=BOTH)
    pane_droit.pack(side=RIGHT, padx=10, pady=10, fill=BOTH)

    bouton_regle = Button(pane_droit, text="Règles du jeu", bg="#55B4D1", font=f, height=h_droit)
    bouton_regle.pack(side=TOP, fill=BOTH)

    bouton_quiiter = Button(pane_droit, text="Quitter le jeu", bg="red", font=f, height=h_droit)
    bouton_quiiter.pack(side=BOTTOM, fill=BOTH)

    bouton_art = Button(pane_gauche, text="Arts", bg="red", font=f, height=h_gauche, width=w_gauche)
    bouton_art.grid(row=1, column=1)

    bouton_environnement = Button(pane_gauche, text="Environnement", bg="red", font=f, height=h_gauche, width=w_gauche)
    bouton_environnement.grid(row=1, column=2)

    fen.mainloop()


if __name__ == "__main__":
    main()
