from tkinter import *
from tkinter import font
from BallGame import *
from Timer import *




class MainUI(Frame):

    def __init__(self):
        self.root = Tk()
        self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.overrideredirect(1)

        # FullScreen
        self.root.geometry("%dx%d+0+0" % (self.w, self.h))

        # Titre
        self.root.title("34003611 - Python Ball'z")


        self.initUI()
        self.root.mainloop();

    def initUI(self):
        # font
        buttonFont      = font.Font(family="Helvetica", weight="bold")

        # buttonSize
        buttonWidth     = self.w * .020
        buttonHeight    = self.h * .006

        # Conteneur
        self.bottomContainer = Canvas(self.root, width=self.w, height=self.h*.1)
        self.bottomContainer.pack(side="bottom")
        self.bottomContainer.configure(background="honeydew4")


        self.topContainer = Canvas(self.root, width=self.w, height=self.h*.1)
        self.topContainer.pack(side="top", fill=X)

        self.ballsArea = Canvas(self.root, width=self.w, height=self.h*.8)
        self.ballsArea.pack()
        self.ballsArea.configure(background="cornsilk2")

        # Buttons
        self.closeButton                    = Button(self.bottomContainer, text="CLOSE", command=self.root.quit, width=int(buttonWidth), height=int(buttonHeight), font=buttonFont)
        self.closeButton.pack(side="right")

        self.startStopButton                = Button(self.bottomContainer, text="START", width=int(buttonWidth), height=int(buttonHeight), font=buttonFont)
        self.startStopButton.pack(side="right")

        self.resetButton                    = Button(self.bottomContainer, text="RESET", width=int(buttonWidth), height=int(buttonHeight), font=buttonFont)
        self.resetButton.pack(side="right")

        self.plusButton                     = Button(self.bottomContainer, text="+", width=int(buttonWidth), height=int(buttonHeight), font=buttonFont)
        self.plusButton.pack(side="left")

        self.minusButton                    = Button(self.bottomContainer, text="-", width=int(buttonWidth), height=int(buttonHeight), font=buttonFont)
        self.minusButton.pack(side="left")

        # Texte du top container
        self.score                          = Label(self.topContainer, text="Score : 0", height=int(self.h * .005))
        self.score.pack(side="left", padx=int(self.w*.15))

        self.timer                          = Label(self.topContainer, text="00:00:00", height=int(self.h * .005))
        self.timer.pack(side="right", padx=int(self.w*.15))

        #self.resetButton.config(command=self.root.quit)

        self.game = BallGame(self.ballsArea, self.score)

        self.timerThread = Timer(self.timer)

        self.plusButton.config(command=self.game.addOneBall)
        self.minusButton.config(command=self.game.deleteOneBall)
        self.startStopButton.config(command=self.startStopGame)
        self.resetButton.config(command=self.resetGame)



        self.game.start()
        self.timerThread.start()


    def resetGame(self):
        self.game.resetGame()
        self.timerThread.resetTimer()

    def startStopGame(self):
        if(self.game.running):
            self.game.stopGame()
            self.startStopButton.config(text="START")
            self.timerThread.stopTimer()
        else:
            self.game.startGame()
            self.startStopButton.config(text="STOP")
            self.timerThread.startTimer()
