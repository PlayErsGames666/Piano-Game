import pygame

from pygame import mixer

#Inicialization
pygame.init()
mixer.init()

#Create window
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("PlayErsGmaes Piano Game")

#Downloading sounds from nearest directory
do = mixer.Sound('../notes/do.wav')
re = mixer.Sound('../notes/re.wav')
mi = mixer.Sound('../notes/mi.wav')
fa = mixer.Sound('../notes/fa.wav')
sol = mixer.Sound('../notes/sol.wav')
lja = mixer.Sound('../notes/lja.wav')
si = mixer.Sound('../notes/si.wav')

#Making keyboard letter functional
keymap = {
    pygame.K_q: do,
    pygame.K_w: re,
    pygame.K_e: mi,
    pygame.K_r: fa,
    pygame.K_t: sol,
    pygame.K_y: lja,
    pygame.K_u: si
}

#Variable for Main cycle
running = True

#Main cycle
while running:
    for event in pygame.event.get(): #Event handling
        if event.type == pygame.QUIT: #X closing the window and game
            running = False

        if event.type == pygame.KEYDOWN: #Keyboard handling
            if event.key in keymap: #Check vocabulary
                keymap[event.key].play()

#End cycle
pygame.quit()