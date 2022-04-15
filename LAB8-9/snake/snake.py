import random, pygame, time, sys
from tkinter import W

pygame.init()
resolution = (500,500)
screen = pygame.display.set_mode(resolution)
game_over = pygame.font.SysFont("Verdana", 60).render("Game Over", True, (255, 255, 255))

def create_rect(width, height, border, color, border_color):
    surf = pygame.Surface((width+border*2, height+border*2), pygame.SRCALPHA)
    pygame.draw.rect(surf, color, (border, border, width, height), 0)
    for i in range(1, border):
        pygame.draw.rect(surf, border_color, (border-i, border-i, width+5, height+5), 1)
    return surf

def game_end():
    screen.blit(game_over, (75, 190))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    sys.exit()
class Snake:
    def __init__(self, x, y):
        self.score = 0
        self.is_alive = True
        self.level = 1
        self.size = 1
        self.elements = [[x, y]]  # [[x0, y0], [x1, y1], [x2, y2] ...] (i) -> (i - 1)
        self.radius = 10
        self.dx = 0  # Right/Left
        self.dy = 0  # Up/Down
        self.is_add = False
        self.speed = 30

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (255, 0, 0), element, self.radius)

    def add_to_snake(self,food_size=3):
        self.size += food_size
        for element in range(food_size):
            self.elements.append([0, 0])
        self.is_add = False
        if self.size % 5 == 0:
            self.speed += 10
    def walls(self):
        if self.level>1:
            return True

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        #to avoid to going out for infinity
        if self.level>1:
            if self.elements[0][0] >= 70 and self.elements[0][0] <= 170 and self.elements[0][1] >= 70 and self.elements[0][1] <= 170:
                self.is_alive = False
                game_end()
            elif self.elements[0][0] >= 250 and self.elements[0][0] <= 350 and self.elements[0][1] >= 250 and self.elements[0][1] <= 350:
                self.is_alive=False
                game_end()
        if (self.elements[0][0] == 20):
            game_end()            
        if (self.elements[0][0] == resolution[0]-20):
            game_end()
        if (self.elements[0][1] == 20):
            game_end()
        if(self.elements[0][1] == resolution[1]-20):
            game_end()
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy
        #print(self.elements[0])

    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]
        if foodx <= x <= foodx + 20 and foody <= y <= foody + 20:
            return True
        return False
    

border_res = (20,480)
class Food:
    def __init__(self,food_size,is_exist=True):
        self.is_exist = is_exist
        self.food_size = food_size
        self.x = random.randint(border_res[0],border_res[1])
        self.y = random.randint(border_res[0],border_res[1])

    def gen(self):
        self.x = random.randint(border_res[0],border_res[1])
        self.y = random.randint(border_res[0],border_res[1])

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 10+self.food_size, 10 + self.food_size))


border = create_rect(485, 485, 10, (0, 0, 0),(255, 255, 255))
snake1 = Snake(250, 250)
food = Food(1)
bonus = Food(5,False)

running = True

#Good flow
snake_frame_speed = 5
frame_counter = 0
FPS = 120

d = 5

clock = pygame.time.Clock()

spawn_status = True

spawn_bonus = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_bonus, 4000)
spawn_pause = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_pause, 5000)

start_pos = 250
snake = [(start_pos,start_pos)]
spawn_status = False

while running:
    frame_counter+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawn_bonus:
            bonus.gen()
            if bonus.is_exist:
                bonus.is_exist = False
            elif bonus.is_exist == False:
                bonus.is_exist=True
            spawn_status = True
            
        """if event.type == spawn_pause  and bonus.is_exist==False and spawn_status==True:
            print("Spawn pause!!!!!!!!!!!!!!!!!")
            spawn_status = False"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # if event.key == pygame.K_SPACE:
            #     snake1.is_add = True
            #     snake2.is_add = True
            if event.key == pygame.K_RIGHT and snake1.dx != -d:
                snake1.dx = d
                snake1.dy = 0
            if event.key == pygame.K_LEFT and snake1.dx != d:
                snake1.dx = -d
                snake1.dy = 0
            if event.key == pygame.K_UP and snake1.dy != d:
                snake1.dx = 0
                snake1.dy = -d
            if event.key == pygame.K_DOWN and snake1.dy != -d:
                snake1.dx = 0
                snake1.dy = d

    if snake1.eat(food.x, food.y):
        snake1.is_add = True
        snake1.score+=3
        food.gen()
    if snake1.eat(bonus.x, bonus.y):
        snake1.is_add = True
        bonus.is_exist = False
        snake1.score+=1
    
    #if len(snake1.elements)
    #[pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.food_size, self.food_size))]
    if frame_counter%snake_frame_speed==0:
        if snake1.score>20:
            snake1.level +=1
        print(snake1.size)
        screen.fill((0, 0, 0))
        screen.blit(border,(0,0))
        if (snake1.walls()):
            print("level more 2")
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(70, 70, 100, 100)) # 70 - 170
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(250, 250, 100, 100)) #250 - 350
        snake1.move()    
        snake1.draw()
        food.draw()
        scores = pygame.font.SysFont("Verdana", 10).render(str(snake1.score), True, (0, 0, 0))
        screen.blit(scores,(0,0))
        if bonus.is_exist:
            bonus.draw()
        
    

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()