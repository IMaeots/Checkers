import pygame
from .constants import RED, BLACK, BLUE, SQUARE_SIZE, FPS, WIN_BACKGROUND, FONT, WIDTH, HEIGHT, SOUND
from .board import Board

class Game:
    def __init__(self, SCREEN):
        self._init()
        self.SCREEN = SCREEN


    def update(self):
        self.board.draw(self.SCREEN)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()


    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}


    # Game over screen
    def win_screen(self, winner):
        self.SCREEN.blit(WIN_BACKGROUND, (0, 0))
        text = FONT.render("The winner is {0}!".format(winner), False, BLACK)
        text_rect = text.get_rect(center = (WIDTH // 2, HEIGHT // 2))
        self.SCREEN.blit(text, text_rect)
        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    done = True

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()


    # Select a piece and use functions that move and give valid moves
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
    
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
            
        return False


    # Move a piece and remove a piece if skipped over
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col) 
            skipped = self.valid_moves[(row, col)]   
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        
        pygame.mixer.Sound.play(SOUND) # Play moving a piece sound
        return True


    # Display possible moving options on board
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.SCREEN, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)


    # Change turn in the game
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = BLACK
        else:
            self.turn = RED