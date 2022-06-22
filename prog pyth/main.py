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

    bouton_explication = Button(fen, text="Explication des règles", height=3, width=30, font=f, bg="green", command=vers_explication)
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

    bouton_jouer = Button(fen, text="Mise en place", height=h, width=w, font=f, bg="#55B4D1")
    bouton_jouer.pack()

    bouton_explication = Button(fen, text="Déroulement d'un tour", height=h, width=w, font=f, bg="#55B4D1")
    bouton_explication.pack(pady=y)

    bouton_jouer = Button(fen, text="Fin du jeu", height=h, width=w, font=f, bg="#55B4D1")
    bouton_jouer.pack()

    bouton_explication = Button(fen, text="Explication du dé spécial", height=h, width=w, font=f, bg="#55B4D1")
    bouton_explication.pack(pady=y)

    bouton_jouer = Button(fen, text="Jouer", height=h, width=w, font=f, bg="orange")
    bouton_jouer.pack()

    fen.mainloop()

if __name__ == "__main__":
    main()