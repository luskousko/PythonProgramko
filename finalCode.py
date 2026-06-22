
"""PYGAME CODE"""
#🟡random pre dummies
import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1024, 720))
clock = pygame.time.Clock()
running = True

#Player
player = pygame.image.load('/Users/luskousko/Desktop/Work/Work_Programko/pics_pygame/cat.png').convert_alpha()
player = pygame.transform.scale(player,(100,100))
flipping_player = player

#Weapons
lightsaber = pygame.image.load('/Users/luskousko/Desktop/Work/Work_Programko/pics_pygame/lightsaber.png').convert_alpha()
lightsaber = pygame.transform.scale(lightsaber,(80,80))
lightsaber = pygame.transform.rotate(lightsaber,225)

gun = pygame.image.load('/Users/luskousko/Desktop/Work/Work_Programko/pics_pygame/gun.png').convert_alpha()
gun = pygame.transform.scale(gun, (80, 80))

#ZOZNAM
weapons = [{
        "name": "lightsaber",
        "image": lightsaber,
        "base_rotation": 0,
        "rotates": True,
        "offset": (10, 10)},
    
        {"name": "gun",
        "image": gun,
        "base_rotation": 0,
        "rotates": False,
         "offset": (60, 40)}]
current_weapon_index = 0

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

#🟣 Svihanie meca -----------------------------------------------
smer_svihu = 1      #1 = dopredu, -1 = naspäť
max_uhol = 50       #o koľko stupňov max švihne
rychlost_svihu = 8  #ako rýchlo švihá

#🟡 Dummies ----------------------------------------------------
#Dummies
dummies = []
dummy_velkost = 150
dummy_rychlost = 20

dummy_image = pygame.image.load('/Users/luskousko/Desktop/Work/Work_Programko/pics_pygame/dog.png').convert_alpha()
dummy_image = pygame.transform.scale(dummy_image, (dummy_velkost, dummy_velkost))
dummy_image_left = pygame.transform.flip(dummy_image, True, False) #otacanie
#🟡 Dummies ----------------------------------------------------

#FUNCTIONS
def switch_weapon():
    global current_weapon_index, angle
    current_weapon_index = (current_weapon_index + 1) % len(weapons)
    angle = 0  #reset to angle 0 when switching

def set_weapon(index):
    global current_weapon_index, angle
    if 0 <= index < len(weapons):
        current_weapon_index = index
        angle = 0
    
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

    
    if event.key == pygame.K_e:
        switch_weapon() 
    if event.key == pygame.K_1:
        set_weapon(0)
    if event.key == pygame.K_2:
        set_weapon(1)
    #🟡dumici 
    if event.key == pygame.K_o:
        spawn_dummy()

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


"""
def spracuj_key(event, stav):
    global pohyb_hore, pohyb_dole, pohyb_doprava, pohyb_dolava, tocenie_meca

    if event.key == pygame.K_w:
        pohyb_hore = stav
    if event.key == pygame.K_s:
        pohyb_dole = stav
    if event.key == pygame.K_a:
        pohyb_dolava = stav
    if event.key == pygame.K_d:
        pohyb_doprava = stav
    if event.key == pygame.K_SPACE:
        tocenie_meca = stav
"""


def pohyb_hraca():
    #🟣 add smer svihu
    global player_x, player_y, angle, player, smer_svihu
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
        
    #🔴Will rotate only if weapon supports that
    """
    aktualna_zbran = weapons[current_weapon_index]
    if tocenie_meca and aktualna_zbran["rotates"]:
        angle += 10
    """
    
    #🟣Substitue the previous lines with that
    aktualna_zbran = weapons[current_weapon_index]
    if tocenie_meca and aktualna_zbran["rotates"]:
        angle += rychlost_svihu * smer_svihu
        if angle >= max_uhol:
            smer_svihu = -1
        if angle <= -max_uhol:
            smer_svihu = 1
    else:
        angle = 0
        smer_svihu = 1
        
    #if tocenie_meca:
    #angle += 10
        

   
    #Border
    if player_x < 0:
        player_x = 0 
    if player_y < 0:
        player_y = 0  
    if player_x > 1024 - player.get_width():
        player_x = 1024 - player.get_width()  
    if player_y > 720 - player.get_height():
        player_y = 720 - player.get_height()





