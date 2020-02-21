#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) This code snippet will be O(n), because it will take n loops for a + n \* n to be equal to n \* n \* n, You can verify this by placing number on n such as 4, 3, or 2.

b) This algorithm will be O(nlogn) since there is an outer loop that scales directly with n, which gives us the O(n), but the inner loop is advancing twice as fast each loop towards n giving us the O(logn) part.

c) Since the recursive function is only being called once per bunny, it scales directly with bunnies making it O(n).

## Exercise II

Would use a method similar binary search, I would have my high floor set to the highest floor and low floor set to the lowest, and I would drop an egg at half of between the high and low floor.

If it breaks it means I would have to move down, and if it doesn't break I would move up. If moving down I would update my high floor and then drop an egg from the middle of my new high floor and low floor. Similarly if it didn't break but I would update my low floor.

I will repeat this until finding the floor it breaks and then 1 below will be the floor it doesn't break. The runtime complexity of this algorith would be O(logn)
