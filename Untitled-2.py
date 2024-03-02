import pygame
import random
#Количество начальных объектов
rnd_count = random.randint(10, 50)
STARTING_BLUE_BLOBS = rnd_count
STARTING_RED_BLOBS = rnd_count
STARTING_GREEN_BLOBS = rnd_count
STARTING_ORANGE_BLOBS = rnd_count
STARTING_CYAN_BLOBS = rnd_count
STARTING_PURPLE_BLOBS = rnd_count
STARTING_YELLOW_BLOBS = rnd_count
#Ширина и высота экрана
WIDTH = 800
HEIGHT = 600
#Доступные цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255,165,0)
YELLOW = (255,255,0)
PURPLE = (139,0,255)
CYAN = (66,170,255)
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()
class Blob:
    def __init__(self, color):
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        #Размеры объекта
        self.size = random.randrange(10, 25)
        self.color = color
    def move(self):
        #Скорость передвижение объекта
        self.move_x = random.randrange(-1,2)
        self.move_y = random.randrange(-1,2)
        self.x += self.move_x
        self.y += self.move_y
        if self.x < 0: self.x = 0
        elif self.x > WIDTH: self.x = WIDTH
        
        if self.y < 0: self.y = 0
        elif self.y > HEIGHT: self.y = HEIGHT
def draw_environment(blob_list):
    game_display.fill(WHITE)
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
    pygame.display.update()
    
def main():
    #Виды объектов
    blue_blobs = dict(enumerate([Blob(BLUE) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([Blob(RED) for i in range(STARTING_RED_BLOBS)]))
    green_blobs = dict(enumerate([Blob(GREEN) for i in range(STARTING_GREEN_BLOBS)]))
    orange_blobs = dict(enumerate([Blob(ORANGE) for i in range(STARTING_ORANGE_BLOBS)]))
    cyan_blobs = dict(enumerate([Blob(CYAN) for i in range(STARTING_CYAN_BLOBS)]))
    purple_blobs = dict(enumerate([Blob(PURPLE) for i in range(STARTING_PURPLE_BLOBS)]))
    yellow_blobs = dict(enumerate([Blob(YELLOW) for i in range(STARTING_YELLOW_BLOBS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment([blue_blobs,red_blobs,green_blobs, orange_blobs,cyan_blobs,purple_blobs,yellow_blobs])
        #Кадры в секунду
        clock.tick(60)
if __name__ == '__main__':
    main() 