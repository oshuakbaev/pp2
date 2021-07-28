import pygame,sys,random,time,pygame_menu



class Game():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600

        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.brown = pygame.Color(165, 42, 42)
        self.blue = pygame.Color(0,0,255)
        self.fps = pygame.time.Clock()

        self.score = 0 
    
    def check_for_errors(self):
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()
        else:
            print("OK")
    
    def set_surface(self):
        self.play_surface = pygame.display.set_mode((
            self.screen_width,self.screen_height))
        pygame.display.set_caption("The Snake game")

    def even_loop(self,change_to):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change_to = "RIGHT"
                elif event.key == pygame.K_LEFT:
                    change_to = "LEFT"
                elif event.key == pygame.K_DOWN:
                    change_to = "DOWN"
                elif event.key == pygame.K_UP:
                    change_to = "UP"
        return change_to
    def refresh_screen(self,fps):
        pygame.display.flip()
        game.fps.tick(fps)
    
    def show_score(self):
        font = pygame.font.SysFont('arial',24)
        surf = font.render('Score:{0}'.format(self.score),True,self.black)
        rect = surf.get_rect()
        rect.midtop = (80,10)
        self.play_surface.blit(surf,rect)

    def game_over(self):
        menu = pygame_menu.Menu('Play Again?', game.screen_width, game.screen_height,
                       theme=pygame_menu.themes.THEME_BLUE)
        menu.add.text_input('Name :', default='Player')
        menu.add.button('Yes', play_again)
        menu.add.button('No', pygame_menu.events.EXIT)
        menu.mainloop(game.play_surface)
class Wall():
    def __init__(self,wall_color):
        self.wall_color = wall_color
        temp1 = random.randint(0,(game.screen_width - 100)/10)*10
        temp2 = random.randint(0,(game.screen_height - 100)/10)*10
        t = random.randint(1,2)

        if t == 1: 
            self.wall_position = [[temp1,temp2],[temp1,temp2+10],[temp1,temp2+20],[temp1,temp2+30],[temp1,temp2+40]] 
        elif t == 2: 
            self.wall_position = [[temp1,temp2],[temp1+10,temp2],[temp1+20,temp2],[temp1+30,temp2],[temp1+40,temp2]]
        
    def draw_walls(self,play_surface):
        for pos in self.wall_position:
            pygame.draw.rect(play_surface,self.wall_color,
                pygame.Rect(pos[0],pos[1],10,10))

class Snake():
    def __init__(self,snake_color):
        self.snake_head_pos = [100,50]
        self.snake_body = [[100,50],[90,50],[80,50]]
        self.direction = "RIGHT"
        self.change_to = self.direction
        self.snake_color = snake_color
        # change_to указываем змее куда идти , а direction указывает на то куда змея сама идет , ее статус.
    def direction_and_change(self):
        if any((self.change_to == "RIGHT" and not self.direction == "LEFT",
            self.change_to == "LEFT" and not self.direction == "RIGHT",
            self.change_to == "UP" and not self.direction == "DOWN",
            self.change_to == "DOWN" and not self.direction == "UP")):
                # это условия нужно для того чтобы если змея идет направо мы не могли сказать ей идти в лево
            self.direction = self.change_to
        #any - or = , 
    def change_head_position(self):
        if self.direction == "RIGHT":
            self.snake_head_pos[0] += 10
        elif self.direction == "LEFT":
            self.snake_head_pos[0] -= 10
        elif self.direction == "UP":
            self.snake_head_pos[1] -= 10
        elif self.direction == "DOWN":
            self.snake_head_pos[1] += 10
        #changing the position 
    def change_body_position(
        self ,score,food_pos,screen_width,screen_height):
        self.snake_body.insert(0,list(self.snake_head_pos))
        if(self.snake_head_pos[0] == food_pos[0] and
        self.snake_head_pos[1] == food_pos[1]):
            food_pos = [random.randrange(1,screen_width/10)*10,
                        random.randrange(1,screen_height/10)*10]
            score += 1 
        else:
            self.snake_body.pop()
        return score,food_pos 
    
    def wall_collision(self,wall_position,game_over):
        for pos in wall_position:
            if (self.snake_head_pos[0] == pos[0] and 
                self.snake_head_pos[1] == pos[1]):
                game_over()
    
    def draw_snake(self,play_surface,surface_color):
        play_surface.fill(surface_color)
        for pos in self.snake_body:
            pygame.draw.rect(play_surface,self.snake_color,
                pygame.Rect(pos[0],pos[1],10,10))
    def check_for_collision(self,game_over,screen_width,screen_height):
        if any((
            self.snake_head_pos[0] > screen_width-10
            or self.snake_head_pos[0] < 0,
            self.snake_head_pos[1] > screen_height 
            or self.snake_head_pos[1] < 0
            )):
            game_over()
        for pos in self.snake_body[1:]:
            if (pos[0] == self.snake_head_pos[0]
                and pos[1] == self.snake_head_pos[1]):
                game_over()

