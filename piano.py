import pygame

from pygame import mixer

#Inicialization
pygame.init()
mixer.init()

#Create window
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("PlayErsGmaes Piano Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 40)

#Downloading sounds from nearest directory
do = mixer.Sound('../notes/do.wav')
re = mixer.Sound('../notes/re.wav')
mi = mixer.Sound('../notes/mi.wav')
fa = mixer.Sound('../notes/fa.wav')
sol = mixer.Sound('../notes/sol.wav')
lja = mixer.Sound('../notes/lja.wav')
si = mixer.Sound('../notes/si.wav')

#Coordinate of keyboard
key_positions = {
    pygame.K_q: (20, 200, 80, 150),
    pygame.K_w: (100, 200, 80, 150),
    pygame.K_e: (180, 200, 80, 150),
    pygame.K_r: (260, 200, 80, 150),
    pygame.K_t: (340, 200, 80, 150),
    pygame.K_y: (420, 200, 80, 150),
    pygame.K_u: (500, 200, 80, 150)
}

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

pressed_keys = set()
#Variable for Main cycle
running = True

#Main cycle
while running:
    screen.fill((4, 4, 89))

    for event in pygame.event.get(): #Event handling
        if event.type == pygame.QUIT: #X closing the window and game
            running = False

        if event.type == pygame.KEYDOWN: #Keyboard handling
            if event.key in keymap: #Check vocabulary
                keymap[event.key].play()
                pressed_keys.add(event.key)

            if event.type == pygame.KEYUP:
                pressed_keys.discard(event.key)

    for key, rect in key_positions.items():
        if key in pressed_keys:
            color = (200, 200, 255)  # цвет при нажатии
        else:
            color = (255, 255, 255)  # обычный цвет

        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 2)

    text = font.render("PlayErsGames Piano Game", True, (164, 164, 179))
    screen.blit(text, (117, 50))

    pygame.display.flip()
    clock.tick(60)

#End cycle
pygame.quit()