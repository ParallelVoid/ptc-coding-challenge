Problem taken from https://coding-challenge.projecttechconferences.com/challenges/2 (Problem 3)

"Turbofrog is playing tic-tac-toe with his friend Sittingduck. Unfortunately for him, even though Sittingduck is really slow to move, she’s very, very good at tic-tac-toe. On the other hand, Turbofrog is new to tic-tac-toe; even though Sittingduck is nice and always lets Turbofrog play first and play with the X pieces, he plays way too quickly and has already lost 14 games in a row to Sittingduck. Desperate for a way to turn his losing streak around, Turbofrog turns to you and your programming skills to help him win. Can you beat Sittingduck and her methodical calculations?"

Part A:
"Given a board and a command (‘Block’ or ‘Win’), show Turbofrog the board after he plays. There will always be at least one possible move for Turbofrog. If there is more than one possible move, any of the possible moves will be accepted. Then, tell Turbofrog the coordinates of his move in the format [row] [column]. Turbofrog always plays as X and Sittingduck always plays as O. Note that the board may not always represent a possible position in the standard game of tic tac toe.

Input:
The first three lines of input each contain three characters, ‘x’, ‘o’, or ‘.’, which represents the board’s current state. More specifically, ‘x’ represents an X piece, ‘o’ represents an O piece, and ‘.’ represents a blank square. The fourth and final line of input contains a command, either ‘Block’ or ‘Win’, which represents the kind of move that Turbofrog wants to take.

Sample Input:
.xo
.xo
...
Block

Output:
Output each row of the board after Turbofrog’s move on three separate lines. On the final line, output the coordinates of his move in the format [row] [column], where the top left corner has coordinates 1 1. It is guaranteed that only one valid move will exist.

Sample Output:
.xo
.xo
..x
3 3"

Part B:
"Now, Turbofrog is focusing on not losing within one move. Given the current state of the board, find a move for Turbofrog that either wins the game for him, or, if this is not possible, prevents Sittingduck from winning on the next move. If there are multiple possible moves, output any of them. It is guaranteed that there are at least 6 starting pieces on the board and that there is at least one move that satisfies the constraints. Turbofrog always plays as X and Sittingduck always plays as O. Note that the board may not always represent a possible position in the standard game of tic tac toe.

Input:
The first three lines of input each contain three characters, ‘x’, ‘o’, or ‘.’, which represents the board’s current state. More specifically, ‘x’ represents an X piece, ‘o’ represents an O piece, and ‘.’ represents a blank square.

Sample Input:
oxo
oxo
...

Output:
Output the space-separated coordinates of Turbofrog’s best move, in the form [row] [column]. If multiple moves lead to the same result, output any of them.

Sample Output:
2 3"

Part C:
"Turbofrog wants to develop a strategy where he thinks ahead by two moves. Given a board with Turbofrog to move, let Turbofrog know whether he will win or lose, given that both he and Sittingduck play optimally. It is guaranteed that there are at least 5 starting pieces on the board and that there is a forced win or loss within two moves from each player. Turbofrog always plays as X and Sittingduck always plays as O. Note that the board may not always represent a possible position in the standard game of tic tac toe.

Input:
The first three lines of input each contain three characters, ‘x’, ‘o’, or ‘.’, which represents the board’s current state. More specifically, ‘x’ represents an X piece, ‘o’ represents an O piece, and ‘.’ represents a blank square.

Sample Input:
oox
o..
x..

Output:
Output ‘Win’ if Turbofrog will win and ‘Lose’ if he will lose. It is guaranteed that there is a forced win or loss within two moves from each player.

Sample Output:
Win"