Problem taken from https://coding-challenge.projecttechconferences.com/challenges/2 (Problem 2)

"Hailey the Hedgehog went hiking with her friend, Theo the Turtle. Unfortunately, Hailey runs too fast for Theo and they get separated! Luckily for them, Hailey packed a compass and a map before leaving home this morning. With her mapping skills, she finds out where she is and where she left poor Theo. Hailey quickly realizes that Theo probably hasn’t moved since she lost him, so she races off to find him, only to realize she doesn’t know how far she has to go before finding him. Help Hailey find her way back to her friend!"

Part A:
"Hailey knows her position and Theo’s position in Cartesian coordinates. Help her find the distance that she’ll have to travel to get to him!

Input:
The first line of input contains two space-separated integers x and y, Hailey’s Cartesian coordinates. The second line of input contains two space-separated integers X and Y, Theo’s Cartesian coordinates. For this subproblem, -10³ ≤ x, y, X, Y ≤ 10³.

Sample Input:
0 0
1 1

Output:
Output the distance Hailey will have to travel, rounded to exactly one decimal place.

Sample Output:
1.4"

Part B:
"The evil Callie the Crocodile is here too! Hailey can only save Theo if she reaches Theo before Callie. Otherwise, Theo will be in trouble! Luckily for Hailey, Callie left her GPS on and Hailey knows exactly where she is. If Theo stays where he is and Hailey and Callie move at the same speed, help Hailey find out who will make it to Theo first!

Input:
Each of the three lines of input contains two space-separated integers. The first line of input contains Hailey’s Cartesian coordinates, x₁ and y₁. The second line of input contains Callie’s Cartesian coordinates, x₂ and y₂. The third and final line of input contains Theo’s coordinates, x₃ and y₃. For this subproblem, -10⁶ ≤ x₁, y₁, x₂, y₂, x₃, y₃ ≤ 10⁶.

Sample Input:
10 10
5 5
1 1

Output:
Output “Callie” if Callie reaches Theo first and “Hailey” if Hailey can reach Theo before Callie. If they reach Theo at the same time, output “Hailey” because she’s smarter than Callie and will still manage to save her friend.

Sample Output:
Callie"

Part C:
"Hailey lost her friend again, and Callie is still on the loose! Now, Hailey and Callie can both move at different speeds to get to any spot in the forest. Who will make it to Theo first? As in subproblem B, Hailey will save Theo if she reaches him before Callie, and Theo is in trouble otherwise.

Input:
The first line of input contains Hailey’s Cartesian coordinates, x₁ and y₁, followed by her speed v₁. The second line of input contains Callie’s Cartesian coordinates, x₂ and y₂, followed by her speed v₂. The third and final line of input contains Theo’s coordinates, x₃ and y₃. For this subproblem, -10⁶ ≤ x₁, y₁, x₂, y₂, x₃, y₃ ≤ 10⁶, and 1 ≤ v₁, v₂ ≤ 10⁴.

Sample Input:
-1 -1 1
4 4 7
1 1

Output:
Output “Callie” if Callie reaches Theo first and “Hailey” if Hailey can reach Theo before Callie. If they reach Theo at the same time, output “Hailey” because she’s smarter than Callie and will still manage to save her friend.

Sample Output:
Hailey"
