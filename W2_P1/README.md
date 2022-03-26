Problem taken from https://coding-challenge.projecttechconferences.com/challenges/2 (Problem 1)

"For his birthday, Alexander received an n by m rectangular maze! He immediately walks in the entrance, finds himself stuck at the top left corner, and realizes he can only escape by reaching the bottom right corner. However, there’s a catch; to move from one cell to the next, Alexander has to write down the total distinct number of ways to get from the first cell to that cell. Also, the maze has some special properties: Alexander can only make a move by moving one cell right or down, whereas he can’t move to the cells directly above or to the left of his current cell. Alexander works quickly, writing down numbers and moving from cell to cell, and ends up just one square away from exiting the maze, but he can’t figure out how many ways there are to get to the last cell! Can you help him write his way out?"

Part A:
"Given the dimensions of the maze, help Alexander find the number of distinct valid escape routes if he can only move right and down. Note that the only difference between these subproblems are the constraints (and the modulus in parts B and C). In part A, there are no more than 20 cells in total.

Input:
The first and only line of input contains two space-separated integers n and m (1 ≤ n · m ≤ 20), representing the length and width of the maze respectively.

Sample Input:
4 5

Output:
Output the number of distinct ways to move from the top left to the bottom right of the maze. Note that two paths are considered distinct if a) they have a different number of moves OR b) they have the same number of moves but following the two paths will lead you to different squares at any point in time.

Sample Output:
35"
