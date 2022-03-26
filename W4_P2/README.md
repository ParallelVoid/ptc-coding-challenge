Problem taken from https://coding-challenge.projecttechconferences.com/challenges/4 (Problem 2)

"Theo the Turtle has a deck of special cards. Each card in his deck has a number from 0 to 9 on one side and an uppercase or lowercase alphabet letter on the other. Theo considers a sequence of cards “squishy” if all of the following conditions apply for all cards that have two neighbours (i.e. there are no conditions for the first and last cards in the sequence). The first condition is that if the sum of the immediate neighbours is strictly greater than 5, the other side of the card must be lowercase. The second condition is that if the side is lowercase, there must be one uppercase and one lowercase letter among the faces of its immediate neighbours. Theo the Turtle lets Hailey the Hedgehog borrow his deck! Help Hailey practice identifying and constructing these squishy sequences of cards! (Each sequence that Hailey sets will be at least three cards long.)"

Part A:
"Hailey is trying to put together squishy sequences, but isn’t sure whether they are correct. She records the cards that are face up and gives them to you! Can you help her identify whether the sequence could be squishy, if the other side of each card could have any number or character?

Input:
The first line of input contains a single integer n (3 ≤ n ≤ 10⁵), representing the number of cards in Hailey’s sequence. The second line of input contains n space-separated alphanumeric characters, representing the side that is face up of each card in the line.

Sample Input:
4
a 6 b 7

Output:
Print “Yes” if the sequence could be a squishy sequence, or “No” if it cannot.

Sample Output:
Yes"

Part B:
"Hailey has been writing down a bunch of her sequences and alternating the side of the card facing up, but while having fun, she forgot to record the other sides of the cards! Callie the Crocodile is skeptical of Hailey’s squishy sequences, though. For each of the sequences Hailey gives you, help her determine whether it could be squishy or not. If the sequence could be squishy, help Hailey prove it to Callie by outputting possible values for the reverse side of each card.

Input:
The first line of input contains a single integer n (3 ≤ n ≤ 10⁵), representing the number of cards in Hailey’s sequence. The second line of input contains n space-separated alphanumeric characters, representing the side that is face up of each card in the line. Note that the characters will alternate between alphabet characters and digits!

Sample Input:
6
A 6 b 7 c 9

Output:
Output “Yes” followed by n space-separated characters that represent possible values for the reverse of each card, or “No” if the sequence cannot be squishy. Remember that cards must have a number on one side and a letter on the other side!

Sample Output:
Yes
3 n 3 X 1 b"
