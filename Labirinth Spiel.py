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

# Labyrinth-Konfiguration (0 = Freie Zelle, 1 = Hindernis, 2 = Ziel/Passierbares Feld)
labyrinth = [
    [3, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
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
    [1, 1, 1, 0, 0, 1, 0, 1, 2, 1, 1, 0, 1, 1, 1],
]

# Position der Figur
figur_x = 0
figur_y = 0

# Funktion zum Zeichnen des Spielfelds mit Labyrinth und Figur
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
            elif labyrinth[j][i] == 2:
                canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="white", width=1)
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="white", width=1)

    # Zeichne die Figur
    figur_x1 = figur_x * zellen_breite
    figur_y1 = figur_y * zellen_höhe
    figur_x2 = figur_x1 + zellen_breite
    figur_y2 = figur_y1 + zellen_höhe
    canvas.create_oval(figur_x1, figur_y1, figur_x2, figur_y2, fill="red")

# Funktion zur Überprüfung der Kollision mit Wänden oder dem Ziel
def prüfe_kollision(neue_x, neue_y):
    if neue_x < 0 or neue_x >= Feld_Breite:
        return False
    if neue_y < 0 or neue_y >= Feld_Höhe:
        return False
    if labyrinth[neue_y][neue_x] == 1:
        return False
    return True

# Funktion zum Bewegen der Figur
def bewege_figur(event):
    global figur_x, figur_y

    if event.keysym == "Up":
        neue_x = figur_x
        neue_y = figur_y - 1
    elif event.keysym == "Down":
        neue_x = figur_x
        neue_y = figur_y + 1
    elif event.keysym == "Left":
        neue_x = figur_x - 1
        neue_y = figur_y
    elif event.keysym == "Right":
        neue_x = figur_x + 1
        neue_y = figur_y
    else:
        return

    if prüfe_kollision(neue_x, neue_y):
        figur_x = neue_x
        figur_y = neue_y

    # Überprüfe, ob das Ziel erreicht wurde
    if labyrinth[figur_y][figur_x] == 2:
        
        label = tk.Label(canvas, text="Next Level", font=("Arial", 20), fg="black", bg="white")
        label.pack(expand=True)

    # Aktualisiere das Spielfeld
    zeichne_spielfeld()

# Aufruf der Funktion zum Zeichnen des Spielfelds mit Labyrinth und Figur
zeichne_spielfeld()

# Verknüpfen der Tastaturereignisse mit der Funktion zum Bewegen der Figur
fenster.bind("<Key>", bewege_figur)
fenster.focus_set()

# Starten der Hauptschleife des Fensters
fenster.mainloop()