#🟡dumici --------------------------------------
def spawn_dummy():
    novy = {
        "x": random.randint(0, 1024 - dummy_velkost),
        "y": random.randint(0, 720 - dummy_velkost),
        "vx": random.choice([-dummy_rychlost, dummy_rychlost]),
        "vy": random.choice([-dummy_rychlost, dummy_rychlost])
    }
    dummies.append(novy)

#🟡dumici pohyb --------------------------------------
def pohyb_dummies():
    for d in dummies:
        d["x"] += d["vx"]
        d["y"] += d["vy"]
        #odraz od stien
        if d["x"] < 0 or d["x"] > 1024 - dummy_velkost:
            d["vx"] = -d["vx"]
        if d["y"] < 0 or d["y"] > 720 - dummy_velkost:
            d["vy"] = -d["vy"]

#⚪️zasah dumikov --------------------------------------
def kontrola_zasahu():
    if not tocenie_meca:
        return
    player_rect = pygame.Rect(player_x, player_y, player.get_width(), player.get_height())
    for d in dummies[:]:   #[:] = kopia, aby sme mohli mazat pocas iteracie
        dummy_rect = pygame.Rect(d["x"], d["y"], dummy_velkost, dummy_velkost)
        if player_rect.colliderect(dummy_rect):
            dummies.remove(d)


#Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            spracuj_keydown(event)
            #spracuj_key(event, True)
            
        if event.type == pygame.KEYUP:
            spracuj_keyup(event)
            #spracuj_key(event, False)
        


    pohyb_hraca()
    #🟡 pohyb dumikov
    pohyb_dummies()
    #⚪️ zasah dumikov
    kontrola_zasahu()
    screen.fill((255, 255, 255))
    #🟡 dumiki
    #for d in dummies:
        #pygame.draw.rect(screen, (200, 50, 50), (d["x"], d["y"], dummy_velkost, dummy_velkost))
        #screen.blit(dummy_image, (d["x"], d["y"]))
    for d in dummies:
        if d["vx"] < 0:
            screen.blit(dummy_image_left, (d["x"], d["y"]))
        else:
            screen.blit(dummy_image, (d["x"], d["y"]))
    screen.blit(player, (player_x, player_y))
    
    #Sword - old
    #rotated_sword = pygame.transform.rotate(sword, angle)
    #screen.blit(rotated_sword, (player_x + 70, player_y + 25))
    #🔴 Current weapon ---------------------------------------------------------------_
    aktualna_zbran = weapons[current_weapon_index]
    weapon_image = aktualna_zbran["image"]
    rotated_weapon = pygame.transform.rotate(weapon_image,aktualna_zbran["base_rotation"] + angle)
    offset_x, offset_y = aktualna_zbran["offset"]
    screen.blit(rotated_weapon, (player_x + offset_x, player_y + offset_y))
    
    #screen.blit(rotated_weapon, (player_x + 70, player_y + 25))
    #🔴 Current weapon ----------------------------------------------------------------
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()

#najprv fialove
















