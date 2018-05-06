#Create a simple ping pong game

import  pygame, sys
from pygame.locals import *
#Using uppercase letter to create a local variable, which will be used for the whole game
BLACK = (0,0,0)
WHITE = (255,255,255)

window_height = 300
window_width = 400

#Create the game's window
display_surf = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Ping pong")

fps = 200 #Number of frame per second
fps_clock = pygame.time.Clock()

class Paddle():
    def __init__(self,w,h,x):
        self.w = w
        self.h = h
        self.x = x
        self.y = int(window_height/2)
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self):
        pygame.draw.rect(display_surf,WHITE,self.rect)
    #Create a movement for user
    def move(self,pos):
        self.rect.y = pos[1] #Array of direction pos[x,y] -> x = pos[0], y = pos[1]
        self.draw()

#Create a movement for bots based on the movement of ball
class Autopaddle(Paddle):
    def __init__(self,w,h,x,speed,ball): #How to inherit a class
        #Call back its superior
        super().__init__(w,h,x)
        self.speed = speed
        self.ball = ball #we need to use var 'ball' to see the movement of the ball
    def move(self):
        if self.ball.dir_x == 1:
            if self.rect.y < self.ball.rect.bottom:
                self.rect.y += self.speed
            if self.rect.y > self.ball.rect.bottom:
                self.rect.y -= self.speed
class Scoreboard():
    def __init__(self,fontSize = 20,score = 0):
        self.x = window_width - 150
        self.y = 20
        self.score = score
        self.font = pygame.font.Font('freesansbold.ttf', fontSize)
    def display(self):
        result_srf = self.font.render('Score: = %s'%(self.score),True, WHITE)
        result_rect = result_srf.rect.get()
        result_rect.topleft = (window_width-150, 20)
        display_surf.blit(result_rect,result_srf)
class Ball():
    def __init__(self,x,y,w,h,speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.dir_x = -1 #Set direction: Left: -1  Right: 1
        self.dir_y = -1 #Set direction: Up: -1  Down:
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h) #Toa do cua qua bong
    def draw(self):
        pygame.draw.rect(display_surf,WHITE,self.rect)
    def bounce(self,axis):
        if axis == 'x':
            self.dir_y *= -1 #Change direction if the ball hit the wall
        if axis == 'y':
            self.dir_x *= -1 #Change direction if the ball hit the floor or ceiling
    def hit_ceiling(self):
            if self.dir_y == -1 and self.rect.top <= self.h:
                return True
            else:
                return False
    def hit_floor(self):
            if self.dir_y == 1 and self.rect.bottom >= window_height-self.h: #h la do day cua tuong vien cua window
                return True
            else:
                return False
    def hit_wall(self):
            if (self.dir_x == -1 and self.rect.left <= self.w) or (self.dir_x == 1 and self.rect.right >= window_width-self.w):
                return True
            else:
                return False
    def hit_paddle(self,paddle):
        if self.rect.left <= paddle.rect.right and (self.rect.bottom >= paddle.rect.top and self.rect.top <= paddle.rect.bottom):
            return True
        elif self.rect.right <= paddle.rect.left and (self.rect.bottom >= paddle.rect.top and self.rect.top <= paddle.rect.bottom):
                return True
        else:
            return False
    def move(self):
        self.rect.x += (self.dir_x * self.speed)
        self.rect.y += (self.dir_y * self.speed)
        if self.hit_ceiling() or self.hit_floor():
            self.bounce('x')
class Game():
    def __init__(self, line_thickness = 10, speed = 1):
        self.line_thickness = line_thickness
        self.speed = speed

        ball_x = int(window_width/2)
        ball_y = int(window_height/2)
        ball_w = self.line_thickness
        ball_h = self.line_thickness

        self.ball = Ball(ball_x,ball_y,ball_w,ball_h,self.speed) #Create the ball

        self.paddles = {} #Contain user's paddle and bots' paddle
        paddle_x = 20
        paddle_w = self.line_thickness
        paddle_h = 50
        self.paddles['user'] = Paddle(paddle_w,paddle_h,paddle_x)
        self.paddles['computer'] = Autopaddle(paddle_w,paddle_h,paddle_x,self.speed,self.ball)

        self.score = Scoreboard(0)
    def draw_arena(self):

        display_surf.fill((0,0,0))
        pygame.draw.line(display_surf,WHITE,(int(window_width/2),0),(int(window_width/2),int(window_height)))

    def update(self):

        self.ball.move()
        self.paddles['computer'].move()

        if self.ball.hit_paddle(self.paddles['user']):
            self.score.score +=1
            self.score.display(self.score.score)

        self.draw_arena()
        self.ball.draw()
        self.paddles['user'].draw()
        self.paddles['computer'].draw()
def main():
    pygame.init()

    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                game.paddles['user'].move(event.pos)
        game.update()
        pygame.display.update()
        fps_clock.tick(fps)

if __name__ == '__main__': #Python will automatically create a compulsory variable '__name__' to use whenever we want to use it
    main()