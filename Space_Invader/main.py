#Basic pygame structure

import pygame
import random
import math
from pygame import mixer
pygame.init()

screen = pygame.display.set_mode((800, 600))


background = pygame.image.load("C:\\Users\Dell\\OneDrive\\Documents\\CODING\\PYTHON\\Mega Project\\Space_Invader\\bg.jpg")
















#screen width and height
pygame.display.set_caption("Space Ship")#screen name
icon = pygame.image.load("C:\\Users\\Dell\\OneDrive\\Documents\\CODING\\PYTHON\\Mega Project\\Space_Invader\\cricket.png")#screen logo
pygame.display.set_icon(icon)

player = pygame.image.load("C:\\Users\\Dell\\OneDrive\\Documents\\CODING\\PYTHON\\Mega Project\\Space_Invader\\Main.png")#loading player image

playerX = 370
playerY = 480
playerXchange = 0







enemies = pygame.image.load("C:\\Users\\Dell\\OneDrive\\Documents\\CODING\\PYTHON\\Mega Project\\Space_Invader\\invader.png")#loading enemy image

enemyX = random.randint(0, 735)
enemyY = random.randint(50,150)
enemyXchange = 0.3
enemyYchange = 40


bullets = pygame.image.load("C:\\Users\\Dell\\OneDrive\\Documents\\CODING\\PYTHON\\Mega Project\\Space_Invader\\bullet.png")#loading bullet image

bulletY = 480
bulletXchange = 0
bulletYchange = 1.25
bulletX = 0
bullet_state = "ready"#if bullet_state == "ready" then we can shoot


score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)
textX = 10
textY = 10





ovr_font = pygame.font.Font("freesansbold.ttf",64)

def game_over():
    over_text = ovr_font.render("Game Over", True , (255, 255, 255))
    screen.blit(over_text,(200, 250))
    pygame.quit()


def showscore(x, y):
    score = font.render("Score: "+ str(score_value), True , (255, 255, 255))
    screen.blit(score,(x, y)) 




def players(x, y):
    screen.blit(player, (x, y))
    
def enemy(x, y):
    screen.blit(enemies, (x, y))
    

    
def fire_bullet(x, y):
    global bullet_state #making bullet state global variable
    bullet_state = "fire" 
    screen.blit(bullets, (x+16, y+10))
    


life_value = 3
font1 = pygame.font.Font("freesansbold.ttf",32)
text1X = 640
text1Y = 10

def show(x, y):
    life = font1.render("Bullets: "+ str(life_value), True, (255, 255, 255) )
    screen.blit(life, (x, y))


    
    
def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance =  math.sqrt((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY - bulletY,2)))
    if distance < 27:
        return True
    else:
        return False
    
    
t = True

while t:
    
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            t = False
            pygame.quit()#closing window
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -0.7
            if event.key == pygame.K_RIGHT:
                playerXchange = 0.7
            if event.key == pygame.K_SPACE :
                if bullet_state is "ready":
                    bulsound = mixer.Sound("C:\\Users\\Dell\\OneDrive\\Documents\\CODING\\PYTHON\\Mega Project\\Space_Invader\\laser.wav")
                    bulsound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                    
                
                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0
    
    
    
    
    playerX += playerXchange
    
    
    if playerX <= 0:
        playerX =0
    if playerX >= 736:
        playerX = 736
        
    if enemyY>440 or life_value == 0:
        enemyY = 2000
        game_over()
           
        
    enemyX += enemyXchange
    
    
    if enemyX <= 0:
        enemyXchange = 0.3
        enemyY += enemyYchange
    if enemyX >= 736:
        enemyXchange = -0.3
        enemyY += enemyYchange
        
        
        
    #bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletYchange  
    if bulletY <= 40 :
        bulletY = 480
        bullet_state = "ready"
        life_value -= 1
            
    #collision detection
    collision = iscollision(enemyX, enemyY, bulletX, bulletY)   
    if collision:
        esound = mixer.Sound("C:\\Users\\Dell\\OneDrive\\Documents\\CODING\\PYTHON\\Mega Project\\Space_Invader\\explosion.wav")
        esound.play()
        bulletY = 480
        bullet_state = "ready"
        
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50,150)
        
        
        score_value += 1
            
        
    players(playerX, playerY)
    enemy(enemyX, enemyY)
    showscore(textX, textY)
    show(text1X, text1Y)
    pygame.display.update()
