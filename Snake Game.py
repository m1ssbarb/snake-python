import pygame
import random
import time

#implement tests
#organize code: screen and sq_size  and underscores 

screen = pygame.display.set_mode((520,520))
sq_size = 40

#food properties: color, location 
class Food:

def __init__(self, x, y):
    self.x = x
    self.y = y
    self.brown = (165, 100, 42)

def draw_food(self):
    return pygame.draw.rect(screen, self.brown, (self.x, self.y, sq_size, sq_size))
    

#color, body parts, location, direction 
class Snake:

def __init__(self, x, y):
    self.x = x
    self.y = y
    self.list_of_xy = [[self.x, self.y]]
    self.green = (10,200,100)
    self.direction = None 
    self.length = 3

def right(self):
    self.direction = 'right'

def left(self):
    self.direction = 'left'
    

def up(self):
    self.direction = 'up'

def down(self):
    self.direction = 'down' 

def entire_snake(self): #modifies a list of xy
    i = 1
    for num in range(self.length - 1):
        if self.direction == None or self.direction == 'right':
            self.list_of_xy.append([self.x - sq_size * i, self.y])
            i += 1
        elif self.direction == 'left':
            self.list_of_xy.append([self.x + sq_size * i, self.y])
            i += 1
        elif self.direction == 'up':
            self.list_of_xy.append([self.x, self.y + sq_size * 1])
            i += 1
        elif self.direction == 'down':
            self.list_of_xy.append([self.x, self.y - sq_size * 1])
            i += 1

def move_snake(self):
    if self.direction == 'right':
        self.x += sq_size
        self.list_of_xy.append([self.x, self.y])
        self.update_snake()
    elif self.direction == 'left':
        self.x -= sq_size 
        self.list_of_xy.append([self.x, self.y])
        self.update_snake()
    elif self.direction == 'up':
        self.y -= sq_size
        self.list_of_xy.append([self.x, self.y])
        self.update_snake()
    elif self.direction == 'down':
        self.y += sq_size
        self.list_of_xy.append([self.x, self.y])
        self.update_snake()

def update_snake(self): #updates list of xy with new coordinates
    new_pos = [self.list_of_xy[len(self.list_of_xy)-1]]
    old_pos = self.list_of_xy.copy()[:self.length-1]
    for xy in old_pos:
        new_pos.append(xy)
    self.list_of_xy = new_pos.copy()
    
def draw_snake(self):
    for xy in self.list_of_xy:
        pygame.draw.rect(screen, self.green, (xy[0], xy[1], sq_size, sq_size))

def eat_snake(self):
    for xy in self.list_of_xy[1:]:
        if self.list_of_xy[0] == xy:
            return True

class Game:

def __init__(self):
    self.snakeX = 120
    self.snakeY = 240
    self.foodXY = random.randrange(0, 481, 40)
    self.score = 0
    self.running = True
    self.food = Food(self.foodXY, self.foodXY)
    self.snake = Snake(self.snakeX, self.snakeY)
    self.black = (0,0,0)

def game_screen(self):
    pygame.init()
    screen.fill((112,130,56))
    pygame.display.set_caption('Snake')
    score_font = pygame.font.Font('freesansbold.ttf', 20)
    display_score = score_font.render('Score: ' + str(self.score), True, self.black)
    screen.blit(display_score,(10,10))

def game_keys(self):
    pygame.event.pump()
    keys = pygame.key.get_pressed() 
    if (keys[pygame.K_RIGHT]):
        self.snake.right()
    elif (keys[pygame.K_LEFT]):
        self.snake.left()
    elif (keys[pygame.K_UP]):
        self.snake.up()
    elif (keys[pygame.K_DOWN]):
        self.snake.down()

def eat_food(self):
    if self.snake.list_of_xy[0][0] == self.food.x and self.snake.list_of_xy[0][1] == self.food.y:
            self.food = Food(random.randrange(0, 481, 40), random.randrange(0, 481, 40))
            self.snake.length += 1
            self.score += 1
    for snake_part in self.snake.list_of_xy[1:]:
        if snake_part[0] == self.food.x and snake_part[1] == self.food.y:
            self.food = Food(random.randrange(0, 481, 40), random.randrange(0, 481, 40))

def quit_game(self):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False 

def again_button(self):
    pygame.draw.rect(screen, self.snake.green, (10, 90, 160, 40))
    again_font = pygame.font.Font('freesansbold.ttf', 27)
    play_again = again_font.render('Play Again', True, self.black)
    screen.blit(play_again,(17, 97))
    pos = pygame.mouse.get_pos()
    button = pygame.Rect(10, 90, 160, 40)
    if button.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            self.__init__()
            self.execute()
            

def game_over(self):
    if self.snake.list_of_xy[0][0] < 0 or self.snake.list_of_xy[0][0] > 520 or self.snake.list_of_xy[0][1] < 0 or self.snake.list_of_xy[0][1] > 520 or self.snake.eat_snake():
        self.running = 'Game Over'
        while self.running == 'Game Over':
            screen.fill((112,130,56))
            game_over_font = pygame.font.Font('freesansbold.ttf', 32)
            score_font = pygame.font.Font('freesansbold.ttf', 27)
            game_over = game_over_font.render('GAME OVER', True, self.black)
            player_score = score_font.render('Your score is: ' + str(self.score), True, self.black)
            screen.blit(game_over,(10,10))
            screen.blit(player_score,(10,50))
            self.again_button()
            self.quit_game()
            pygame.display.update()

def execute(self):
        self.snake.entire_snake()
        while self.running:
            self.game_screen()
            self.game_keys()
            self.eat_food()
            self.food.draw_food()
            self.snake.move_snake()
            self.snake.draw_snake()
            self.game_over()
            self.quit_game()
            pygame.display.update()
            time.sleep(125/1000)

g = Game()
g.execute()