class Food():
    def __init__(self,food_color,screen_width,screen_height):
        self.food_color = food_color
        self.food_size_x = 10 
        self.food_size_y = 10 
        self.food_pos = [random.randrange(1,screen_width/10)*10,
                        random.randrange(1,screen_height/10)*10]
    def draw_food(self,play_surface):
        pygame.draw.rect(play_surface,self.food_color,
                pygame.Rect(self.food_pos[0],self.food_pos[1],self.food_size_x,self.food_size_y))

def play_again():

    game = Game()
    snake = Snake(game.green)
    food = Food(game.brown,game.screen_width,game.screen_height)
    wall1 = Wall(game.blue)
    wall2 = Wall(game.blue)
    wall3 = Wall(game.blue)
    game.check_for_errors()
    game.set_surface()

    while True:
        snake.change_to = game.even_loop(snake.change_to)
        snake.direction_and_change()
        snake.change_head_position()

        snake.wall_collision(wall1.wall_position,game.game_over)
        snake.wall_collision(wall2.wall_position,game.game_over)
        snake.wall_collision(wall3.wall_position,game.game_over)

        game.score, food.food_pos = snake.change_body_position(
            game.score,food.food_pos,game.screen_width,game.screen_height)
        snake.draw_snake(game.play_surface,game.white)
        
        food.draw_food(game.play_surface)

        wall1.draw_walls(game.play_surface)
        wall2.draw_walls(game.play_surface)
        wall3.draw_walls(game.play_surface)

        snake.check_for_collision(
            game.game_over,game.screen_width,game.screen_height)

        pygame.draw.rect(game.play_surface, (64,128,255),
            (0,0,800,600), 10)

        game.show_score()
        if game.score >= 0 and game.score<1: 
            game.refresh_screen(20)
        elif game.score >= 1 and game.score <10:
            snake.wall_collision(wall4.wall_position,game.game_over)
            wall4.draw_walls(game.play_surface)
            game.refresh_screen(30)
        elif game.score >= 10 and game.score < 15:
            snake.wall_collision(wall5.wall_position,game.game_over)
            wall5.draw_walls(game.play_surface)
            game.refresh_screen(40)
        elif game.score >= 15 and game.score < 20:
            snake.wall_collision(wall6.wall_position,game.game_over)
            wall6.draw_walls(game.play_surface)
            game.refresh_screen(50)
        elif game.score >= 20 and game.score < 25:
            snake.wall_collision(wall7.wall_position,game.game_over)
            wall7.draw_walls(game.play_surface)
            game.refresh_screen(60)


game = Game()
snake = Snake(game.green)
food = Food(game.brown,game.screen_width,game.screen_height)

game.check_for_errors()
game.set_surface()

wall1 = Wall(game.blue)
wall2 = Wall(game.blue)
wall3 = Wall(game.blue)
wall4 = Wall(game.blue)
wall5 = Wall(game.blue)
wall6 = Wall(game.blue)
wall7 = Wall(game.blue)

def start_the_game():
   while True:
        snake.change_to = game.even_loop(snake.change_to)
        snake.direction_and_change()
        snake.change_head_position()
        
        snake.wall_collision(wall1.wall_position,game.game_over)
        snake.wall_collision(wall2.wall_position,game.game_over)
        snake.wall_collision(wall3.wall_position,game.game_over)

        game.score, food.food_pos = snake.change_body_position(
            game.score,food.food_pos,game.screen_width,game.screen_height)
        snake.draw_snake(game.play_surface,game.white)
        wall1.draw_walls(game.play_surface)
        wall2.draw_walls(game.play_surface)
        wall3.draw_walls(game.play_surface)
        food.draw_food(game.play_surface)

        snake.check_for_collision(
        game.game_over,game.screen_width,game.screen_height)
        pygame.draw.rect(game.play_surface, (64,128,255),
            (0,0,800,600), 10)
        game.show_score()
        
        if game.score >= 0 and game.score<1: 
            game.refresh_screen(20)
        elif game.score >= 1 and game.score <10:
            snake.wall_collision(wall4.wall_position,game.game_over)
            wall4.draw_walls(game.play_surface)
            game.refresh_screen(30)
        elif game.score >= 10 and game.score < 15:
            snake.wall_collision(wall5.wall_position,game.game_over)
            wall5.draw_walls(game.play_surface)
            game.refresh_screen(40)
        elif game.score >= 15 and game.score < 20:
            snake.wall_collision(wall6.wall_position,game.game_over)
            wall6.draw_walls(game.play_surface)
            game.refresh_screen(50)
        elif game.score >= 20 and game.score < 25:
            snake.wall_collision(wall7.wall_position,game.game_over)
            wall7.draw_walls(game.play_surface)
            game.refresh_screen(60)

menu = pygame_menu.Menu('Welcome', game.screen_width, game.screen_height,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='Player')
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(game.play_surface)