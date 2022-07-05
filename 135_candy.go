/*
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
*/

func candy(ratings []int) int {
    length := len(ratings)
	res := make([]int, length)
	for i := 0; i < length; i++ {
		res[i] = 1
	}
	for i := 1; i < length; i++ {
		if ratings[i] > ratings[i-1] {
		    res[i] = res[i-1] + 1
	    }
	}
	for i := length - 1; i > 0; i-- {
		if ratings[i-1] > ratings[i] {
		    res[i-1] = max(res[i]+1, res[i-1])
	    }
	}
	count := 0
	for _, item := range res {
		count += item
	}
	return count
}

func max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}

