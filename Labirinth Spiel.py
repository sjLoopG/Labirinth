# Module importieren
import tkinter as tk
import time

# Größe des Spielfelds
Feld_Breite = 15
Feld_Hoehe = 15

# Position der Figur
figur_x = 0
figur_y = 0

highscore = [
    {"name": "Loop", "zeit": 30.0},
    {"name": "Nadia", "zeit": 25.0}
]

start_time = time.time()
end_time = start_time

# Klasse definieren
class App:

    # root/master initialisieren
    def __init__(self):
        something = self
        self.master = tk.Tk()
        self.master.geometry("400x400")
        self.master.title("Maze Runner")
        self.set_main_frame()

    # Hauptfenster starten
    def set_main_frame(self):
        # Hauptframe definieren
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack()
        # Widgets initialisieren
        self.name_label = tk.Label(self.main_frame, text="Welcome to the amazing Maze Game!", font="bold")
        self.empty_label = tk.Label(self.main_frame, text="")
        self.start_button = tk.Button(self.main_frame, text="Start Game", command=self.set_level_1_frame)
        self.empty_label_2 = tk.Label(self.main_frame, text="")
        self.empty_label_3 = tk.Label(self.main_frame, text="")
        self.highscore_titel = tk.Label(self.main_frame, text="Highscore", font="bold")

        # Widgets positionieren
        self.name_label.grid(row=0, column=0)
        self.empty_label.grid(row=1, column=0)
        self.start_button.grid(row=2, column=0)
        self.empty_label_2.grid(row=3, column=0)
        self.highscore_titel.grid(row=4, column=0)
        self.empty_label_3.grid(row=5, column=0)

        # Highscore sortieren
        sortedHighScoreList = sorted(highscore, key=lambda x: x["zeit"])

        # Highscore anzeigen
        counter = 0
        for score in sortedHighScoreList:
            tk.Label(self.main_frame, text=str(counter+1) +". " +
                                           str(score["name"]) + " " + str(score["zeit"])+ "''").grid(row=counter+6, column=0)
            counter += 1

        self.master.mainloop()

    def set_name_frame(self):

        global start_time, end_time, highscore

        self.name_frame = tk.Frame(self.master)
        self.name_frame.pack()
        self.total_time = round((end_time - start_time), 2)

        sortedHighScoreList = sorted(highscore, key=lambda x: x["zeit"])
        bestScore = sortedHighScoreList[0]
        bestTime = bestScore["zeit"]

        if (self.total_time < bestTime):
            print(bestScore)
            print(bestScore["zeit"])
            print(self.total_time)
            tk.Label(self.name_frame , text="NEW RECORD !!!").grid(row=0, column=0)
            tk.Label(self.name_frame , text="You have beaten the time of " + bestScore["name"]).grid(row=1, column=0)


        time_label = tk.Label(self.name_frame , text="Your time was: " + str(self.total_time))
        self.name_label = tk.Label(self.name_frame, text="Please enter your Name:")
        self.inputName = tk.Entry(self.name_frame)
        self.ok_button = tk.Button(self.name_frame , text="OK", command=self.exit_name_frame)

        self.name_label.grid(row=2, column=0)
        self.inputName.grid(row=3, column=0)
        time_label.grid(row=4, column=0)
        self.ok_button.grid(row=5, column=0)



    def exit_name_frame(self):
        print(self.inputName.get())
        print(self.total_time)

        highscore.append({"name": "" + self.inputName.get() + "", "zeit": + self.total_time })
        self.name_frame.destroy()
        self.set_main_frame()

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

        def zeichne_spielfeld():
            zellen_breite = 400 / Feld_Breite
            zellen_höhe = 400 / Feld_Hoehe

            for i in range(Feld_Breite):
                for j in range(Feld_Hoehe):
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
            if neue_y < 0 or neue_y >= Feld_Hoehe:
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
            self.set_name_frame()

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

            zeichne_spielfeld()

        zeichne_spielfeld()
        self.level_1_frame.bind("<Key>", bewege_figur)
        self.level_1_frame.focus_set()
        # Fenster neustarten
        self.master.mainloop()

# App ausführen
app = App()
