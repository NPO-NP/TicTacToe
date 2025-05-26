# Tic Tac Toe

22 May 2025

The game board is defined as a list of 3 lists, with each sub-list representing a row on the board.
For example, [ ['-', 'O', '-'], ['-', '-', 'O'], ['X', '-', '-'] ].
Each column of each row is either Player 1 (O), Player 2 (X) or empty (-).
Each element of the board can be accessed using index like board[0][1] (row 0, column 1).
A function is included to display the state of the board. 

You need to do the following:
- Decide on the input format for a player to move eg 0,1 (row 0, column 1) or 1 2 (row 1, column 2) etc
- Implement logic to control each player's turn
- Implement logic to determine winning combination or a draw (ie examine every row, every column and the diagonals)
- For AI vs human, implement logic to determine where the AI should move to
- When a game has ended, either quit the program or start another game

You can either clone or fork the repo.
