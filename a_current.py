import pygame
pygame.init()
screen = pygame.display.set_mode((1024, 720))
clock = pygame.time.Clock()
running = True

#Player
player = pygame.image.load('/Users/luskousko/Desktop/Work/pics_pygame/cat.png').convert_alpha()
player = pygame.transform.scale(player,(100,100))
flipping_player = player


#Weapons
lightsaber = pygame.image.load('/Users/luskousko/Desktop/Work/pics_pygame/lightsaber.png').convert_alpha()
lightsaber = pygame.transform.scale(lightsaber,(80,80))
lightsaber = pygame.transform.rotate(lightsaber,225)


#Variables 
player_x = 0
player_y = 0
angle = 0
tocenie_meca = False
rychlost = 8
pohyb_hore = False
pohyb_dole = False
pohyb_doprava = False
pohyb_dolava = False


def spracuj_keydown(event):
    global pohyb_hore, pohyb_dole, pohyb_doprava, pohyb_dolava, tocenie_meca
    if event.key == pygame.K_w:
        pohyb_hore = True
    if event.key == pygame.K_s:
        pohyb_dole = True
    if event.key == pygame.K_a:
        pohyb_dolava = True
    if event.key == pygame.K_d:
        pohyb_doprava = True
    if event.key == pygame.K_SPACE:
        tocenie_meca = True


def spracuj_keyup(event):
    global pohyb_hore, pohyb_dole, pohyb_doprava, pohyb_dolava,  tocenie_meca
    if event.key == pygame.K_w:
        pohyb_hore = False
    if event.key == pygame.K_s:
        pohyb_dole = False
    if event.key == pygame.K_a:
        pohyb_dolava = False
    if event.key == pygame.K_d:
        pohyb_doprava = False
    if event.key == pygame.K_SPACE:
        tocenie_meca = False


def pohyb_hraca():
    global player_x, player_y, angle, player
    if pohyb_hore:
        player_y -= rychlost
    if pohyb_dole:
        player_y += rychlost
    if pohyb_dolava:
        player_x -= rychlost
        player = pygame.transform.flip(flipping_player, True, False) 
    if pohyb_doprava:
        player_x += rychlost
        player = flipping_player
    if tocenie_meca:
        angle += 10
        
    #Border ------------------------------------------
    if player_x < 0:
        player_x = 0 
    if player_y < 0:
        player_y = 0  
    if player_x > 1024 - player.get_width():
        player_x = 1024 - player.get_width()  
    if player_y > 720 - player.get_height():
        player_y = 720 - player.get_height()


#Main loop 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            spracuj_keydown(event)
     
        if event.type == pygame.KEYUP:
            spracuj_keyup(event)

    pohyb_hraca()
    screen.fill((255, 255, 255))
    screen.blit(player, (player_x, player_y))


    rotated_sword = pygame.transform.rotate(lightsaber, angle)
    screen.blit(rotated_sword, (player_x + 70, player_y + 25))
    pygame.display.update()
    clock.tick(60)
        
pygame.quit()

    
