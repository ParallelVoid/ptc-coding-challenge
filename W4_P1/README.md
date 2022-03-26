Problem taken from https://coding-challenge.projecttechconferences.com/challenges/4 (Problem 1)

"Eliza realized she will never be able to write as fast as Alexander, so to intimidate him, she bought a magic life-sized typing rug! The letters on the rug are arranged in a long single line, sorted in alphabetical order from A to Z. The rug is so big that it takes Eliza 1 second to move from one letter to an adjacent letter, and 1 second to type a single letter that she’s already on. But, on the plus side, Eliza only needs to type all the letters in the message she sends, and the rug will magically rearrange themselves in the proper order before sending her message! Eliza wants to know some things before she uses her rug, but Alexander is too intimidated by the rug to help. Can you answer her questions instead?"

Part A:
"Eliza wants to figure out how much of each character she’ll have to type. Can you output a frequency array that shows her the number of times she’ll have to type each character? The frequency array should be space-separated and have exactly 26 integers showing how many times the i-th letter of the alphabet appears in her message.

Input:
The first and only line of input contains a string of lowercase Latin letters no longer than 10⁵ characters.

Sample Input:
elizastypingrug

Output:
Output 26 space-separated integers on a single line, where the i-th integer represents the number of times the i-th letter of the alphabet needs to be typed.

Sample Output:
1 0 0 0 1 0 2 0 2 0 0 1 0 1 0 1 0 1 1 1 1 0 0 0 1 1"

Part B:
"It’s time for Eliza to use her keyboard! If she can start and finish on any key, output the minimum time it takes her to send a message to her friend Angelica. Remember that it doesn’t matter what order Eliza types the letters in her message!

Input:
The first and only line of input contains a string of lowercase Latin letters no longer than 10⁵ characters.

Sample Input:
hiangelica

Output:
Output a single integer, representing the minimum amount of time it takes Eliza to type her message.

Sample Output:
23"

Part C:
"Eliza enjoys her keyboard so much that she decides to buy a circular version! In this keyboard, all adjacent letters in the alphabet are still adjacent, but the A key is also adjacent to the Z key. If she can start and finish on any two keys, can you tell Eliza the minimum time it will take her to write the message? Remember that it doesn’t matter what order Eliza types the letters in her message!

Input:
The first and only line of input contains a string of lowercase Latin letters no longer than 10⁵ characters.

Sample Input:
czya

Output:
Output a single integer, representing the minimum amount of time it takes Eliza to type her message.

Sample Output:
8"
