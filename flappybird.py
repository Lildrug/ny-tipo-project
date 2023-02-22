import pygame
pygame.init()
W = 1280
H = 1024
BLUE = (0, 0, 255)
BLACK=(0,0,0)
a=0
korda2=900
sc = pygame.display.set_mode((W, H))
bird=pygame.image.load('/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/bird.png')
bird_rect=bird.get_rect()
grass=pygame.image.load('/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/2.png')
grass_rect=grass.get_rect()
sc_rect=sc.get_rect()
kolonna=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/1.png")
kolonna2=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/1.png")
kolonna3=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/1.png")
kolonna4=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/1.png")
kolonna5=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/1.png")
kolonna6=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/1.png")
kolonna7=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/1.png")
kolonna8=pygame.image.load("/home/Sokolov_Kirill/Рабочий стол/flappy bird/picture/1.png")
grass_rect.bottom=sc_rect.bottom
bird_rect.bottom=grass_rect.top
kolonna_rect=kolonna.get_rect()
kolonna2_rect=kolonna2.get_rect()
kolonna3_rect=kolonna3.get_rect()
kolonna5_rect=kolonna5.get_rect()
kolonna6_rect=kolonna6.get_rect()
kolonna7_rect=kolonna7.get_rect()
kolonna_rect.x=900
kolonna5_rect.x=900
kolonna2_rect.x=900
kolonna3_rect.x=900
kolonna6_rect.x=900
kolonna7_rect.x=900
kolonna_rect.top=sc_rect.top
kolonna2_rect.top=kolonna_rect.bottom
kolonna3_rect.top=kolonna2_rect.bottom
kolonna5_rect.bottom=grass_rect.top
kolonna6_rect.bottom=kolonna5_rect.top
kolonna7_rect.bottom=kolonna6_rect.top
f1 = pygame.font.Font(None, 36)
f2 = pygame.font.Font(None, 36)
jump_force = 15 
move = jump_force+1
FPS = 60
clock = pygame.time.Clock()
schore=0
while True:
    kolonna5_rect.x-=5
    kolonna_rect.x-=5
    kolonna2_rect.x-=5
    kolonna3_rect.x-=5
    kolonna7_rect.x-=5
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
                schore=schore+1
    keys = pygame.key.get_pressed()
    if move<=jump_force:
        if bird_rect.bottom+move<grass_rect.top:
            bird_rect.bottom+=move
            if move<jump_force:
                move+=1
        else:
            bird_rect.bottom=grass_rect.top
            move=jump_force+1
    if (bird_rect.bottom==grass_rect.top or bird_rect.top<=0 or bird_rect.right==kolonna3_rect.left or bird_rect.right==kolonna7_rect) and a==1:
        while True:
            sc.fill(BLACK)
            text2 = f2.render('GOOD GAME BRO', 1, (180, 0, 0))
            sc.blit(text2, ((W//2)-100, (H//2)-50))
            pygame.display.update()
            schore=schore+1
            if schore==1000:
                exit()
    sc.fill(BLUE)
    sc.blit(kolonna,(kolonna_rect))
    sc.blit(kolonna2,(kolonna2_rect))
    sc.blit(kolonna3,(kolonna3_rect))
    sc.blit(kolonna5,(kolonna5_rect))
    sc.blit(kolonna6,(kolonna6_rect))
    sc.blit(kolonna7,(kolonna7_rect))
    sc.blit(text1, (10, 10))
    sc.blit(bird, bird_rect)
    sc.blit(grass,grass_rect)
    clock.tick(FPS)
    pygame.display.update()
    #fcdsfcds