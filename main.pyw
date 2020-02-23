import time
from random import *
import webbrowser
import os
try :
    import pygame
    from pygame.locals import *
except :
    print("Pour pouvoir utiliser ce programme, merci d'installer Pygame sur votre machine.\npip install pygame")
    time.sleep(5)
    exit()

# Variables
all_game = []
f = open("game.txt", "r", encoding="utf-8")
all_game_brut = f.read().split("\n")
for i in range(1, len(all_game_brut)):
    if not all_game_brut[i] == "":
        if not all_game_brut[i].startswith("#") :
            all_game.append(all_game_brut[i])
width, height = 400, 400
back = pygame.image.load('back.png')
front = pygame.image.load('front.png')

# Initialisation Pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption('Make A Choice')
screen = pygame.display.set_mode((width,height))

def affiche(color, menu):
    screen.fill((0,0,0))
    screen.blit(back, (0,0))
    if menu != "non" :
        game = str(choice(all_game))
        #print(game)
        text_draw(game, ((width//2)-len(game)*6 ,(height//2)-37), color, 25)
    screen.blit(front, (0,0))
    pygame.display.update()

def text_draw(text, position, color, size):
    '''affiche le texte demandé dans la couleur et la position choisie.'''
    myfont = pygame.font.SysFont('arial', size)
    try :
        textsurface = myfont.render(text, True, color)
        screen.blit(textsurface,position)
    except:
        print("error")

def choose():
    '''affichage rapide de tous les jeux de la liste fournie.'''
    pygame.mixer.music.load("sound_roulette.mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(1)
    time.sleep(0.1)
    for i in range(1,50):
        affiche((255,255,255), "oui")
        time.sleep(0.05*(i//10))
    affiche((0,255,0), "oui")

# Boucle de jeu
click = False
loop = True
affiche((0,0,0), "non")
while loop :
    mx, my = pygame.mouse.get_pos()

    button_github = pygame.Rect(width//2-75, height-60, 300, 125)
    button_github_draw = pygame.Surface((150,20))
    button_github_draw.set_alpha(0)
    screen.blit(button_github_draw, button_github)

    button_add = pygame.Rect(width-40, height-40, 300, 125)
    button_add_draw = pygame.Surface((40,40))
    button_add_draw.set_alpha(0)
    screen.blit(button_add_draw, button_add)

    pygame.display.update()

    if button_add.collidepoint((mx, my)) :
        if click :
            webbrowser.open('https://github.com/ArthurTakase?tab=repositories')

    elif button_github.collidepoint((mx, my)) :
        if click :
            os.system("game.txt")

            all_game = []
            f = open("game.txt", "r", encoding="utf-8")
            all_game_brut = f.read().split("\n")
            for i in range(1, len(all_game_brut)):
                if not all_game_brut[i] == "":
                    if not all_game_brut[i].startswith("#") :
                        all_game.append(all_game_brut[i])

    click = False
    for event in pygame.event.get():
        if event.type == QUIT :
            loop = False
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
        if event.type == KEYDOWN :
            if event.key == K_SPACE :
                choose()

pygame.quit()
quit()
