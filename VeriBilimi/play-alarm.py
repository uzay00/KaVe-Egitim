
import time

dk, sn = 0, 3
sure = 60 * dk + sn # bekleme suresi
time.sleep(sure - 2) 


import pygame
pygame.init()

pencere = pygame.display.set_mode((275,175)) # ((0, 0), pygame.FULLSCREEN) 
pencere.fill(pygame.Color(250,0,0, 128))

resim = pygame.image.load('veri/terminator2.jpg')



pygame.mixer.init()
pygame.mixer.music.load('veri/genisys.mp3')
pygame.mixer.music.play()



devam_et = True
while devam_et:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            devam_et = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            devam_et = False
    pencere.blit(resim,(0,0))
    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
quit()