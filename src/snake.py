import pygame
import random
import time
import sys


class bodyPart:
    def __init__(self, window,dotSize,colour):
        self.x = 0
        self.y = 0
        self.window = window
        self.dotSize=dotSize
        self.colour=colour

    def draw(self):
        pygame.draw.rect(self.window, self.colour, (self.x, self.y, self.dotSize, self.dotSize))




class snake:
    def __init__(self, window,dotSize,colour):
        #Coordenadas de la cabeza
        self.dir = 0
        self.body = [bodyPart(window,dotSize,(255-colour[0], 255-colour[1], 255-colour[2]))]#Resto del cuerpo de la serpiente
        self.window=window
        self.dotSize=dotSize
        self.colour=colour

    def draw(self):
        for i in self.body:
            i.draw()

    def addBodyPart(self ):
        self.body.append(bodyPart(self.window,self.dotSize,self.colour))

    def borderMove(self,x,y):

        self.body[0].x=x
        self.body[0].y=y
    def move(self):
        #Mover cabeza
        if self.dir == 0:
            self.body[0].x+=self.dotSize
        elif self.dir == 1:
            self.body[0].x -= self.dotSize
        elif self.dir == 2:
            self.body[0].y += self.dotSize
        elif self.dir == 3:
            self.body[0].y -= self.dotSize
    def moveBody(self):
        #Mover el resto del cuerpo
        for i in range(len(self.body) - 1):
            self.body[len(self.body) - i - 1].x =  self.body[len(self.body) - i - 2].x
            self.body[len(self.body) - i - 1].y =  self.body[len(self.body) - i - 2].y


    def bodyTouch(self):
        for i in range(len(self.body) - 2):
            if self.body[len(self.body) - i - 1].x == self.body[0].x and \
                    self.body[len(self.body) - i - 1].y ==  self.body[0].y:
                return True
        return False

class food:
    def __init__(self, window,wSize, dotSize,type):
        self.wSize=wSize
        self.x = random.randrange(int(wSize/dotSize)) * dotSize
        self.y = random.randrange(int(wSize/dotSize)) * dotSize
        self.window = window
        self.dotSize=dotSize
        self.type=type
        self.score=1
        self.colour=(255, 0, 0)

    def draw(self):
        pygame.draw.rect(self.window, self.colour, (self.x, self.y, self.dotSize, self.dotSize))

    def newfood(self):
        self.x = random.randrange(int(self.wSize/self.dotSize)) * self.dotSize
        self.y = random.randrange(int(self.wSize/self.dotSize))* self.dotSize
        if self.type!=0:
            if random.randrange(2)==1:
                self.score=2
                self.colour=(212, 172, 13)
            else:
                self.score = 1
                self.colour = (255, 0, 0)

    def eaten(self, x, y):
        return x==self.x and y == self.y



class Board:
    def __init__(self,size,dotSize,speed, backColour, snakeColour,borders,foodType):
        pygame.init()
        self.window=pygame.display.set_mode((size*dotSize, size*dotSize))
        self.window.fill(backColour)
        self.snake=snake(self.window,dotSize,snakeColour)
        self.size = size * dotSize
        self.food=food(self.window,self.size,dotSize,foodType)
        self.speed=speed
        self.backColour=backColour
        self.snakeColour=snakeColour
        self.borders=borders
        self.foodType=foodType
        self.dotSize=dotSize
        self.score=0
        pygame.display.set_caption('Snake')


    def refresh(self):
        self.window.fill(self.backColour)
        self.food.draw()
        self.snake.draw()
        self.printScore()

    def borderJump(self):
        # Aparecer en el borde contrario
        if self.snake.body[0].x > self.size:
            self.snake.borderMove(0-self.dotSize, self.snake.body[0].y)
        elif self.snake.body[0].x < 0:
            self.snake.borderMove(self.size , self.snake.body[0].y)

        if self.snake.body[0].y >self.size:
            self.snake.borderMove(self.snake.body[0].x, 0-self.dotSize)
        elif self.snake.body[0].y < 0:
            self.snake.borderMove(self.snake.body[0].x, self.size )

    def play(self):

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                #Decidir siguiente movimiento de la serpiente
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and self.snake.dir != 1:
                        self.snake.dir = 0
                    elif event.key == pygame.K_LEFT and self.snake.dir != 0:
                        self.snake.dir = 1
                    elif event.key == pygame.K_DOWN and self.snake.dir != 3:
                        self.snake.dir = 2
                    elif event.key == pygame.K_UP and self.snake.dir != 2:
                        self.snake.dir = 3

            self.snake.move()
            self.refresh()
            pygame.display.update()
            pygame.time.delay(self.speed)

            if self.food.eaten(self.snake.body[0].x , self.snake.body[0].y):
                self.score += self.food.score
                self.food.newfood()
                self.snake.addBodyPart()

            self.snake.moveBody()
            if not self.borders: self.borderJump()
            #Decidir si se acaba la partida

            run=self.gameOver()

        return self.score



    def gameOver(self):
        run = True
        if self.snake.bodyTouch():
            print("GAME OVER")
            time.sleep(1)
            run = False
        if self.borders:
            if self.snake.body[0].x >self.size or self.snake.body[0].x < 0 \
                    or  self.snake.body[0].y >self.size or self.snake.body[0].y < 0:
                print("GAME OVER")

                time.sleep(1)
                run=False

        return run

    def printScore(self):
        score_font = pygame.font.SysFont('times new roman', 30)
        score_surface = score_font.render('Score : ' + str(self.score), True, ( 211, 84, 0 ))
        score_rect = score_surface.get_rect()
        score_rect.midtop = (self.size/2, 1.25)
        self.window.blit(score_surface, score_rect)




    def finish(self):
        return True



