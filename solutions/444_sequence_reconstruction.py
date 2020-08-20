'''
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

 

Example 1:

Input: org = [1,2,3], seqs = [[1,2],[1,3]]
Output: false
Explanation: [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:

Input: org = [1,2,3], seqs = [[1,2]]
Output: false
Explanation: The reconstructed sequence can only be [1,2].
Example 3:

Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
Output: true
Explanation: The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Example 4:

Input: org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
Output: true
 

Constraints:

1 <= n <= 10^4
org is a permutation of {1,2,...,n}.
1 <= segs[i].length <= 10^5
seqs[i][j] fits in a 32-bit signed integer.
'''

class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        values = {x for seq in seqs for x in seq}
        graph = {x: [] for x in values}
        indegrees = {x: 0 for x in values}
        
        for seq in seqs:
            for i in range(len(seq) - 1):
                s = seq[i]
                t = seq[i+1]
                graph[s].append(t)
                indegrees[t] += 1
        queue = collections.deque()
        for node, count in indegrees.items():
            if count == 0:
                queue.append(node)
        
        res = []
        while queue:
            if len(queue) != 1:
                return False
            source = queue.popleft()
            res.append(source)
            for target in graph[source]:
                indegrees[target] -= 1
                if indegrees[target] == 0:
                    queue.append(target)
        return len(res) == len(values) and res == org
        
