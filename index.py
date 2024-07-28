import pygame
import sys
from game import Game

pygame.init()
dark_blue = (44, 44, 127)
red = (255, 0, 0)
white = (255, 255, 255)
light_gray = (200, 200, 200)
black = (0, 0, 0)

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 300)

def show_message(message, color, size, y_offset=0, shadow=True):
    font = pygame.font.SysFont("Arial", size, bold=True)  
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 4 + y_offset))
    
    if shadow:
        shadow_text = font.render(message, True, black)
        shadow_rect = shadow_text.get_rect(center=(screen.get_width() // 2 + 2, screen.get_height() // 4 + y_offset + 2))
        screen.blit(shadow_text, shadow_rect)
    
    pygame.draw.rect(screen, light_gray, text_rect.inflate(20, 20))
    screen.blit(text, text_rect)

def show_multiline_message(messages, color, size, line_height, y_offset=0):
    font = pygame.font.SysFont("Arial", size, bold=True)  
    start_y = screen.get_height() // 2 + y_offset
    for i, message in enumerate(messages):
        text = font.render(message, True, color)
        text_rect = text.get_rect(center=(screen.get_width() // 2, start_y + i * line_height))
        pygame.draw.rect(screen, light_gray, text_rect.inflate(20, 20))
        screen.blit(text, text_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.game_over = False
                game.reset()
            else:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                if event.key == pygame.K_RIGHT:
                    game.move_rigth()
                if event.key == pygame.K_DOWN:
                    game.move_down()
                if event.key == pygame.K_UP:
                    game.rotate()

        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()

    # Drawing
    screen.fill(dark_blue)
    game.draw(screen)

    if game.game_over:
        show_message("GAME OVER", red, 40, 30)  
        show_multiline_message(["CLIQUE EM QUALQUER TECLA", "PARA CONTINUAR"], white, 16, 30, 50)

    pygame.display.update()
    clock.tick(60)
