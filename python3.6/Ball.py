import math

class Ball:

    def __init__(self, x, y, r):
        self.x          = x
        self.y          = y
        self.r          = r
        self.d_x        = 0
        self.d_y        = 0
        self.speed      = 2
        self.direction  = 90
        self.color      = "#000000"

    def updateDeplacement(self):
        self.d_x = self.speed * math.cos(self.direction)
        self.d_y = self.speed * math.sin(self.direction)

    def move(self):
        self.x += self.d_x
        self.y += self.d_y

    def invertDx(self):
        self.d_x = -self.d_x

    def invertDy(self):
        self.d_y = -self.d_y

    def setColor(self, color):
        self.color = color

    def setSpeed(self, speed):
        self.speed = speed

    def setDirection(self, d):
        self.direction = d
        self.updateDeplacement()

    def setGraphics(self, graphics):
        self.graphics = graphics
