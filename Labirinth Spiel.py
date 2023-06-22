

# Module importieren
import tkinter as tk
import time

# Größe des Spielfelds
Feld_Breite = 15
Feld_Höhe = 15

# Position der Figur
figur_x = 0
figur_y = 0

start_time = time.time()
end_time = start_time

# Klasse definieren
class App:

    # root/master initialisieren
    def __init__(self):
        something = self
        self.master = tk.Tk()
        self.master.geometry("400x400")
        self.master.protocol("WM_DELETE_WINDOW", self.quit_app)
        self.master.title("Maze Runner")

        self.set_main_frame()

    # Hauptfenster starten
    def set_main_frame(self):
        # Hauptframe definieren
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack()
        # Widgets initialisieren
        self.hallo_label = tk.Label(self.main_frame, text="Welcome to the amazing Maze Game!")
        self.empty_label = tk.Label(self.main_frame, text="")
        self.start_button = tk.Button(self.main_frame, text="Start Game", command=self.set_level_1_frame)
        total_time = round((end_time - start_time), 2)
        self.last_time_label = tk.Label(self.main_frame, text="Last Time: " + str(total_time))
        self.quit_button = tk.Button(self.main_frame, text="Quit", command=self.quit_app)
        # Widgets positionieren
        self.hallo_label.grid(row=0, column=0)
        self.empty_label.grid(row=1, column=0)
        self.start_button.grid(row=2, column=0)
        self.last_time_label.grid(row=4, column=0)
        self.quit_button.grid(row=8, column=0)

        # Bestätigung in der Konsole
        print("Hauptfenster geöffnet")
        # Fenster neustarten
        self.master.mainloop()



    # Einsellungsfenster starten
    def set_level_1_frame(self):
        global start_time

        start_time = time.time()
        # Einstellungsframe definieren
        self.level_1_frame = tk.Frame(self.master)
        # Hauptframe schließen
        self.main_frame.destroy()
        self.level_1_frame.pack()
        # Widgets initialisieren
        # self.head_label = tk.Label(self.level_1_frame, text ="Level 1")

        # Erstellen eines Canvas-Widgets für das Spielfeld
        self.level_1_canvas = tk.Canvas(self.level_1_frame, width=400, height=400, bg="white")
        self.level_1_canvas.pack()

        # Labyrinth-Konfiguration (0 = Freie Zelle, 1 = Hindernis, 2 = Ziel/Passierbares Feld)
        labyrinth = [
            [3, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
            [0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1],
            [2, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1],
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
                        self.level_1_canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="white", width=1)
                    elif labyrinth[j][i] == 2:
                        self.level_1_canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="white", width=1)
                    else:
                        self.level_1_canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="white", width=1)

            # Zeichne die Figur
            figur_x1 = figur_x * zellen_breite
            figur_y1 = figur_y * zellen_höhe
            figur_x2 = figur_x1 + zellen_breite
            figur_y2 = figur_y1 + zellen_höhe
            self.level_1_canvas.create_oval(figur_x1, figur_y1, figur_x2, figur_y2, fill="red")

        def prüfe_kollision(neue_x, neue_y):
            if neue_x < 0 or neue_x >= Feld_Breite:
                return False
            if neue_y < 0 or neue_y >= Feld_Höhe:
                return False
            if labyrinth[neue_y][neue_x] == 1:
                return False
            return True


        def end_level(self):
            # figur wieder auf 0 0
            global figur_x, figur_y, end_time
            figur_x = 0
            figur_y = 0
            end_time = time.time()
            self.level_1_frame.destroy()
            # Hauptframe starten
            self.set_main_frame()

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
                end_level(self)
                #
                # label = tk.Label(canvas, text="Next Level", font=("Arial", 20), fg="black", bg="white")
                # label.pack(expand=True)

            zeichne_spielfeld()

        zeichne_spielfeld()
        self.level_1_frame.bind("<Key>", bewege_figur)
        self.level_1_frame.focus_set()
        # Fenster neustarten
        self.master.mainloop()


    def quit_app(self):
        print("Programm beendet")
        self.master.destroy()


# App ausführen (Instanz der Klasse App erstellen)
app = App()
