import math

class Ball:
    """
    Ball class
    Representation of a Ball
    """
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
        """
        Calcul of d_x and d_y for moving
        """
        self.d_x = self.speed * math.cos(self.direction)
        self.d_y = self.speed * math.sin(self.direction)

    def move(self):
        """
        Move the ball
        """
        self.x += self.d_x
        self.y += self.d_y

    def invertDx(self):
        """
        change the direction of the ball for x coord
        """
        self.d_x = -self.d_x

    def invertDy(self):
        """
        change the direction of the ball for y coord
        """
        self.d_y = -self.d_y

    def setColor(self, color):
        """
        set the color of the ball by the argument given
        """
        self.color = color

    def setSpeed(self, speed):
        """
        set the speed of the ball by the argument given
        """
        self.speed = speed

    def setDirection(self, d):
        """
        set the direction (in degree) of the ball by the argument given
        and update dx and dy
        """
        self.direction = d
        self.updateDeplacement()

    def setGraphics(self, graphics):
        """
        set the graphic (ellipse object) of the ball by the argument given
        """
        self.graphics = graphics
