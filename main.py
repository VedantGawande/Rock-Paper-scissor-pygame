#  ---Rock Paper Scissor---
import pygame, sys, os, random
from time import sleep

pygame.init()
# Skin = (215,205,155)
# Pink = (225,105,135)
# ---Main settings---
BG = (255,255,255)
BLACK = (0,0,0)

WIDTH = 1537
HEIGHT = 807
FPS = 60

FONT = pygame.font.SysFont('comicsans', 40)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rock Paper Scissor')

# ---Variables---
options = ['r', 'p', 's']
player_score = 0
pc_score = 0
draws = 0
angle = 0
angle_2 = 0
cba = True # - these 2 variables are used in a function
abc = True


# ---Assets---
ROCK = pygame.transform.scale((pygame.image.load(os.path.join('assets', 'rock.png')).convert_alpha()), (400,400))
PAPER = pygame.transform.scale((pygame.image.load(os.path.join('assets', 'paper.png')).convert_alpha()), (400,400))
SCISSOR = pygame.transform.scale((pygame.image.load(os.path.join('assets', 'scissor.png')).convert_alpha()), (400,400))
# BLACK_IMG = pygame.transform.scale((pygame.image.load(os.path.join('assets', 'black.png')).convert_alpha()), (1536,781))


# ---Functions---
def drawrock(rock, player=True, pc=False):
    '''
    It takes the surface 'rock', player(bool), and pc(bool)
    It will draw image if it's pc or player according to the bool arguments
    '''
    if player and pc:
        WIN.blit(rock, (WIDTH - rock.get_width(),HEIGHT/2 - rock.get_height()/2))
        
        rock_flip = pygame.transform.flip(rock,True,False)
        WIN.blit(rock_flip, (0,HEIGHT/2 - rock.get_height()/2))
    elif player:
        rock = pygame.transform.flip(rock,True,False)
        WIN.blit(rock, (0,HEIGHT/2 - rock.get_height()/2))
    elif pc:
        WIN.blit(rock, (WIDTH - rock.get_width(),HEIGHT/2 - rock.get_height()/2))
    pygame.display.update()

def drawp_s(paper, player=True, pc=False):
    '''
    It takes the surface 'paper OR scissor', player(bool), and pc(bool)
    It will draw image if it's pc or player according to the bool arguments
    '''
    if player and pc:
        WIN.blit(paper, (0,HEIGHT/2 - paper.get_height()/2))
        
        paper_flip = pygame.transform.flip(paper,True,False)
        WIN.blit(paper_flip, (WIDTH - paper.get_width(),HEIGHT/2 - paper.get_height()/2))
    elif player:
        
        WIN.blit(paper, (0,HEIGHT/2 - paper.get_height()/2))
    elif pc:
        paper = pygame.transform.flip(paper,True,False)
        WIN.blit(paper, (WIDTH - paper.get_width(),HEIGHT/2 - paper.get_height()/2))
    pygame.display.update()

def shake(surface):
    global angle, angle_2, abc, cba, BLACK
    i = 0
    THREE = 210*2
    while i != 70*2:
        if abc == True:
            angle += 1
        else:
            angle -= 1

        if angle >= 40:
            abc = False
        if angle <= -30:
            abc = True

        rock_flip = pygame.transform.flip(surface,True,False)
        
        rotated = pygame.transform.rotozoom(rock_flip, angle,1)
        rotated_pc = pygame.transform.rotozoom(surface, angle,1)

        rect = rotated.get_rect(center = (200,HEIGHT//2))
        
        sur_rect = rotated.get_rect(center = (WIDTH - surface.get_width() + 200, HEIGHT/2 - surface.get_height()/2 + 200))

        i +=1
        # rect.centerx -= 1
        WIN.blit(rotated, rect)
        WIN.blit(rotated_pc, sur_rect)
        pygame.display.update()
    
    WIN.fill(BLACK)
    pygame.display.update()
        
        


# ---Main loop---
run = True
clock = pygame.time.Clock()
while run:
    WIN.fill(BLACK)

    player_render = FONT.render(f'Your Score: {player_score}',1,BG)
    WIN.blit(player_render, (0,0))

    pc_render = FONT.render(f'Computer Score: {pc_score}',1,BG)
    WIN.blit(pc_render, (WIDTH - pc_render.get_width(), 0))

    draw_render = FONT.render(f'Draws: {draws}',1,BG)
    WIN.blit(draw_render, (WIDTH/2 - draw_render.get_width(), 0))

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                shake(ROCK)
                drawrock(ROCK, True, False)
                if random.choice(options) == 'r':
                    drawrock(ROCK, False, True)
                    draws += 1
                    print('draw')

                elif random.choice(options) == 'p':
                    drawp_s(PAPER, False, True)
                    pc_score += 1
                    print('lost')

                elif random.choice(options) == 's':
                    drawp_s(SCISSOR, False, True)
                    player_score += 1
                    print('won')

                else:
                    drawrock(ROCK, False, True)
                    draws += 1
                    print('draw (else)')
                    
            if event.key == pygame.K_p:
                shake(ROCK)
                drawp_s(PAPER, True, False)
                if random.choice(options) == 'r':
                    drawrock(ROCK, False, True)
                    player_score += 1
                    print('won')
                elif random.choice(options) == 'p':
                    drawp_s(PAPER, False, True)
                    draws += 1
                    print('draw')
                elif random.choice(options) == 's':
                    drawp_s(SCISSOR, False, True)
                    pc_score += 1
                    print('lost')
                else:
                    drawp_s(PAPER, False, True)
                    draws += 1
                    print('draw (else)')

            if event.key == pygame.K_s:
                shake(ROCK)
                drawp_s(SCISSOR,True, False)
                if random.choice(options) == 'r':
                    drawrock(ROCK, False, True)
                    pc_score += 1
                    print('lost')
                elif random.choice(options) == 'p':
                    drawp_s(PAPER, False, True)
                    player_score += 1
                    print('won')
                elif random.choice(options) == 's':
                    drawp_s(SCISSOR, False, True)
                    draws += 1
                    print('draw')
                else:
                    drawp_s(SCISSOR, False, True)
                    draws += 1
                    print('draw (else)')

            if event.key == pygame.K_n:
                draws = 0
                player_score = 0
                pc_score = 0
