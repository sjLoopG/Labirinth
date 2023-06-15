import tkinter as tk

# Größe des Spielfelds
Feld_Breite = 15
Feld_Höhe = 15

# Erstellen des Hauptfensters
fenster = tk.Tk()
fenster.title("Labyrinth")
fenster.configure(bg="white")

# Erstellen eines Canvas-Widgets für das Spielfeld
canvas = tk.Canvas(fenster, width=400, height=400, bg="white")
canvas.pack()

# Labyrinth-Konfiguration (0 = Freie Zelle, 1 = Hindernis)
labyrinth = [
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
    [0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
]


# Funktion zum Zeichnen des Spielfelds mit Labyrinth
def zeichne_spielfeld():
    zellen_breite = 400 / Feld_Breite
    zellen_höhe = 400 / Feld_Höhe

    for i in range(Feld_Breite):
        for j in range(Feld_Höhe):
            x1 = i * zellen_breite
            y1 = j * zellen_höhe
            x2 = x1 + zellen_breite
            y2 = y1 + zellen_höhe

            if labyrinth[j][i] == 1:
                canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="white", width=1)
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="white", width=1)

# Aufruf der Funktion zum Zeichnen des Spielfelds mit Labyrinth
zeichne_spielfeld()

# Starten der Hauptschleife des Fensters
fenster.mainloop()
