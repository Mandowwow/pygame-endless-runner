import os
import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (640, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def enemy_movement(enemy_list):
    if enemy_list:
        for enemy_rect in enemy_list:
            enemy_rect.x -= 5

            screen.blit(goblin_surface, enemy_rect)

        enemy_list = [enemy for enemy in enemy_list if enemy.x > -128]

        return enemy_list
    else: return []

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Nora')
clock = pygame.time.Clock()

base_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_dir, "Assets", "Sprites", "Sky1.jpg")
image_goblin_path = os.path.join(base_dir, "Assets", "Sprites", "goblin.png")
image_hero_path = os.path.join(base_dir, "Assets", "Sprites", "hero.png")
image_eye_path = os.path.join(base_dir, "Assets", "Sprites", "eye.png")
font_path = os.path.join(base_dir, "Assets", "Fonts", "Pixeltype.ttf")
test_font = pygame.font.Font(font_path, 65)

game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load(image_path).convert_alpha()

ground_surface = pygame.Surface((1280, 200))
ground_surface.fill('#5a391b')

#score_surf = test_font.render('My game', False, 'Black')
#score_rect = score_surf.get_rect(center = (640, 50))


#enemies / obstacles
goblin_surface = pygame.image.load(image_goblin_path).convert_alpha()
goblin_surface = pygame.transform.flip(goblin_surface, True, False)
goblin_surface = pygame.transform.scale2x(goblin_surface)
#goblin_rect = goblin_surface.get_rect(midbottom = (1152, 620))

eye_surf = pygame.image.load(image_eye_path).convert_alpha()
eye_surf = pygame.transform.flip(eye_surf, True, False)
eye_surf = pygame.transform.scale2x(eye_surf)

enemy_rect_list = []

hero_surface = pygame.image.load(image_hero_path).convert_alpha()
hero_surface = pygame.transform.scale2x(hero_surface)
hero_rect = hero_surface.get_rect(midbottom = (64, 620))
hero_gravity = 0

#intro scene
hero_stand = pygame.image.load(image_hero_path).convert_alpha()
hero_stand = pygame.transform.scale2x(hero_stand)
hero_stand_rect = hero_stand.get_rect(center = (640, 360))

game_name_surf = test_font.render('Nora Runner',False,(111,196,169))
game_name_rect = game_name_surf.get_rect(center = (640, 260))

game_message_surf = test_font.render('Press space to run', False,(111,196,169))
game_message_rect = game_message_surf.get_rect(center = (640, 460))

#timer
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1750)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hero_rect.collidepoint(event.pos) and hero_rect.bottom >= 620: 
                    hero_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and hero_rect.bottom >= 620:
                    hero_gravity = -30
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

        if event.type == enemy_timer and game_active:
            if randint(0,2):
                enemy_rect_list.append(goblin_surface.get_rect(midbottom = (randint(1280, 1400), 620)))
            else:
                enemy_rect_list.append(eye_surf.get_rect(midbottom = (randint(1280, 1400), 500)))


    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,620))
        # pygame.draw.rect(screen, 'Pink', score_rect)
        # pygame.draw.rect(screen, 'Pink', score_rect, 6)
        # screen.blit(score_surf, score_rect)
        score = display_score()

        #PLAYER
        hero_gravity += 1
        hero_rect.y += hero_gravity
        #hero_rect.x += 3
        if hero_rect.bottom >= 620:
            hero_rect.bottom = 620
        screen.blit(hero_surface, hero_rect)

        # obstacle / enemy movement
        enemy_rect_list = enemy_movement(enemy_rect_list)

        # screen.blit(goblin_surface, goblin_rect)
        # goblin_rect.right -= 4
        # if goblin_rect.left < -128: goblin_rect.left = 1280

        #COLLISION

    else:
        screen.fill((94,129,162))
        screen.blit(hero_stand, hero_stand_rect)

        score_message_surf = test_font.render(f'Your score: {score}', False, (111,196,169))
        score_message_rect = score_message_surf.get_rect(center = (640, 460))
        screen.blit(game_name_surf, game_name_rect)

        if score == 0:
            screen.blit(game_message_surf, game_message_rect)
        else:
            screen.blit(score_message_surf, score_message_rect)

    pygame.display.update()
    clock.tick(60)