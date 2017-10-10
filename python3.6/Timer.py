from threading import Thread
import time

class Timer(Thread):
    def __init__(self, timerText):
        Thread.__init__(self)
        self.hours      = 0
        self.minutes    = 0
        self.seconds    = 0
        self.timerText  = timerText
        self.running    = False
        self.daemon     = True

    def startTimer(self):
        self.running = True

    def stopTimer(self):
        self.running = False

    def resetTimer(self):
        self.hours      = 0
        self.minutes    = 0
        self.seconds    = 0
        self.timerText.config(text=self.getFormattedText())

    def getFormattedText(self):
        h = "00"
        m = "00"
        s = "00"
        if(self.seconds < 10):
            s = "0" + str(self.seconds)
        else:
            s = str(self.seconds)

        if(self.minutes < 10):
            m = "0" + str(self.minutes)
        else:
            m = str(self.minutes)

        if(self.hours < 10):
            h = "0" + str(self.hours)
        else:
            h = str(self.hours)

        return h + ":" + m + ":" + s

    def run(self):
        while(True):
            time.sleep(1)
            if(self.running):
                self.seconds += 1

                if(self.seconds >= 60):
                    self.seconds = 0
                    self.minutes += 1

                if(self.minutes >= 60):
                    self.minutes = 0
                    self.hours += 1

                self.timerText.config(text=self.getFormattedText())
