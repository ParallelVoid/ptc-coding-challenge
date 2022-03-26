Problem taken from https://coding-challenge.projecttechconferences.com/challenges/1 (Problem 2)

"Hailey the Hedgehog is sending messages to her friend Theo the Turtle. To avoid the evil (and not very smart) Callie the Crocodile from reading their messages, Hailey sends all her messages in a secret code. Unfortunately, Theo isn’t the brightest either (he only got a C- in his C++ programming classes), and he’s having trouble decoding Hailey’s messages. Can you help him decode his friend’s messages?"

Part A:
"Hailey’s first message is simple: she sends an integer n and a character c. The decoded message is the character c repeated n times.

Input:
The first and only line of input contains an integer n (0 ≤ n ≤ 100) and a lowercase character c, separated by a space.

Sample Input:
7 d

Output:
Output the decoded message on a single line.

Sample Output:
ddddddd"

Part B:
"Hailey gets lazy and decides to get rid of the space in between the number and character. The decoded message is the character c repeated n times.

Input:
The first and only line of input contains an integer n (0 ≤ n ≤ 10⁴) followed by a lowercase character c.

Sample Input:
7d

Output:
Output the decoded message on a single line.

Sample Output:
ddddddd"

Part C:
"Hailey gets even lazier and wants to send more detail in each message. She codes messages with integer-character pairs on a single line. To decode the message, print each character (cᵢ) nᵢ times, where n is the number appearing before the character.

Input:
The first and only line of input contains some number of non-space-separated alternating sequences of integers and characters, where every integer nᵢ satisfies the condition 1 ≤ nᵢ ≤ 10⁵. It is guaranteed that neither the length of the input nor the sum of all nᵢ exceeds 10⁶.

Sample Input:
1p1r1e2t1y1l2o1p1s

Output:
Output the decoded message in a single line.

Sample Output:
prettyloops"
