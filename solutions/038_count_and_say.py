'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''

class Solution:
    def countAndSay(self, n: int) -> str:
        counts = [[None],[1]]
        for i in range(1, n):
            count = []
            n_cur = None
            n_count = 0
            
            for num in counts[i]:
                if n_cur == None or n_cur != num:
                    if n_cur:
                        count.append(n_count)
                        count.append(n_cur)
                    n_cur = num
                    n_count = 0
                n_count += 1
            count.append(n_count)
            count.append(n_cur)
            counts.append(count)
            
        return "".join(map(str, counts[n]))
        
