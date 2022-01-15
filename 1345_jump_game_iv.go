/*
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
 

Constraints:

1 <= arr.length <= 5 * 104
-108 <= arr[i] <= 108
*/

func minJumps(arr []int) int {
    graph := make(map[int][]int)
    for i := range arr {
        if graph[arr[i]] == nil {
            graph[arr[i]] = make([]int, 0)
        }
        graph[arr[i]] = append(graph[arr[i]], i)
    }
    numVisited := make(map[int]bool)
    
    queue := make([]int, 1)
    queue[0] = 0
    step := 0
    visited := make([]bool, len(arr))
    visited[0] = true
    
    for len(queue) > 0 {
        size := len(queue)
        for i := 0; i < size; i++ {
            cur := queue[i]
            if cur == len(arr) - 1 {
                return step
            }
            if !numVisited[arr[cur]] {
                numVisited[arr[cur]] = true
                for _, j := range graph[arr[cur]] {
                    if j == cur {
                        continue
                    }
                    queue = append(queue, j)
                    visited[j] = true
                }
            }
            if cur - 1 >= 0 && !visited[cur-1] {
                queue = append(queue, cur-1)
                visited[cur-1] = true
            }
            if cur + 1 < len(arr) && !visited[cur+1] {
                queue = append(queue, cur+1)
                visited[cur+1] = true
            }
        }
        queue = queue[size:]
        step++
    }
    
    return -1
}

