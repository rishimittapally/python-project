import pygame
import random

pygame.init()

#screen
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the blocks")

clock = pygame.time.Clock()
font = pygame.font.SysFont('ariel', 35)

# player
player_x = 250
player_y = 520
player_size = 40
player_speed = 10

# block
block_x = random.randint(0, 460 - 40)
block_y = -40
block_size = 40
block_speed = 6

score = 0
running = True
game_over = False 

while running:
    clock.tick(60)
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          pygame.quit()
    if not game_over:
        # movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += player_speed
        # block falling
        block_y += block_speed
        if block_y > HEIGHT:
            block_y = -40
            block_x = random.randint(0, WIDTH - block_size)     
            score += 1
            block_speed += 0.2

        #rectangles   
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size )
        block_rect = pygame.Rect(block_x, block_y, block_size, block_size )
        
        #collision
        if player_rect.colliderect(block_rect):
            running = True
            game_over = True
        
        

        #draw 
        pygame.draw.rect(screen,(0,200,255), player_rect )
        pygame.draw.rect(screen,(255, 80, 80), block_rect)
    
        # score
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
    
    if game_over:
       lose_text = font.render("Sorry, you lost!", True, (255, 0, 0))
       gameover_text = font.render("Click on the crossbar to close the tab!", True, (255, 0, 0))
       screen.blit(lose_text, (100, HEIGHT // 2))
       screen.blit(gameover_text, (0, 250))
       screen.blit(score_text, (250, 10))

       

    pygame.display.update()

pygame.quit() 

    