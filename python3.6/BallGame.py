from threading import Thread
import time, random, math
from Ball import *


class BallGame(Thread):

    def __init__(self, ballsContainer, scorePanel):
        Thread.__init__(self)

        self.daemon                 = True
        self.running                = False
        self.balls                  = []
        self.ballsContainer         = ballsContainer
        self.ballsToAdd             = 0
        self.ballsToDelete          = 0
        self.reset                  = False
        self.scorePanel             = scorePanel
        self.score                  = 0

    def startGame(self):
        self.running = True;

    def stopGame(self):
        self.running = False;

    def addOneBall(self):
        if(len(self.balls) < 21):
            self.ballsToAdd += 1

    def deleteOneBall(self):
        self.ballsToDelete += 1

    def run(self):
        while True:
            # Suppression des balles
            while(self.ballsToDelete > 0):
                # S'il y a des balles à supprimer
                if(len(self.balls) > 0):
                    self.ballsContainer.delete(self.balls[-1].graphics)
                    self.balls.remove(self.balls[-1])
                    self.ballsToDelete -= 1
                else:
                    self.ballsToDelete = 0

            # Ajout des balles
            while(self.ballsToAdd > 0):

                self.ballsToAdd -= 1;
                r       = random.randrange(10,50)

                # On s'assure que ça n'apparaisse jamais sur un bord
                x       = random.randrange(0 + r, self.ballsContainer.winfo_width() - r)
                y       = random.randrange(0 + r, self.ballsContainer.winfo_height() - r)

                c_r     = hex(random.randrange(0,255))[2:]
                if(len(c_r) < 2):
                    c_r = "0" + c_r

                c_v     = hex(random.randrange(0,255))[2:]
                if(len(c_v) < 2):
                    c_v = "0" + c_v

                c_b     = hex(random.randrange(0,255))[2:]
                if(len(c_b) < 2):
                    c_b = "0" + c_b


                color = "#" + str(c_r) + "" + str(c_v) + "" + str(c_b)

                # On crée la balle
                b = Ball(x,y,r)

                b.setColor(color)

                b.setSpeed(random.randrange(2,10))

                b.setDirection(random.randrange(0,360))

                bGraphics = self.ballsContainer.create_oval(b.x-b.r, b.y-b.r, b.x+b.r, b.y+b.r, fill=b.color)

                b.setGraphics(bGraphics)

                self.balls.append(b)

            if(self.running):
                self.drawBalls()
                self.moveBalls()
                self.ballsCollision()
            time.sleep(0.015)

    def ballsCollision(self):
        toDelete = []
        for ballFirst in self.balls:
            for ballSecond in self.balls:

                if(ballFirst != ballSecond):
                    dx = ballFirst.x - ballSecond.x
                    dy = ballFirst.y - ballSecond.y

                    dist = math.sqrt(dx * dx + dy * dy)

                    if(dist < ballFirst.r + ballSecond.r):
                        if(ballFirst not in toDelete):
                            toDelete.append(ballFirst)
                        if(ballSecond not in toDelete):
                            toDelete.append(ballSecond)

        tempScore = 0
        for ball in toDelete:
            self.ballsContainer.delete(ball.graphics)
            self.balls.remove(ball)
            tempScore += 1

        if(tempScore > 0):
            self.score += int(tempScore/2)
            self.scorePanel.config(text="Score : " + str(self.score))



    def resetGame(self):
        self.score = 0
        self.scorePanel.config(text="Score : 0")
        toDelete = []
        for ball in self.balls:
            toDelete.append(ball)

        # Ici on utilise une autre liste
        # Demande de la mémoire et du cpu, mais négligeable au vu du maximum de balles
        for ball in toDelete:
            self.ballsContainer.delete(ball.graphics)
            self.balls.remove(ball)


    # Deplace l'ensemble des balles
    def moveBalls(self):
        for ball in self.balls:
            if(ball.x - ball.r - 1) <= 0:
                ball.invertDx()
            if(ball.x + ball.r + 1) >= self.ballsContainer.winfo_width():
                ball.invertDx()
            if(ball.y - ball.r - 1) <= 0:
                ball.invertDy()
            if(ball.y + ball.r + 1) >= self.ballsContainer.winfo_height():
                ball.invertDy()

            ball.move()

    # Affiche l'ensemble des balles à l'écran
    def drawBalls(self):
        for ball in self.balls:
            self.ballsContainer.move(ball.graphics, ball.d_x, ball.d_y)
