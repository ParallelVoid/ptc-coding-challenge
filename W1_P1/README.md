Problem taken from https://coding-challenge.projecttechconferences.com/challenges/1 (Problem 1)

"Eliza is trying bubble tea for the first time ever! Excited by this news, her friend Alexander buys different flavours for her to try out. Eliza quickly realizes that some flavours of bubble tea taste better than others and gives each of the drinks a score (note that this score can be negative if Eliza really dislikes the flavour!). Eliza also realizes she can drink up to two flavours of bubble tea at a time, so she defines the happiness of two bubble teas as the two individual scores added together. Unfortunately, Eliza is not very good at math, so please write a program to help her do calculations!"

Part A:
"Given the scores of two bubble teas, what is Eliza’s happiness from drinking both at once?

Input:
The first line of input contains two space-separated integers a and b (|a|, |b| ≤ 10³), the individual scores of each bubble tea.

Sample Input:
4 6

Output:
Output the happiness of this pair of bubble teas on a single line.

Sample Output:
10"

Part B:
"Given the scores of n different pairs of bubble teas, what is Eliza’s happiness from drinking each pair?

Input:
The first line of input contains the integer n (0 ≤ n ≤ 10⁴). The next n lines of input each contain two space-separated integers, aᵢ and bᵢ (|aᵢ|, |bᵢ| ≤ 10⁴), the individual scores of each bubble tea.

Sample Input:
3
4 6
-5 3
0 -3

Output:
Output n lines with the happiness of the i-th pair of bubble teas on the i-th line (1 ≤ i ≤ n).

Sample Output:
10
-2
-3"

Part C:
"Given the scores of n different pairs of bubble teas, what is Eliza’s maximum happiness?

Input:
The first line of input contains the integer n (1 ≤ n ≤ 10⁴). The next n lines of input each contain two space-separated integers, aᵢ and bᵢ (|aᵢ|, |bᵢ| ≤ 10⁵), the individual scores of each bubble tea.

Sample Input:
3
4 6
-5 3
0 -3

Output:
Output Eliza’s maximum happiness from any of the n pairs of bubble tea.

Sample Output:
10"

Part D:
"Given the scores of n different pairs of bubble teas, what is Eliza’s second greatest happiness?

Input:
The first line of input contains the integer n (2 ≤ n ≤ 10⁵). The next n lines of input each contain two space-separated integers, aᵢ and bᵢ (|aᵢ|, |bᵢ| ≤ 10⁵), the individual scores of each bubble tea.

Sample Input:
3
4 6
-5 3
0 -3

Output:
Output Eliza’s second largest happiness from any of the n pairs of bubble tea.

Sample Output:
-2"