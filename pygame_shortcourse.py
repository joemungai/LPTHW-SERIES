import pygame
from sys import exit
from random import randint
#initializing pygame
pygame.init()

#display surface
screen = pygame.display.set_mode((800,400))

# score screen
clock = pygame.time.Clock()
test_font = pygame.font.Font("Game_mediafiles/images/GENIS 400.otf",50)
score_surface = test_font.render('*SHARKNADO*',False,(64,64,64))

#obstacle_movement
def obstacle_movement(obstacle_list):
    if obstacle_list:
        ## logical error obstacle_rect_list instead of obstacle_list
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 350:screen.blit(obstacle_surface,obstacle_rect)
            else:screen.blit(bat_surf,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list  if obstacle.x > -100]
        return obstacle_list
    else:return []

#create the  score display surface
def dislay_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Score :{current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):return False
    return True

def player_animation():
    global player_surface,player_index
    if player_rect.bottom < 370:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):player_index = 0
        player_surface = player_walk[int(player_index)]


    #play walking animation when player is on the floor




#back ground image
cave_surface = pygame.image.load("Game_mediafiles/images/back_cave.png").convert_alpha()
#ground image
ground_surface = pygame.image.load("Game_mediafiles/images/Piso.png").convert_alpha()

#player
player_walk_1 = pygame.image.load("Game_mediafiles/images/ch004.png").convert_alpha()
player_walk_2 = pygame.image.load("Game_mediafiles/images/player_walk_2.png").convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_jump = pygame.image.load("Game_mediafiles/images/player_jump.png").convert_alpha()
player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(center = (100,370))

player_gravity = 0
start_time = 0
score = 0

#intro screeen
player_stand = pygame.image.load("Game_mediafiles/images/player_stand.png")
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

intro_name = test_font.render("The Bug Game",False,"purple")
intro_surface = intro_name.get_rect(center = (400,80))
intro_message = test_font.render("Press space bar to run",False,"purple")
intro_message_rect = intro_message.get_rect(center = (400,340))

#obstacle
obstacle_surface = pygame.image.load('''Game_mediafiles/images/obstacle_4.png''').convert_alpha()
#obstacle_rect = obstacle_surface.get_rect(midbottom = (800,350))

#timer
bat_surf = pygame.image.load("Game_mediafiles/images/bat_1.png").convert_alpha()
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

obstacle_rect_list = []


game_active = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active == True:
            #player_rect.left =
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 370 :
                    player_gravity = -20

            if event.type == pygame.KEYDOWN and player_rect.bottom >= 370 :
                if event.key == pygame.K_SPACE:
                       player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                #player_rect.left = 800
                start_time = int(pygame.time.get_ticks() /1000)
                if obstacle_rect.left < player_rect.right :
                    #obstacle_rect.left = 800
                    game_active = True

        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(obstacle_surface.get_rect(bottomright = (randint(900,1110),350)))
            else :
                obstacle_rect_list.append(bat_surf.get_rect(bottomright = (randint(900,1110),211)))



#draw all  our elements
#update everything
#background image

    if game_active:
            screen.blit(cave_surface,(0,0))
        #ground iamge
            screen.blit(ground_surface,(0,320))

        #text image
            score = dislay_score()

        #Player
            player_gravity += 1
            player_rect.y += player_gravity
            if player_rect.bottom >=370 :player_rect.bottom = 370
            player_animation()
            screen.blit(player_surface,player_rect)

        #obstacle movement
            obstacle_rect_list =  obstacle_movement(obstacle_rect_list)

        #Collision
            game_active = collisions(player_rect,obstacle_rect_list)
    else:
        screen.fill((64,64,64))
        screen.blit(player_stand,player_stand_rect)
        screen.blit(intro_name,intro_surface)
        player_rect.midbottom = (100,370)
        player_gravity =  0



        score_message = test_font.render(f"your score: {score}",False,"purple")
        score_message_rect = score_message.get_rect(center = (400,340))

        if score == 0:
            screen.blit(intro_message,intro_message_rect)
        else:
            screen.blit(score_message,score_message_rect)

    pygame.display.update()
    clock.tick(60)
