import pygame
from .constants import LBLUE, ROWS, DBLUE, SQUARE_SIZE, COLS, RED, BLACK
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.red_remaining = self.black_remaining = 12
        self.red_kings = self.black_kings = 0
        self.create_board()


    # To make the gameboard
    def draw_squares(self, SCREEN):
        SCREEN.fill(LBLUE)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(SCREEN, DBLUE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


    # To switch piece's location aka move
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        
        # To make the piece King if it is on the 'edge'
        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == BLACK:
                self.black_kings += 1
            else:
                self.red_kings += 1


    def get_piece(self, row, col):
        return self.board[row][col]


    # Display (create) pieces onto the board and assign values into the list (empty = 0)
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, BLACK))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)


    # Draw squares of the gameboard and pieces onto it
    def draw(self, SCREEN):
        self.draw_squares(SCREEN)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(SCREEN)


    # Remove a piece that was 'eaten'
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_remaining -= 1
                else:
                    self.black_remaining -= 1


    # Check if someone has won
    def winner(self):
        if self.red_remaining <= 0:
            return "Black"
        elif self.black_remaining <= 0:
            return "Red"
        
        return None



    # Start of the algorithm 
    # Determine valid moves based on a piece
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row-1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row-1, max(row-3, -1), -1, piece.color, right))

        if piece.color == BLACK or piece.king:
            moves.update(self._traverse_left(row+1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row+1, min(row+3, ROWS), 1, piece.color, right))

        return moves

    # Start, stop, step for the for loop where step shows direction (up or down diagonal)
    # Skipped will show if any pieces are skipped and if so then you can only skip but not just move
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves


    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r+step, row, step, color, right-1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves
    
    # End of the algorithm