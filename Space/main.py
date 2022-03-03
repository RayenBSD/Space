import pygame as pg
from pygame import mixer

pg.init()
screenHeight, screenWidth = 500, 900
screen = pg.display.set_mode((screenWidth, screenHeight))
pg.display.set_caption("Space")
icon = pg.image.load("PyGame/Space/spaceship_red.png")
pg.display.set_icon(icon)

#back ground music
mixer.music.load("PyGame/Space/background.wav")
mixer.music.play(-1)

#player1
player1X = 200
player1Y = 100
player1Health = 10
player1Score = 0

#player2
player2X = 650
player2Y = 300
player2Health = 10
player2Score = 0

#bullet
bullet1X = 750
bullet1Y = 750
bullet2X = 1000
bullet2Y = 1000

isShooted1 = False
isShooted2 = False

#Back Ground
bg = pg.image.load("PyGame/Space/space.png")
bgSize = pg.transform.scale(bg, (900, 500))
#Player 1
player1 = pg.image.load("PyGame/Space/spaceship_red.png")
player1_resize = pg.transform.rotate(pg.transform.scale(player1, (55, 40)), 90)
#Player 2
player2 = pg.image.load("PyGame/Space/spaceship_yellow.png")
player2_resize = pg.transform.rotate(pg.transform.scale(player2, (55, 40)), -90)
#Bullet 1
bullet1 = pg.image.load("PyGame/Space/bullet (1).png")
bullet2 = pg.transform.rotate(pg.image.load("PyGame/Space/bullet (1).png"), 180)

def redraw():
    global bgSize, player1_resize, player2_resize, player1X, player1Y, player2X, player2X, bullet1, bullet2, bullet1X, bullet1Y, bullet2X, bullet2Y, player1Health, player2Health, player2Score, player1Score

    screen.blit(bgSize, (0, 0))
    screen.blit(player1_resize, (player1X, player1Y))
    screen.blit(player2_resize, (player2X, player2Y))
    screen.blit(bullet1, (bullet1X, bullet1Y))
    screen.blit(bullet2, (bullet2X, bullet2Y))

    font = pg.font.Font("freesansbold.ttf", 32)
    health1 = font.render(f"Health1: {str(int(player1Health))}", True, (255, 255, 255))
    screen.blit(health1, (10, 0))

    health2 = font.render(f"Health2: {str(int(player2Health))}", True, (255, 255, 255))
    screen.blit(health2, (700, 0))

    score1 = font.render(f"Score1: {str(int(player1Score))}", True, (255, 255, 255))
    screen.blit(score1, (10, 30))

    score2 = font.render(f"Score2: {str(player2Score)}", True, (255, 255, 255))
    screen.blit(score2, (700, 30))

    pg.display.update()

def move():    
    global player1X, player1Y, player2X, player2Y, bullet1X, bullet1Y, bullet2X, bullet2Y, isShooted1, isShooted2, player1Health, player2Health, player2Score, player1Score
    step = 10
    keys = pg.key.get_pressed()
    #up
    if keys[pg.K_z] and player1Y - step> 0:
        player1Y -= step
    if keys[pg.K_UP] and player2Y - step> 0:
        player2Y -= step
    #down
    if keys[pg.K_s] and player1Y + step + 55 <= 500:
        player1Y += step
    if keys[pg.K_DOWN] and player2Y + step + 55 <= 500:
        player2Y += step
    #shoot
    if keys[pg.K_SPACE] and not isShooted1:
        laser1 = mixer.Sound("PyGame/Space/Gun+Silencer.mp3")
        laser1.play()
        isShooted1 = True
        bullet1Y = player1Y + 10
        bullet1X = player1X + 16     
    if (keys[pg.K_LEFT] or keys[pg.K_RIGHT]) and not isShooted2:
        laser2 = mixer.Sound("PyGame/Space/Gun+Silencer.mp3")
        laser2.play()
        isShooted2 = True
        bullet2X = player2X + 10
        bullet2Y = player2Y + 16

    if isShooted1 and bullet1X < screenWidth:
        bullet1X += step + 10
    else:
        isShooted1 = False   

    if isShooted2 and bullet2X > -32:
        bullet2X -= step + 10
    else:
        isShooted2 = False

    explosion = mixer.Sound("Pygame/Space/Grenade+1.mp3") 
    if (bullet1X >= player2X and bullet1X <= player2X + 32) and (bullet1Y >= player2Y and bullet1Y <= player2Y + 32):
        bullet1X, bullet1Y = 1000, 1000
        explosion.play()
        player2Health -= 1
    if (bullet2X <= player1X + 32 and bullet2X >= player1X) and (bullet2Y >= player1Y and bullet2Y <= player1Y + 32):
        bullet2X, bullet2Y = -1000, -1000
        explosion.play()
        player1Health -= 1

    #score
    if player1Health == 0:
        player1Health, player2Health = 10, 10
        player2Score += 1
    if player2Health == 0:
        player1Health, player2Health = 10, 10
        player1Score += 1

def main():
    while True:
        pg.time.delay(50)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
        redraw()
        move()
    
if __name__ == "__main__":
    main()