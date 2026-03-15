import pygame
import os
import sys

from pygame import mixer

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


#Inicialization
pygame.init()
mixer.init()

#Create window
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("PlayErsGames Piano Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 40)

#Downloading sounds from nearest directory
do = mixer.Sound(resource_path('notes/do.wav'))
re = mixer.Sound(resource_path('notes/re.wav'))
mi = mixer.Sound(resource_path('notes/mi.wav'))
fa = mixer.Sound(resource_path('notes/fa.wav'))
sol = mixer.Sound(resource_path('notes/sol.wav'))
lja = mixer.Sound(resource_path('notes/lja.wav'))
si = mixer.Sound(resource_path('notes/si.wav'))

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

#Making note letter
note_names = {
    pygame.K_q: "DO",
    pygame.K_w: "RE",
    pygame.K_e: "MI",
    pygame.K_r: "FA",
    pygame.K_t: "SOL",
    pygame.K_y: "LA",
    pygame.K_u: "SI"
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

        if event.type == pygame.KEYUP: #Check for pressing a key
            pressed_keys.discard(event.key)

    for key, rect in key_positions.items():
        if key in pressed_keys:
            color = (200, 200, 255)  # цвет при нажатии
        else:
            color = (255, 255, 255)  # обычный цвет

        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 2)

        # Getting name of the key
        key_name = pygame.key.name(key)

        # Print letter
        key_text = font.render(key_name.upper(), True, (0, 0, 0))

        # Print note name
        note_text = font.render(note_names[key], True, (50, 50, 50))

        # Set middle position
        text_rect = key_text.get_rect(center=(rect[0] + rect[2] // 2,
                                              rect[1] + rect[3] // 2))

        screen.blit(key_text, text_rect)

        note_rect = note_text.get_rect(center=(rect[0] + rect[2] // 2,
                                               rect[1] + rect[3] // 2 + 50))

        screen.blit(note_text, note_rect)

    text = font.render("PlayErsGames Piano Game", True, (164, 164, 179))
    screen.blit(text, (117, 50))

    pygame.display.flip()
    clock.tick(60)

#End cycle
pygame.quit()