import pygame
import random
pygame.init()
W = 1280
H = 1024
BLUE = (0, 0, 255)
BLACK=(0,0,0)
a=0
korda=random.randint(-690,0)
korda2=random.randint(-690,0)
korda3=random.randint(-690,0)
korda4=100+korda
korda5=100+korda2
korda6=100+korda3
sc = pygame.display.set_mode((W, H))
bird=pygame.image.load('/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/bird.png')
zxc=pygame.image.load('/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/zxc.jpg')
bird_rect=bird.get_rect()
grass=pygame.image.load('/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/2.png')
grass=pygame.transform.scale(grass,(grass.get_rect().width*15, grass.get_rect().height//2))
grass_rect=grass.get_rect()
sc_rect=sc.get_rect()
kolonna=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/столб.png")
kolonna2=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/столб.png")
kolonna3=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/столб.png")
kolonna4=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/столб.png")
kolonna5=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/столб.png")
kolonna6=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/столб.png")
grass_rect.bottom=sc_rect.bottom
bird_rect.bottom=grass_rect.top
kolonna_rect=kolonna.get_rect()
kolonna2_rect=kolonna2.get_rect()
kolonna3_rect=kolonna3.get_rect()
kolonna5_rect=kolonna5.get_rect()
kolonna6_rect=kolonna6.get_rect()
kolonna4_rect=kolonna4.get_rect()
korda=random.randint(-690,0)
korda2=random.randint(-690,0)
korda3=random.randint(-690,0)
korda4=korda+1000
korda5=korda2+1000
korda6=korda3+1000
kolonna_rect.y=korda
kolonna2_rect.y=korda2
kolonna3_rect.y=korda3
kolonna4_rect.y=korda4
kolonna5_rect.y=korda5
kolonna6_rect.y=korda6
kolonna_rect.x=900
kolonna4_rect.x=900
kolonna5_rect.x=1500
kolonna2_rect.x=1500
kolonna3_rect.x=2100
kolonna6_rect.x=2100
f1 = pygame.font.Font(None, 36)
f2 = pygame.font.Font(None, 36)
f3 = pygame.font.Font(None, 36)
jump_force = 15 
move = jump_force+1
FPS = 60
clock = pygame.time.Clock()
schore=0
b=1
while True:
    kolonna5_rect.x-=5
    kolonna_rect.x-=5
    kolonna2_rect.x-=5
    kolonna3_rect.x-=5
    kolonna4_rect.x-=5
    kolonna6_rect.x-=5  
    text1 = f1.render('Твой счёт:'+str(schore), 1, (180, 0, 0))
    sc.blit(text1, (10, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                move= -jump_force
                a=1
    if move<=jump_force:
        if bird_rect.bottom+move<grass_rect.top:
            bird_rect.bottom+=move
            if move<jump_force:
                move+=1
        else:
            bird_rect.bottom=grass_rect.top
            move=jump_force+1
    if kolonna_rect.x<=-100:
        kolonna_rect.x=1500
        kolonna4_rect.x=1500
        korda=random.randint(-690,0)
        korda4=korda+1000
        kolonna_rect.y=korda
        kolonna4_rect.y=korda4
    if kolonna2_rect.x<=-100:
        kolonna2_rect.x=1500
        kolonna5_rect.x=1500
        korda2=random.randint(-690,0)
        korda5=korda2+1000
        kolonna2_rect.y=korda2
        kolonna5_rect.y=korda5
    if kolonna3_rect.x<=-100:
        kolonna3_rect.x=1500
        kolonna6_rect.x=1500
        korda3=random.randint(-690,0)
        korda6=korda3+1000
        kolonna3_rect.y=korda3
        kolonna6_rect.y=korda6
    if kolonna_rect.x==0 or kolonna2_rect.x==0 or kolonna3_rect.x==0:
        schore=schore+1
    if a==1 and ((bird_rect.bottom==grass_rect.top or bird_rect.top==sc_rect.top) or kolonna_rect.collidepoint(bird_rect.topright) or kolonna2_rect.collidepoint(bird_rect.topright) or kolonna3_rect.collidepoint(bird_rect.topright) or kolonna4_rect.collidepoint(bird_rect.topright)  or kolonna5_rect.collidepoint(bird_rect.topright) or kolonna6_rect.collidepoint(bird_rect.topright)):
        sc.fill(BLACK)
        text2 = f2.render('GOOD GAME BRO', 1, (180, 0, 0))
        text3=f3.render('Хочешь сыграть вновь? 1-Да 2-Нет',1,(180,0,0))
        sc.blit(zxc,((W//2)-250,(H//2)-250))
        sc.blit(text2, ((W//2)-100, 900))
        sc.blit(text1,((W//2)-50, 800))
        sc.blit(text3,(400,100))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[49]:
            schore=0
            a=0
            kolonna_rect.x=900
            kolonna4_rect.x=900
            kolonna5_rect.x=1500
            kolonna2_rect.x=1500
            kolonna3_rect.x=2100
            kolonna6_rect.x=2100
        if keys[50]:
            break
    if a==1 and ((bird_rect.bottom==grass_rect.top or bird_rect.top==sc_rect.top) or kolonna_rect.collidepoint(bird_rect.bottomleft) or kolonna2_rect.collidepoint(bird_rect.bottomleft) or kolonna3_rect.collidepoint(bird_rect.bottomleft) or kolonna4_rect.collidepoint(bird_rect.bottomleft)  or kolonna5_rect.collidepoint(bird_rect.bottomleft) or kolonna6_rect.collidepoint(bird_rect.bottomleft)):
        sc.fill(BLACK)
        text2 = f2.render('GOOD GAME BRO', 1, (180, 0, 0))
        text3=f3.render('Хочешь сыграть вновь? 1-Да 2-Нет',1,(180,0,0))
        sc.blit(zxc,((W//2)-250,(H//2)-250))
        sc.blit(text2, ((W//2)-100, 900))
        sc.blit(text1,((W//2)-50, 800))
        sc.blit(text3,(400,100))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[49]:
            schore=0
            a=0
            kolonna_rect.x=900
            kolonna4_rect.x=900
            kolonna5_rect.x=1500
            kolonna2_rect.x=1500
            kolonna3_rect.x=2100
            kolonna6_rect.x=2100
        if keys[50]:
            break
    sc.fill(BLUE)
    sc.blit(kolonna,(kolonna_rect))
    sc.blit(kolonna2,(kolonna2_rect))
    sc.blit(kolonna3,(kolonna3_rect))
    sc.blit(kolonna4,(kolonna4_rect))
    sc.blit(kolonna5,(kolonna5_rect))
    sc.blit(kolonna6,(kolonna6_rect))
    sc.blit(text1, (10, 10))
    sc.blit(bird, bird_rect)
    sc.blit(grass,grass_rect)
    clock.tick(FPS)
    pygame.display.update() 