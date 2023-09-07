/*
 * A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.



Example 1:

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.


Constraints:

2 <= stones.length <= 2000
0 <= stones[i] <= 231 - 1
stones[0] == 0
stones is sorted in a strictly increasing order.
*/

use std::collections::BinaryHeap;
use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn can_cross(stones: Vec<i32>) -> bool {
        if stones[1] != 1 { return false }

        let n = stones.len();
        let mut pq = BinaryHeap::from([(1usize, 1usize)]);
        let mut mp = HashMap::new();
        let mut s = HashSet::new();

        for i in 0 .. n  { mp.insert(stones[i] as usize, i); }

        while let Some((i, k)) = pq.pop() {
            if i == n - 1 { return true }

            if k > 1 && mp.contains_key(&(k + stones[i] as usize - 1)) {
                let j = *mp.get(&(k + stones[i] as usize - 1)).unwrap();
                if s.contains(&(j, k - 1)) == false {
                    pq.push((j, k - 1));
                    s.insert((j, k - 1));
                }
            }

            if mp.contains_key(&(k + stones[i] as usize)) {
                let j = *mp.get(&(k + stones[i] as usize)).unwrap();
                if s.contains(&(j, k)) == false {
                    pq.push((j, k));
                    s.insert((j, k));
                }
            }

            if mp.contains_key(&(k + stones[i] as usize + 1)) {
                let j = *mp.get(&(k + stones[i] as usize + 1)).unwrap();
                if s.contains(&(j, k + 1)) == false {
                    pq.push((j, k + 1));
                    s.insert((j, k + 1));
                }
            }
        }

        false
    }
}

