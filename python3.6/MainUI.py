from tkinter import *
from tkinter import font
from BallGame import *
from Timer import *




class MainUI(Frame):
    """
    MainUI class
    Create the frame with all buttons and areas
    And launch threads (game and timer)
    """

    def __init__(self):
        # Tk init
        self.root = Tk()
        self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.overrideredirect(1)

        # FullScreen
        self.root.geometry("%dx%d+0+0" % (self.w, self.h))

        # Titre
        self.root.title("34003611 - Python Ball'z")

        # init UI and threads
        self.initUI()

        # Start Tkinter thread
        self.root.mainloop();

    def initUI(self):
        """
        Create all the user interface
        And launch the game and timer threads
        """
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

        # Game Object
        self.game = BallGame(self.ballsArea, self.score)

        # Timer Object
        self.timerThread = Timer(self.timer)

        # Bind commands to buttons
        self.plusButton.config(command=self.game.addOneBall)
        self.minusButton.config(command=self.game.deleteOneBall)
        self.startStopButton.config(command=self.startStopGame)
        self.resetButton.config(command=self.resetGame)


        # Start threads
        self.game.start()
        self.timerThread.start()


    def resetGame(self):
        """
        Reset Game and Timer
        """
        self.game.resetGame()
        self.timerThread.resetTimer()

    def startStopGame(self):
        """
        Start or Pause the game
        update startStopButton text
        """
        if(self.game.running):
            self.game.stopGame()
            self.startStopButton.config(text="START")
            self.timerThread.stopTimer()
        else:
            self.game.startGame()
            self.startStopButton.config(text="STOP")
            self.timerThread.startTimer()