"""Try later"""
##import pygame
##import random
##
##pygame.init()
##
##WIDTH = 1024
##HEIGHT = 720
##CELL = 64   # veľkosť políčka gridu
##
##screen = pygame.display.set_mode((WIDTH, HEIGHT))
##clock = pygame.time.Clock()
##running = True
##
##player_img = pygame.image.load('/Users/luskousko/Desktop/cat.png').convert_alpha()
##player_img = pygame.transform.scale(player_img,(100,100))
##player = player_img  #aktuálny obrázok
##
##player_x = 0
##player_y = 0
##
##rychlost = 8
##
##pohyb_hore = False
##pohyb_dole = False
##pohyb_doprava = False
##pohyb_dolava = False
##
### ---------------- PREKÁŽKY (grid bunky) ----------------
##prekazky = [
##    pygame.Rect(3*CELL, 2*CELL, CELL, CELL),
##    pygame.Rect(4*CELL, 2*CELL, CELL, CELL),
##    pygame.Rect(5*CELL, 2*CELL, CELL, CELL),
##    pygame.Rect(6*CELL, 4*CELL, CELL, CELL),
##]
##
### ---------------- DOMČEK ----------------
##domcek = pygame.Rect(10*CELL, 5*CELL, CELL*2, CELL*2)
##
##def aktualizuj_smer():
##    global player
##    if pohyb_dolava:
##        player = pygame.transform.flip(player_img, True, False)
##    elif pohyb_doprava:
##        player = player_img
##        
##
##def kolizia(rect):
##    for p in prekazky:
##        if rect.colliderect(p):
##            return True
##    return False
##
##def spracuj_keydown(event):
##    global pohyb_hore, pohyb_dole, pohyb_doprava, pohyb_dolava, player_x, player_y 
##    if event.key == pygame.K_w:
##        pohyb_hore = True
##    if event.key == pygame.K_s:
##        pohyb_dole = True
##    if event.key == pygame.K_a:
##        pohyb_dolava = True
##    if event.key == pygame.K_d:
##        pohyb_doprava = True
####    if event.key == pygame.K_SPACE:
####        player_x = random.randint(0,1000)
####        player_y = random.randint(0,1000)
##
##def spracuj_keyup(event):
##    global pohyb_hore, pohyb_dole, pohyb_doprava, pohyb_dolava
##    if event.key == pygame.K_w:
##        pohyb_hore = False
##    if event.key == pygame.K_s:
##        pohyb_dole = False
##    if event.key == pygame.K_a:
##        pohyb_dolava = False
##    if event.key == pygame.K_d:
##        pohyb_doprava = False
##   
##
##def pohyb_hraca():
##    global player_x, player_y
##
##    HITBOX_MARGIN = 17  #čím väčšie, tým bližšie k stene môže ísť
##
##    new_rect = pygame.Rect(
##        player_x + HITBOX_MARGIN,
##        player_y + HITBOX_MARGIN,
##        player.get_width() - 2*HITBOX_MARGIN,
##        player.get_height() - 2*HITBOX_MARGIN
##    )
##
##    if pohyb_hore:
##        new_rect.y -= rychlost
##    if pohyb_dole:
##        new_rect.y += rychlost
##    if pohyb_dolava:
##        new_rect.x -= rychlost
##    if pohyb_doprava:
##        new_rect.x += rychlost
##
##    # kolízia s prekážkami
##    if not kolizia(new_rect):
##        player_x = new_rect.x - HITBOX_MARGIN
##        player_y = new_rect.y - HITBOX_MARGIN
##
##    # ohraničenie okna
##    if player_x < 0:
##        player_x = 0
##    if player_y < 0:
##        player_y = 0
##    if player_x > WIDTH - player.get_width():
##        player_x = WIDTH - player.get_width()
##    if player_y > HEIGHT - player.get_height():
##        player_y = HEIGHT - player.get_height()
##
##while running:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            running = False
##        if event.type == pygame.KEYDOWN:
##            spracuj_keydown(event)
##        if event.type == pygame.KEYUP:
##            spracuj_keyup(event)
##
##    pohyb_hraca()
##    aktualizuj_smer()
##    screen.fill((255,255,255))
##
##    # -------- GRID --------
##    for x in range(0, WIDTH, CELL):
##        pygame.draw.line(screen, (220,220,220), (x,0), (x,HEIGHT))
##    for y in range(0, HEIGHT, CELL):
##        pygame.draw.line(screen, (220,220,220), (0,y), (WIDTH,y))
##
##    # -------- PREKÁŽKY --------
##    for p in prekazky:
##        pygame.draw.rect(screen, (120,120,120), p)
##
##    # -------- MAČKA --------
##    screen.blit(player,(player_x,player_y))
##
##    # -------- DOMČEK (prekryje mačku) --------
##    pygame.draw.rect(screen,(200,100,50), domcek)
##
##    pygame.display.update()
##    clock.tick(60)
##
##pygame.quit()
















