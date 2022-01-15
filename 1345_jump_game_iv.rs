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

use std::collections::{HashMap, LinkedList};

impl Solution {
    pub fn min_jumps(arr: Vec<i32>) -> i32 {
        let mut visited = vec![false; arr.len()];
        let mut map = HashMap::new();
        for (index, &num) in arr.iter().enumerate() {
            map.entry(num).or_insert(Vec::new()).push(index);
        }
        let mut queue: LinkedList<(usize, usize)> = LinkedList::new();
        
        queue.push_back((0, 0));
        while let Some((idx, time)) = queue.pop_front() {
            if visited[idx] {
                continue;
            }
            visited[idx] = true;
            
            
            if idx + 1 == arr.len() {
                return time as i32;
            }
            
            queue.push_back((idx + 1, time + 1));
            
            if idx > 0 {
                queue.push_back((idx - 1, time + 1));
            }
            
            let ref key = arr[idx];
            if map.contains_key(key) {
                for &index in map[key].iter() {
                    queue.push_back((index, time + 1));
                }
                map.remove(key);
            }
        }
        
        panic!("Not possible");
    }
}

