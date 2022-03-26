Problem taken from https://coding-challenge.projecttechconferences.com/challenges/3 (Problem 3)

"Turbofrog is almost late for his tic-tac-toe tournament with Sittingduck! Luckily, he finds a special path of teleporter lily pads on the pond separating him from the tournament. If Turbofrog uses these teleporters optimally, he can cross the pond in time for his game! Since he doesn’t want to keep Sittingduck waiting for long, help Turbofrog find the minimum time it takes to cross the pond. The lily pads are arranged in a straight line and are numbered from 1 to n. Each second, Turbofrog can choose to jump forward one lily pad (if a lily pad exists for him to jump to) or he can choose to teleport to the destination of the teleporter lily pad he’s standing on. (Note that teleporters will only bring Turbofrog forward, never backward!) Turbofrog starts on the first lily pad and crosses the pond when he makes it to the nᵗʰ lily pad."

Part A:
"If each teleporter takes 1 second to transport Turbofrog to its destination and Turbofrog can take as many teleporters he wants, what is the minimum time it takes for him to cross the pond?

Input:
The first line of input contains a single integer n (2 ≤ n ≤ 10⁵), the number of lily pads on the pond. The following n lines of input each contain an integer lᵢ, representing the location that the iᵗʰ lily pad will teleport to. For all lily pads, either lᵢ ≥ i OR lᵢ = 0 (indicating that there is no teleporter on the lily pad).

Sample Input:
4
3
3
0
4

Output:
Output the minimum time it takes for Turbofrog to cross the pond. In the sample i/o, Turbofrog teleports from lily pad 1 to 3 in one second, then jumps from lily pad 3 to 4 in one second for a total of two seconds.

Sample Output:
2"
