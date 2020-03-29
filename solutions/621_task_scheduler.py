'''
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Note:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
'''

from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(Counter(tasks).values())
        intervals = 0
        while counts[0] > 0:
            i = 0
            while i <= n:
                if counts[0] == 0:
                    break
                if i < len(counts) and counts[i] > 0:
                    counts[i] -= 1
                i += 1
            intervals += i
            counts.sort(reverse=True)
        
        return intervals
            
