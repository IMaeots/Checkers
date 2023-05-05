# ENGLISH DRAUGHTS
#### Youtube link: https://youtu.be/u095mOaYhLM
# Description:
# Main idea
English Draughts is similar to the international checkers but has some rule differences.
Main rule differences compared to international checkers are that a piece can not take opponents pieces going backwards and that a king can move backwards also but only one step at a time. Overall the game is just like checkers where pieces move diagonally and the winner is the one who has eaten all the opponents pieces. Piece will become a king if it reaches the opponents end. Game is played on a 8x8 game board.

# My perspective
The goal was to do something interesting related to python and game developement as I will 
continue learning web developement afterawards anyways. The project is supposed to be Version 1.0.
It will allow local Draughts, that is two players playing the game on one computer. Future versions
developed outside CS50 will possibly feature an AI and/or multiplayer/online.

# Before starting
First step was to learn the basics of pygame as it was used to display and make the game.
Next up was to make necessary folders and code files. I also made __init__.py files to 
reference folders as python modules (librarys), this made it easier to use classes with functions as objects.

# Steps I stepped through when making the game of Draughts (Checkers) with python
1. Made the main file of the game called main.py. There is a while loop that runs when the window is open and
keeps the players updated. The window will close and quit the game if pressed exit or 'r'.
2. Made the game board in blue colours. For which I made board.py that I used to display and
draw necessary pixels at necessary places. Different functions have necessary vales also that track the game.
3. Made constants.py where I store all constant variables so they are easy to change and accessible.
4. Set up piece.py where everything about checkerpieces is. Made a class and defined everything using self as an object.
5. Draw the board and its pieces with the help of Board.py to main.py and piece.py (circle shaped pieces in draw function)
Found out that white piece does not fit with the board colours so changed it to red to be more visible.
6. Make crown appear on the piece when it gets the King status.
For this I downloaded a free png of a comic crown and fitted it in the center of a piece thanks to self object in piece.py.
The picture I opened again in constants.
In constants I opened the picture from assets/crown.png and sized it correct.
7. Started working on how to move the pieces around and delete them.
Made a function called move in board.py and also in piece.py..
Combined these will swap positions where the piece was and where the piece will be. This can be used later to make the piece move.
Then I made a for loop with which I checked if a piece had moved onto a row that would make it king, if it had happend then
it would turn into a king, otherwise not.
Used pygame feature in main.py to get the xy of where the mouse clicked and got the row and col of that location to select the piece behind it.
Check if the square is valid and other possible movements
8. For all this movement I created game.py that tracks movements, assigns valid possibilities and makes playing the game possible.
Game.py will have the update function that updates the game in main.py after every while loop.
Made a method reset (with the key 'r') that uses init to intialize a new game.
change_turn method to change turn after a move in game.py
9. Now starting to make things visible by drawing moves onto the screen and making the correct valid moves.
10. An alogrithm that applies to each checkers piece to give valid movements.
* Check each piece diagonals for available squares and movements.
* King has the same alogrithm but also backwards.
Alogrithm: 1. Check the color of the piece (one can move only down, other up). 2. Check diagonals. 2.1 Check if first square is empty then it is a valid move.
2.2 If the square is blocked then check the color of the piece in way. 2.2 If the color is the same = non-valid move. 2.3 If the color is opponent's
then check the next square also. 2.4 If its free then its valid, if its not free it is not valid move.
Algorithm Update: Check if we jumped a piece, then restart and check if we can jump another piece. If so then add these moves.
Symboled the start and end of the algorithm with descriptions in between. It works with a loop that is recursive in case of a skip.
Finished the game by making different changes in movement and fixing bugs
11. Made an endscreen with text of the winner and a button that restarts the game.
12. Added a moving sound that is common in checkers.

# Main idea of every file .py
main.py - main loop (not linked with user) (uses other library methods) displays the game and takes user input.
game.py - operating the game (running and checking game movements) (methods to use) uses input to send information as needed.
constants.py - Assign constant variables for easy change and use
board.py - Defining an object called Board that will be used in making the checkers board and making it interactive.
piece.py - Making an object called Piece that can be used to display, manipulate and be used to play the game. It will allow pieces to move and the program
to understand what can and has happend.
__init__.py - is used to reference folders as python libraries with modules to easily take information from one to another and use stuff as objects/methods.
README.txt - to create somewhat understanding of how this code was made and what was done to make it work. How some things work and what is the idea.
The assets folder is for extra things (assets) like the crown picture, win screen picture and sound effect for a move.

#### This was made by Indrek Mäeots for CS50 in 2022.
