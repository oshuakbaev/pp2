import pygame , sys, random, time 

WIDTH = 800
HEIGHT = 600 
FPS = 30
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hungry Lion")

background = pygame.image.load("wh.jpeg").convert()
background_rect = background.get_rect()
player_img = pygame.image.load("blue.jpg").convert()
enemy_img = pygame.image.load("red.png").convert()
food_img = pygame.image.load("green.png").convert()


font_name = pygame.font.match_font('arial') # Переменная, которая хранит шрифт 'arial'
def draw_text(surf, text, size, x, y): # Функция для записи текста на экран
    font = pygame.font.Font(font_name, size) # Переменная, хранящая метод Font, который представляет собой набор из шрифта и размера
    text_surface = font.render(text, True, BLACK) # Переменная, хранящая текст и цвет текста
    text_rect = text_surface.get_rect() # Переменная, делающая текст "частью" pygame (rect)
    text_rect.midtop = (x, y) # Координаты текста
    surf.blit(text_surface, text_rect) # Метод, который рисует текст на экран
    #Sprite , инструкция для всех обьектов
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # это конструктор 
        self.image = pygame.transform.scale(player_img,(10,10)) # изменение размера для картинки 
        self.rect = self.image.get_rect()
        self.rect.centerx = 20
        self.rect.bottom = 580 
        self.speedx = 0
        self.speedy = 0

    
    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        #зажал keystate
        if keystate[pygame.K_LEFT]:
            self.speedx = -10 
        elif keystate[pygame.K_RIGHT]:
            self.speedx = 10 
        elif keystate[pygame.K_UP]:
            self.speedy = -10 
        elif keystate[pygame.K_DOWN]:
            self.speedy = 10 
        self.rect.x += self.speedx 
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.left = 0 
        if self.rect.left < 0: 
            self.rect.right = WIDTH
        


class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # это конструктор 
        self.image = pygame.transform.scale(food_img,(10,10)) # изменение размера для картинки 
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width) # если аргумента нету начинает с 0
        self.rect.y = random.randrange(HEIGHT + 40,HEIGHT + 100)
        self.speedy = random.randrange(-8,-1)
    
    def update(self):
        self.rect.y += self.speedy 
        if self.rect.bottom < -10: 
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(HEIGHT + 40,HEIGHT + 100)
            self.speedy = random.randrange(-8,-1)


    
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # это конструктор 
        self.image = pygame.transform.scale(enemy_img,(10,10)) # изменение размера для картинки 
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = self.speedy = random.randrange(1,8)
    
    def update(self):
        self.rect.y += self.speedy 
        if self.rect.top > HEIGHT + 10: 
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = self.speedy = random.randrange(1,8)

all_sprites = pygame.sprite.Group() #по сути как лист, для множество обьектов
foods = pygame.sprite.Group()
enemies =   pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for x in range(25):
    e = Enemy()
    all_sprites.add(e)
    enemies.add(e)

for x in range(10):
    f =  Food()
    all_sprites.add(f)
    foods.add(f)

score = 0 
running = True 


while running:
    pygame.time.Clock().tick(FPS)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

    all_sprites.update()            
    hits1 = pygame.sprite.spritecollide(player,foods,True) #столкновение, True - уничтожить , False - не уходит
    for x in hits1: 
        score+=1
        f =  Food()
        all_sprites.add(f)
        foods.add(f)
    
    hits2 = pygame.sprite.spritecollide(player,enemies,True) #столкновение, True - уничтожить , False - не уходит
    for x in hits2: 
        score-=1
        f = Food()
        all_sprites.add(e)
        enemies.add(e)
    
    if score < 0:
        running = False

    screen.blit(background,background_rect)
    all_sprites.draw(screen) #отрисовка 
    draw_text(screen ,"Score: " + str(score),18,50,50)
    pygame.display.flip()

pygame.quit()


    
