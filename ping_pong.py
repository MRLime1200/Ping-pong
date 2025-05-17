import pygame
pygame.init()

back = (200, 255, 255) 
mw = pygame.display.set_mode((500, 500)) 
mw.fill(back)
clock = pygame.time.Clock()
racket_x = 200
racket_y = 330


game_over = False
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)       
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
 
ball = Picture('ball.png', 30, 200, 50, 50)
platform = Picture('platform.png', 30, racket_y, 100, 30)

start_x = 5 
start_y = 5
count = 9 
monsters = [] 


speed_x = 3
speed_y = 3
move_right = 0
move_left = 0
while not game_over:
    mw.fill(back)
    ball.fill()
    platform.fill()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: 
                move_right = True 
            if event.key == pygame.K_DOWN:
                move_left = True 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_right = False 
            if event.key == pygame.K_DOWN:
                move_left = False 
    
    if move_right: 
        platform.rect.y -=3
    if move_left: 
        platform.rect.y +=3
    if  ball.rect.y < 0 or ball.rect.y > 500:
        speed_y *= -1
    if ball.rect.x > 450 or ball.rect.x < 0:
        speed_x *= -1




    ball.rect.x += speed_x
    ball.rect.y += speed_y
    platform.draw()
    ball.draw()
    pygame.display.update()
    clock.tick(40)
    
    

    




        


  



























































































































