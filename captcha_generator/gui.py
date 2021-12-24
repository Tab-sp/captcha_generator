import pygame
import main

input_path = 'input_image/sample.png' #where you put in directory to image

check, label = main.do_it(input_path)
pygame.init()
pygame.display.set_caption('Captcha Generator')

WIDTH = 700
HEIGHT = 800
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FONT = pygame.font.Font('freesansbold.ttf', 20)
clock = pygame.time.Clock()

clicked_status = [False, False, False, False, False, False, False, False, False]

def display_images():
    count = 0
    for y in range(3):
        for x in range(3):
            image = pygame.image.load(f'input_image/chopped_up/{count}.png')
            image = pygame.transform.scale(image, (180, 180))
            count += 1
            SCREEN.blit(image, (50+x*200, 100+y*200))
            pygame.draw.rect(SCREEN, RED, pygame.Rect(50+x*200, 100+y*200, 180, 180), 2)

def print_text(word, x, y, color = BLACK):
    TEXT = FONT.render(word, True, color)
    text_rect = TEXT.get_rect()
    text_rect.center = (x, y)
    return SCREEN.blit(TEXT, text_rect)

def update_button(mouse):
    if 50 <= mouse[0] <= 230 and 100 <= mouse[1] <= 280:
        if not clicked_status[0]:
            pygame.draw.rect(SCREEN, GREEN, pygame.Rect(50, 100, 180, 180), 2)
            clicked_status[0] = True
        else:
            pygame.draw.rect(SCREEN, RED, pygame.Rect(50, 100, 180, 180), 2)
            clicked_status[0] = False
    if 250 <= mouse[0] <= 430 and 100 <= mouse[1] <= 280:
        if not clicked_status[1]:
            pygame.draw.rect(SCREEN, GREEN, pygame.Rect(250, 100, 180, 180), 2)
            clicked_status[1] = True
        else:
            pygame.draw.rect(SCREEN, RED, pygame.Rect(250, 100, 180, 180), 2)
            clicked_status[1] = False
    if 450 <= mouse[0] <= 630 and 100 <= mouse[1] <= 280:
        if not clicked_status[2]:
            pygame.draw.rect(SCREEN, GREEN, pygame.Rect(450, 100, 180, 180), 2)
            clicked_status[2] = True
        else:
            pygame.draw.rect(SCREEN, RED, pygame.Rect(450, 100, 180, 180), 2)
            clicked_status[2] = False
    if 50 <= mouse[0] <= 230 and 300 <= mouse[1] <= 480:
        if not clicked_status[3]:
            pygame.draw.rect(SCREEN, GREEN, pygame.Rect(50, 300, 180, 180), 2)
            clicked_status[3] = True
        else:
            pygame.draw.rect(SCREEN, RED, pygame.Rect(50, 300, 180, 180), 2)
            clicked_status[3] = False
    if 250 <= mouse[0] <= 430 and 300 <= mouse[1] <= 480:
        if not clicked_status[4]:
            pygame.draw.rect(SCREEN, GREEN, pygame.Rect(250, 300, 180, 180), 2)
            clicked_status[4] = True
        else:
            pygame.draw.rect(SCREEN, RED, pygame.Rect(250, 300, 180, 180), 2)
            clicked_status[4] = False
    if 450 <= mouse[0] <= 630 and 300 <= mouse[1] <= 480:
        if not clicked_status[5]:
            pygame.draw.rect(SCREEN, GREEN, pygame.Rect(450, 300, 180, 180), 2)
            clicked_status[5] = True
        else:
            pygame.draw.rect(SCREEN, RED, pygame.Rect(450, 300, 180, 180), 2)
            clicked_status[5] = False
    if 50 <= mouse[0] <= 230 and 500 <= mouse[1] <= 680:
        if not clicked_status[6]:
            pygame.draw.rect(SCREEN, GREEN, pygame.Rect(50, 500, 180, 180), 2)
            clicked_status[6] = True
        else:
            pygame.draw.rect(SCREEN, RED, pygame.Rect(50, 500, 180, 180), 2)
            clicked_status[6] = False
    if 250 <= mouse[0] <= 430 and 500 <= mouse[1] <= 680:
        if not clicked_status[7]:
            pygame.draw.rect(SCREEN, GREEN, pygame.Rect(250, 500, 180, 180), 2)
            clicked_status[7] = True
        else:
            pygame.draw.rect(SCREEN, RED, pygame.Rect(250, 500, 180, 180), 2)
            clicked_status[7] = False
    if 450 <= mouse[0] <= 630 and 500 <= mouse[1] <= 680:
        if not clicked_status[8]:
            pygame.draw.rect(SCREEN, GREEN, pygame.Rect(450, 500, 180, 180), 2)
            clicked_status[8] = True
        else:
            pygame.draw.rect(SCREEN, RED, pygame.Rect(450, 500, 180, 180), 2)
            clicked_status[8] = False
    if 250 <= mouse[0] <= 430 and 680 <= mouse[1] <= 800:
        if clicked_status == check:
            pygame.draw.rect(SCREEN, WHITE, pygame.Rect(220, 680, 170, 100))
            pygame.draw.rect(SCREEN, GREEN, pygame.Rect(250, 700, 120, 40))
            print_text('correct!', 320, 750)
        else:
            pygame.draw.rect(SCREEN, WHITE, pygame.Rect(220, 680, 170, 100))
            pygame.draw.rect(SCREEN, RED, pygame.Rect(250, 700, 120, 40))
            print_text('wrong!', 320, 750)

SCREEN.fill(WHITE)
print_text(f'look for {label}', 320, 20)
pygame.draw.rect(SCREEN, GREEN, pygame.Rect(250, 700, 120, 40))
print_text('click to check', 320, 750)
display_images()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            update_button(mouse)

    clock.tick(30)
    pygame.display.update()
