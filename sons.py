import pygame

pygame.mixer.init(48000, -16, 1, 1024)

pygame.init()

sonclic = pygame.mixer.Sound('sons/clic.ogg')

sonmenu = pygame.mixer.Sound('sons/menu.mp3')

sonnotification = pygame.mixer.Sound('sons/notification.mp3')