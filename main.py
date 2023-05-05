import pygame
from checkers.constants import WIDTH, HEIGHT, FPS, SQUARE_SIZE
from checkers.game import Game

# Game screen and caption
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("English Draughts")

# Get values of the square which was clicked on
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# --- MAIN LOOP ---
def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(SCREEN)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.reset()
        
        game.update()

    # Game over
    if game.winner():
        game.win_screen(game.winner())
    pygame.quit()

main()