import pygame
import numpy as np
import math

pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

start_pos_x = int(pygame.Surface.get_width(window) /2)
start_pos_y = int(pygame.Surface.get_height(window) /2)

shaft_width = 25
shaft_height = 100

ball_size = 20

speed = 3000

tip_height = shaft_height / 2


def draw_player():
        

            
        #region of variables for player
    
        left_shaft_start = start_pos_x - (shaft_width/2)
        shaft_top = start_pos_y

        ball1_center_x = start_pos_x - ball_size
        ball1_center_y = start_pos_y + shaft_height
        ball2_center_x = start_pos_x + ball_size
        ball2_center_y = start_pos_y + shaft_height

        tip_left = start_pos_x - shaft_width / 1.5
        tip_top = start_pos_y - shaft_height / 4.5
        tip_width =  shaft_width + 10

        # endregion

        shaft = (pygame.draw.rect
                            (window, 
                             "tan", 
                             pygame.Rect(left_shaft_start, shaft_top, shaft_width, shaft_height),
                               ),
            
                pygame.draw.rect
                            (window, 
                             "black", 
                             pygame.Rect(left_shaft_start, shaft_top, shaft_width, shaft_height),
                               1))

        ball1 = (pygame.draw.circle
                        (window, 
                        "tan", 
                        (ball1_center_x,
                            ball1_center_y), 
                        ball_size),  
                    
                pygame.draw.circle
                        (window, 
                            "black", 
                        (ball1_center_x, 
                            ball1_center_y), 
                        ball_size, 
                        1))
        
        ball2 = (pygame.draw.circle
                        (window, 
                        "tan", 
                        (ball2_center_x, 
                        ball2_center_y), 
                        ball_size),  
                    
                pygame.draw.circle
                        (window, 
                            "black", 
                        (ball2_center_x, 
                        ball2_center_y), 
                        ball_size, 
                        1))
                
        tip =   (pygame.draw.arc
                    (window, 
                    "pink", 
                    pygame.Rect(tip_left, tip_top, tip_width, tip_height), 
                    start_angle = 0, 
                    stop_angle = 3.14, 
                    width = 100), 
                
                pygame.draw.arc
                        (window, 
                        "black", 
                        pygame.Rect(tip_left, tip_top, tip_width, tip_height), 
                        start_angle = 0, 
                        stop_angle = 3.14,))

def move_player(start_pos_x, start_pos_y):


    if press_keys[pygame.K_w]:
        start_pos_y -= speed* dt

    if press_keys[pygame.K_a]:
        start_pos_x -= speed * dt

    if press_keys[pygame.K_s]:
        start_pos_y += speed * dt

    if press_keys[pygame.K_d]:
        start_pos_x += speed * dt
    
    draw_player()
    return start_pos_x, start_pos_y

def rotate_player(start_pos_x, start_pos_y):
    rotate_player_right = pygame.key.get_pressed()[pygame.K_e]
    if rotate_player_right:

        angle = math.degrees(90*dt)

        player_x = move_player(start_pos_x, start_pos_y)[0]
        player_y = move_player(start_pos_x, start_pos_y)[1]

        start_pos_x = start_pos_x + (player_x - start_pos_x) * math.cos(90*dt)
        - (player_y - start_pos_y) * math.sin(angle)

        start_pos_y = start_pos_y + (player_y - start_pos_y) * math.sin(angle) 
        - (player_x - start_pos_x) * math.cos(angle)
        return start_pos_x, start_pos_y
        draw_player()

while running is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    press_keys = pygame.key.get_pressed()

    window.fill("white")

    dt = clock.tick(60) / 1000

    
    start_pos_x, start_pos_y = move_player(start_pos_x, start_pos_y)
    rotate_player(start_pos_x, start_pos_y)
    pygame.display.flip()

    
  
pygame.quit()

