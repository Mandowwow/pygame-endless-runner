import os
import pygame
from sys import exit 

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Nora')
clock = pygame.time.Clock()

base_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_dir, "Assets", "Sprites", "Sky1.jpg")
image_goblin_path = os.path.join(base_dir, "Assets", "Sprites", "goblin.png")
image_hero_path = os.path.join(base_dir, "Assets", "Sprites", "hero.png")
font_path = os.path.join(base_dir, "Assets", "Fonts", "Pixeltype.ttf")

test_font = pygame.font.Font(font_path, 65)

sky_surface = pygame.image.load(image_path).convert_alpha()

ground_surface = pygame.Surface((1280, 200))
ground_surface.fill('#5a391b')

score_surf = test_font.render('My game', False, 'Black')
score_rect = score_surf.get_rect(center = (640, 50))

goblin_surface = pygame.image.load(image_goblin_path).convert()
goblin_surface = pygame.transform.flip(goblin_surface, True, False)
goblin_surface = pygame.transform.scale(goblin_surface, (128, 128))
goblin_rect = goblin_surface.get_rect(midbottom = (1152, 620))

hero_surface = pygame.image.load(image_hero_path).convert()
hero_surface = pygame.transform.scale(hero_surface, (128,128))
hero_rect = hero_surface.get_rect(midbottom = (64, 620))
hero_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if hero_rect.collidepoint(event.pos) and hero_rect.bottom >= 620: 
                hero_gravity = -20


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and hero_rect.bottom >= 620:
                hero_gravity = -20

        if event.type == pygame.KEYUP:
            print('key up')

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,620))
    pygame.draw.rect(screen, 'Pink', score_rect)
    pygame.draw.rect(screen, 'Pink', score_rect, 6)
    #pygame.draw.line(screen, 'Gold', (0,0), pygame.mouse.get_pos(), 10)
    screen.blit(score_surf, score_rect)

    #PLAYER
    hero_gravity += 1
    hero_rect.y += hero_gravity
    #hero_rect.x += 3
    if hero_rect.bottom >= 620:
        hero_rect.bottom = 620
    screen.blit(hero_surface, hero_rect)

    screen.blit(goblin_surface, goblin_rect)
    goblin_rect.right -= 4
    if goblin_rect.left < -128: goblin_rect.left = 1280

    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
    #    print('jump')

    #if hero_rect.colliderect(goblin_rect):
        #print('collision')
    
    #mouse_pos = pygame.mouse.get_pos()
    #if hero_rect.collidepoint(mouse_pos):
    #    print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)