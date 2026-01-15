import pygame
import time
import random
pygame.font.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BG = pygame.transform.scale(pygame.image.load("rain_dodge/bg.jpeg"), (SCREEN_WIDTH, SCREEN_HEIGHT)) #Pass an image and a size to scale it to
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3
POINT_WIDTH = 20
POINT_HEIGHT = 30
POINT_VEL = 5
FONT = pygame.font.SysFont("comicsans", 30) #Font, size

pygame.display.set_caption("Space Dodge") #Name of the Window

def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0)) #blit takes an image and a starting coordinate and puts it on the window

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white") #String, antialiasing, color
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "white", player) #Where to draw it, what color (string or RGB), what rectangle

    for star in stars:
        pygame.draw.rect(WIN, "red", star)

    pygame.display.update() #updates the screen and applys the background

def main():
    run = True
    player = pygame.Rect(200, SCREEN_HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT ) #Starting X, Starting Y, Rect Width, Rect Height
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    star_add_increment = 2000
    star_count = 0
    stars = []
    point_add_increment = 2000
    point_count = 0
    points = []
    hit = False
    score = 0

    while run:
        tick += clock.tick(60) #How many times the while loop runs per second needs the clock object to be made
        star_count += tick
        point_count += tick
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range (3):
                star_x = random.randint(0, SCREEN_WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        if point_count > point_add_increment:
            point_x = random.randint(0, SCREEN_WIDTH - POINT_WIDTH)
            point = pygame.Rect(point_x, -POINT_HEIGHT, POINT_WIDTH, POINT_HEIGHT)
            points.append(point)
            point_add_increment = max(200, point_add_increment - 50)
            point_count = 0
        
        #if score_count =

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        elif keys[pygame.K_RIGHT] and player.x + PLAYER_WIDTH + PLAYER_VEL <= SCREEN_WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]: #Colon in the brackets makes a copy of the list, since list will be edited in the loop
            star.y += STAR_VEL
            if star.y > SCREEN_HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        for point in points[:]:
            point.y += POINT_VEL
            if point.y > SCREEN_HEIGHT:

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (SCREEN_WIDTH/2 - lost_text.get_width()/2, SCREEN_HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break



        draw(player, elapsed_time, stars, points)

    pygame.quit

if __name__ == "__main__":
    main()