import pygame
pygame.init()
W = 1280
H = 1024
BLUE = (0, 0, 255)
BLACK=(0,0,0)
a=0
sc = pygame.display.set_mode((W, H))
bird=pygame.image.load('bird.png')
bird_rect=bird.get_rect()
grass=pygame.image.load('2.png')
grass_rect=grass.get_rect()
sc_rect=sc.get_rect()
kolonna=pygame.image.load("pixil-frame-0(4).png")
kolonna2=pygame.image.load("pixil-frame-0(4).png")
kolonna3=pygame.image.load("pixil-frame-0(4).png")
kolonna4=pygame.image.load("pixil-frame-0(4).png")
grass_rect.bottom=sc_rect.bottom
bird_rect.bottom=grass_rect.top
kolonna_rect=kolonna.get_rect()
kolonna2_rect=kolonna2.get_rect()
kolonna4_rect=kolonna4.get_rect()
kolonna3_rect=kolonna3.get_rect()
kolonna2_rect.top=kolonna_rect.bottom
kolonna4_rect.top=kolonna3_rect.bottom
f1 = pygame.font.Font(None, 36)
f2 = pygame.font.Font(None, 36)
jump_force = 15 
move = jump_force+1
FPS = 60
clock = pygame.time.Clock()
schore=0
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
    if (bird_rect.bottom==grass_rect.top or bird_rect.top<=0) and a==1:
        while True:
            sc.fill(BLACK)
            text2 = f2.render('GOOD GAME BRO', 1, (180, 0, 0))
            sc.blit(text2, ((W//2)-100, (H//2)-50))
            pygame.display.update()
            schore=schore+1
            if schore==1000:
                exit()
    sc.fill(BLUE)
    sc.blit(text1, (10, 10))
    sc.blit(bird, bird_rect)
    sc.blit(grass,grass_rect)
    clock.tick(FPS)
    pygame.display.update()