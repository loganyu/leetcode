/*
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1
 

Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
*/

type IntHeap []int

func (h IntHeap) Len() int {return len(h)}
func (h IntHeap) Less(i, j int) bool {return h[i] > h[j]}
func (h IntHeap) Swap(i, j int) {h[i], h[j] = h[j], h[i]}
func (h *IntHeap) Push(x interface{}) {*h = append(*h, x.(int))}
func (h *IntHeap) Pop() interface{} {
    n := len(*h)
    x := (*h)[n-1]
    *h = (*h)[0:n-1]
    return x
}

func lastStoneWeight(stones []int) int {
    pq := IntHeap(stones)
    heap.Init(&pq)
    for pq.Len() > 1 {
        x, y := heap.Pop(&pq).(int), heap.Pop(&pq).(int)
        if x != y {
            heap.Push(&pq, x-y)
        }
    }
    
    if pq.Len() == 0 {
        return 0
    }
    
    return heap.Pop(&pq).(int)
}

