Problem taken from https://coding-challenge.projecttechconferences.com/challenges/1 (Problem 3)

"Turbofrog is a walking, talking, programming frog! Turbofrog has just discovered the joys of gardening, and he’s making his own fences for his three beautiful gardens. Unfortunately, Turbofrog is not very good at math and needs your help to figure out how to put his garden fence together."

Part A:
"Turbofrog finds a pile of wooden planks in his garage and decides to make the fence for his first garden by arranging the planks from shortest to longest. Unfortunately, Turbofrog isn’t sure where each fence piece will end up. Can you help him determine the order of the planks in his fence?

Input:
The first line of input contains a single integer n, the number of planks (1 ≤ n ≤ 10³). The second line of input contains n space-separated positive integers L (-10⁵ ≤ L ≤ 10⁵), the length of each plank. Note that some planks might have the same length!

Sample Input:
4
5 2 6 8

Output:
Output n space-separated integers on a single line: the height of each piece of Turbofrog’s fence in order from shortest to longest, starting from the shortest piece.

Sample Output:
2 5 6 8"

Part B:
"For his second garden, Turbofrog wants to use one long wooden plank. He will cut the plank into four pieces and use those pieces to make a rectangle around the garden. Turbofrog wonders what the maximum possible area of his garden can be. Can you help him find the maximum possible area?

Input:
The first and only line of input contains a single integer n, the length of the wooden plank (0 ≤ n ≤ 10⁹).

Sample Input:
25

Output:
Print the maximum possible area of a rectangle bordered by the plank, rounded to exactly one decimal place.

Sample Output:
39.1"

Part C:
"For his third garden, Turbofrog found a pile of shiny rope and a pile of nylon rope. He can create a super rope by combining a piece of shiny rope and a nylon rope, where the length of the super rope will be the two ropes’ lengths added together. Turbofrog wants to fence off individual rectangular areas with each of these super ropes and maximize the total area he creates. Can you help him find the maximum combined area he can fence off?

Input:
The first line of input contains a single integer n, the number of shiny ropes AND the number of nylon ropes (1 ≤ n ≤ 10⁵). The second line of input contains n space-separated integers s₁, s₂, …, sₙ, the lengths of the shiny ropes. The third line of input contains n space-separated integers r₁, r₂, …, rₙ, the lengths of the nylon ropes (0 ≤ sᵢ, rᵢ ≤ 10⁵).

Sample Input:
4
5 2 6 8
7 2 4 3

Output:
Print the maximum combined area that Turbofrog can fence off with super rope, rounded to exactly one decimal place. Note that you should round after summing all the areas. Your answer will be accepted as correct if the absolute value of the difference between your answer and the correct answer is less than or equal to 0.1.

Sample Output:
25.3"
