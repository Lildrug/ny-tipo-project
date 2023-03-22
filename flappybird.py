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
gift=pygame.image.load('/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/gift.png')
gift2=pygame.image.load('/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/gift.png')
gift3=pygame.image.load('/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/gift.png')
gift_rect=gift.get_rect()
gift2_rect=gift2.get_rect()
gift3_rect=gift3.get_rect()
bird=pygame.image.load('/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/standart.png')
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
fon=pygame.image.load('/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/fon34.jpg')
fon2=pygame.image.load('/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/fon34.jpg')
fon_rect=fon.get_rect()
fon2_rect=fon2.get_rect()
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
kolonna_rect.x=1000
kolonna4_rect.x=1000
kolonna5_rect.x=1500
kolonna2_rect.x=1500
kolonna3_rect.x=2000
kolonna6_rect.x=2000
fon_rect.x=0
fon2_rect.x=1920
gift_rect.x=kolonna_rect.x
gift2_rect.x=kolonna2_rect.x
gift3_rect.x=kolonna3_rect.x
gift_rect.y=(kolonna4_rect.y)-200
gift2_rect.y=(kolonna5_rect.y)-200
gift3_rect.y=(kolonna6_rect.y)-200
f1 = pygame.font.Font(None, 36)
f2 = pygame.font.Font(None, 36)
f3 = pygame.font.Font(None, 36)
f4 = pygame.font.Font(None, 36)
jump_force = 15 
move = jump_force+1
FPS = 60
clock = pygame.time.Clock()
schore=0
b=0
c=0
n=5
q=0
l=0
g=0
p=1
maxschore=0
while True:
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
    if fon_rect.x==0:
        fon2_rect.x=1920
    if fon2_rect.x==0:
        fon_rect.x=1920
    if a==1:
        fon_rect.x-=1
        fon2_rect.x-=1
        kolonna5_rect.x-=n
        kolonna_rect.x-=n
        kolonna2_rect.x-=n
        kolonna3_rect.x-=n
        kolonna4_rect.x-=n
        kolonna6_rect.x-=n
        gift_rect.x=kolonna_rect.x
        gift2_rect.x=kolonna2_rect.x
        gift3_rect.x=kolonna3_rect.x
        gift_rect.y=(kolonna4_rect.y)-200
        gift2_rect.y=(kolonna5_rect.y)-200
        gift3_rect.y=(kolonna6_rect.y)-200
    if schore%17==0 and schore!=0 and g==0:
            bird=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/bird2.png")
            p=1
            g=1
            q=0 
            kolonna_rect.x=-800
            kolonna2_rect.x=-200
            kolonna3_rect.x=300
            kolonna4_rect.x=-800
            kolonna5_rect.x=-200
            kolonna6_rect.x=300
    if schore%20==0 and schore!=0 and g==1 and schore!=20 :
            bird=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/standart.png")
            p=1
            g=0
            q=0
            kolonna_rect.x=1000
            kolonna2_rect.x=1500
            kolonna3_rect.x=2000
            kolonna4_rect.x=1000
            kolonna5_rect.x=1500
            kolonna6_rect.x=2000 
    if g==0:
        bird_rect.x=0
        n=5
        if kolonna_rect.x<=-100:
            kolonna_rect.x=1500
            kolonna4_rect.x=1500
            korda=random.randint(-690,0)
            korda4=korda+1000
            kolonna_rect.y=korda
            p=1
            kolonna4_rect.y=korda4
        if kolonna2_rect.x<=-100:
            kolonna2_rect.x=1500
            kolonna5_rect.x=1500
            korda2=random.randint(-690,0)
            korda5=korda2+1000  
            kolonna2_rect.y=korda2
            kolonna5_rect.y=korda5
            p=1
        if kolonna3_rect.x<=-100:
            kolonna3_rect.x=1500
            kolonna6_rect.x=1500
            korda3=random.randint(-690,0)
            korda6=korda3+1000
            kolonna3_rect.y=korda3
            kolonna6_rect.y=korda6
            p=1
            c=c+1
    elif g==1:
        bird_rect.x=1180
        n=-5
        if kolonna_rect.x>=1280:
            kolonna_rect.x=-300
            kolonna4_rect.x=-300
            korda=random.randint(-690,0)
            korda4=korda+1000
            kolonna_rect.y=korda
            kolonna4_rect.y=korda4
            p=1
        elif kolonna2_rect.x>=1280:
            kolonna2_rect.x=-300
            kolonna5_rect.x=-300
            korda2=random.randint(-690,0)
            korda5=korda2+1000  
            kolonna2_rect.y=korda2
            kolonna5_rect.y=korda5
            p=1
        elif kolonna3_rect.x>=1280:
            kolonna3_rect.x=-300
            kolonna6_rect.x=-300
            korda3=random.randint(-690,0)
            korda6=korda3+1000
            kolonna3_rect.y=korda3
            kolonna6_rect.y=korda6
            p=1
            c=c+1 
    #if a==1 and ((bird_rect.bottom==grass_rect.top or bird_rect.top==sc_rect.top) or kolonna_rect.colliderect(bird_rect) or kolonna2_rect.colliderect(bird_rect) or kolonna3_rect.colliderect(bird_rect) or kolonna4_rect.colliderect(bird_rect)  or kolonna5_rect.colliderect(bird_rect) or kolonna6_rect.colliderect(bird_rect)):
        #b=1
    if b==1:
        sc.fill(BLACK)
        if schore>maxschore:
            maxschore=schore
        text2 = f2.render('GOOD GAME BRO', 1, (180, 0, 0))
        text3=f3.render('Хочешь сыграть вновь? 1-Да 2-Нет',1,(180,0,0))
        text4=f4.render('Твой максимальный счёт:'+str(maxschore),1,(180,0,0))
        sc.blit(zxc,((W//2)-250,(H//2)-250))
        sc.blit(text2, ((W//2)-120, 900))
        sc.blit(text1,((W//2)-80, 800))
        sc.blit(text3,(450,100))
        sc.blit(text4,((W//2)-150,175))
        bird_rect.x=0
        bird=pygame.image.load('/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/standart.png')
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[49]:
            p=1
            q=0
            g=0
            n=5
            c=0
            schore=0
            a=0
            b=0
            fon_rect.x=0
            kolonna_rect.x=1000
            kolonna4_rect.x=1000
            kolonna5_rect.x=1500
            kolonna2_rect.x=1500
            kolonna3_rect.x=2000
            kolonna6_rect.x=2000
            gift_rect.x=kolonna_rect.x
            gift2_rect.x=kolonna2_rect.x
            gift3_rect.x=kolonna3_rect.x
            gift_rect.y=(kolonna4_rect.y)-200
            gift2_rect.y=(kolonna5_rect.y)-200
            gift3_rect.y=(kolonna6_rect.y)-200
        if keys[50]:
            break
    else:
        if gift_rect.colliderect(bird_rect):
            q=1
            if p==1:
                schore=schore+1
                p=0
        elif gift2_rect.colliderect(bird_rect):
            q=2
            if p==1:
                schore=schore+1
                p=0
        elif gift3_rect.colliderect(bird_rect):
            q=3
            if p==1:
                schore=schore+1
                p=0
        if c%2==0 and c!=0:
            n=n+1
        if c==4 and l==0:
            schore=schore+1
            l=1
        if c==0 and l==1:
            l=0
        sc.blit(fon,(fon_rect))
        sc.blit(fon2,(fon2_rect))
        if a==0:
            text2 = f2.render('Нажими SPACE для начала игры', 1, (0, 0, 0))
            sc.blit(text2,((W//2)-200,(H//2)))
        if q!=1:
            sc.blit(gift,(gift_rect))
        if q!=2:
            sc.blit(gift2,(gift2_rect))
        if q!=3:
            sc.blit(gift3,(gift3_rect))
        sc.blit(kolonna,(kolonna_rect))
        sc.blit(kolonna2,(kolonna2_rect))
        sc.blit(kolonna4,(kolonna4_rect))
        if c==3 and c!=0:
            kolonna3=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/gold.png")
            kolonna6=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/gold.png")
        else:
            kolonna3=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/столб.png")
            kolonna6=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/столб.png")
        sc.blit(kolonna,(kolonna_rect))
        sc.blit(kolonna2,(kolonna2_rect))
        sc.blit(kolonna4,(kolonna4_rect))
        sc.blit(kolonna3,(kolonna3_rect))
        sc.blit(kolonna6,(kolonna6_rect))
        sc.blit(kolonna5,(kolonna5_rect))
        sc.blit(bird,(bird_rect))
        sc.blit(text1, (10, 10))
        sc.blit(grass,grass_rect)
        clock.tick(FPS)
        pygame.display.update()