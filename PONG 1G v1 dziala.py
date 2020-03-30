import sys,pygame
from pygame.locals import *

pygame.init()

pygame.display.set_caption("PONG 1G")

okno = pygame.display.set_mode((800,600),pygame.RESIZABLE)

'''wynik'''
wynik = 0
czcionka = pygame.font.SysFont("comicsansms",20)
def punkty():
    tekst = czcionka.render(str(wynik),True,(255,255,255))
    tekst_dane = tekst.get_rect()
    tekst_dane.center = (750,30)
    okno.blit(tekst,tekst_dane)
              
'''paletka'''
belka = pygame.Surface((80,20))
belka.fill((220,211,182))
bxy = belka.get_rect()
bxy.x = 100
bxy.y = 50
bx = 0
tmp1 = bxy.x

'''pilka'''
pilka = pygame.Surface((30,30))
pilka.fill((255,69,0))
pxy = pilka.get_rect()
pxy.x = 300
pxy.y = 300
px,py = 3, 3

pygame.display.flip()
fps = pygame.time.Clock()
while 1:
    for i in pygame.event.get():
        if i.type == QUIT:
            sys.exit(0)
        if i.type == KEYDOWN:
            if i.key == K_d:
                bx = 5
            if i.key == K_a:
                bx = -5
        if i.type == KEYUP:
            bx = 0
    okno.fill((100,100,100))
    '''przsuwanie paletki'''
    if (bxy.x > 720):
        bx = -1
    elif (bxy.x <0):
        bx = 1
    bxy.x += bx
    

    '''przesuwanie pilki'''
    pxy.x += px
    if pxy.x > 770 or pxy.x < 0:
        px *= -1
    pxy.y += py
    if pxy.y > 570:
        py *= -1
    elif pxy.y < 0:
        wynik -= 5
        py *= -1
        pxy.x = 300
        pxy.y = 300
    '''kolizja z paletka'''
    if bxy.colliderect(pxy):
        py = 3
        wynik += 1
        
    okno.blit(belka,bxy)
    okno.blit(pilka,pxy)
    punkty()
    pygame.display.update()
    fps.tick(60)
