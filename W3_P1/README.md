Problem taken from https://coding-challenge.projecttechconferences.com/challenges/3 (Problem 1)

"Eliza drank too many bubble teas during week 1, and she still has too much sugar in her system! She has to finish her math homework, though! Can you help her!? Note that to score points for this problem, you should use dynamic programming to solve the problem instead of math.factorial()!!"

Part A:
"Eliza’s sugar high makes her wayy too hyper while solving her homework! She gets so excited that she accidentally writes exclamation marks after every number! Eliza learned about factorials in school, and now she wants to practice finding them! Eliza wonders what 5 factorial is equal to! Can you help!?

Output:
Output the numerical value of 5!."

Part B:
"Eliza is even more interested in factorials now and she wants to make a study sheet of the first n factorials. Output 1 to n factorial to help her! Since the numbers can get really big, output each number mod 10⁹ + 7.

Input:
The first and only line of input contains a single integer n. 1 ≤ n ≤ 10⁵.

Sample Input:
4

Output:
Output 1! mod 10⁹ + 7, 2! mod 10⁹ + 7, …, n! mod 10⁹ + 7 on separate lines.

Sample Output:
1
2
6
24"

Part C:
"Eliza decides that it takes too long to look up numbers in her study sheet. Instead, she wants to get the factorial of a number as soon as she needs it. Eliza will ask you to calculate n factorials. Given these n numbers, can you help Eliza? Note that your program should be fast for full marks! Since the numbers can get really big, output each number mod 10⁹ + 7.

Input:
The first line of input contains an integer n, indicating the number of queries (0 ≤ n ≤ 10⁶). The next n lines contain a single integer qᵢ on line i (1 ≤ i ≤ n, 1 ≤ qᵢ ≤ 10⁶).

Sample Input:
3
2
1
3

Output:
Output n lines, where line i contains qᵢ! mod 10⁹ + 7.

Sample Output:
2
1
6"