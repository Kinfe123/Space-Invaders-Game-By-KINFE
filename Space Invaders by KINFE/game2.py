import pygame
import random
import math
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((800 , 600))
icon = pygame.image.load("Space Invaders 3.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("SPACE INVADERS GAME BY KINFE")
backgroundImg = pygame.image.load("background.jpg")
playerImg = pygame.image.load("space-invaders.png")
screenWidth = 800
screenHeight = 600
playerX = 370
playerY = 490
playerVel = 3
enemyImg = []#reserving the space for list to loop through
enemyX = []#reserving the space for list to loop through
enemyY = []#reserving the space for list to loop through
enemyChangeX = []#reserving the space for list to loop through
enemyChangeY = []#reserving the space for list to loop through
numberOfTheEnemy = 7
for i in range(numberOfTheEnemy):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0 , 735))
    enemyY.append(random.randint(50 , 150))
    enemyChangeX.append(3)
    enemyChangeY.append(40)
bulletImg = pygame.image.load("bullet.png")
bulletY = 0
bulletX = 0
bulletChangeY = 10
bulletState = "ready"
mixer.music.load("bgmusic.wav")
mixer.music.play(-1)
score_value = 0
font2 = pygame.font.Font("lemon.ttf" , 12)
font2X = 590
font2Y = 580

font = pygame.font.Font("Angels.ttf" , 15)
fontX = 10
fontY = 10
text = pygame.font.Font("Bristone.ttf" , 50)
text2 = pygame.font.Font("lemon.ttf" , 25)
def gameOverTxtAgain():
    gameOverText = text2.render(f"=>Score: {score_value}" , True , (255 , 255 , 20))
    screen.blit(gameOverText , (260 , 300))
    

def gameOver():
    gameOvrTxt = text.render(f"GAME OVER" , True , (255 , 255 , 20))
    screen.blit(gameOvrTxt , (200 , 230))
    
def abtMeDis(x , y):
    about = font2.render("dev By-KINFE MICAHEL TARIKU" , True , (0 , 0 ,0))
    screen.blit(about , (x , y))
def fontDisplay(x , y):
    score = font.render(f"Your score: {score_value}" ,True , (255 , 255 , 15))#formatted string or formatted specifier
    screen.blit(score, (x , y))
#the comment has been in the case of the

def play(x , y):
    screen.blit(playerImg , (x , y))
def enemy(x , y , i):
    screen.blit(enemyImg[i] , (x , y))
def bullet( x , y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg , (x+16 , y+10))
def isCollide(enemyX , enemyY , bulletX , bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX , 2)) + (math.pow(enemyY - bulletY , 2)))
    if distance < 27:
        return True
    else:
        return False


run = True
while run:
    screen.fill((255 , 255 , 14))
    screen.blit(backgroundImg , (0 , 0)) 
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for i in range(numberOfTheEnemy):
        if enemyY[i] > 440:
            for j in range(numberOfTheEnemy):
                enemyY[j] = 4000
            gameOver()
            gameOverTxtAgain()
            break
            
        enemyX[i]+=enemyChangeX[i]
        if enemyX[i]<=0:
            enemyChangeX[i]= 3
            enemyY[i]+=enemyChangeY[i]
        if enemyX[i] >= 730:
            enemyChangeX[i] =-3 
            enemyY[i]+=enemyChangeY[i]
            
        collision =  isCollide(enemyX[i] , enemyY[i] , bulletX , bulletY)
        if collision:
            collideSound = mixer.Sound("hit.wav")
            collideSound.play()
            
            bulletY = 480
            bulletState = "ready"
            score_value += 1
            
        
            enemyX[i]  = random.randint(0 ,735)
            enemyY[i] =  random.randint(50 , 150)
            
        enemy(enemyX[i] , enemyY[i] , i)
     
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and playerX>=0:
        playerX-=playerVel
    if keys[pygame.K_SPACE]:
        if bulletState == "ready":
             bulletSound = mixer.Sound("shot.wav")
             bulletSound.play()
             bulletX = playerX
             bulletY = playerY
             bullet(bulletX , bulletY)
       
        
        
    if keys[pygame.K_RIGHT] and playerX <= screenWidth - 70:#for the image
        playerX+=playerVel
    if keys[pygame. K_UP] and playerY>=0:
        playerY-=playerVel
    if keys[pygame.K_DOWN] and playerY<=screenHeight - 70:
        playerY+=playerVel  
    
    if bulletY == 0:
        
        bulletState = "ready"
      
    if bulletState == "fire":
        bullet(bulletX , bulletY)
        bulletY-=bulletChangeY    
    
    
        
    
   
    
    play(playerX , playerY)
    abtMeDis(font2X , font2Y)
   
    fontDisplay(fontX , fontY)
    
    
    pygame.display.update()
             
