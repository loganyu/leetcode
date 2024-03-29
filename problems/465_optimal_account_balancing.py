'''
A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be represented as [[0, 1, 10], [2, 0, 5]].

Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.

Note:

A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.
Example 1:

Input:
[[0,1,10], [2,0,5]]

Output:
2

Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.

Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
Example 2:

Input:
[[0,1,10], [1,0,1], [1,2,5], [2,0,5]]

Output:
1

Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.

Therefore, person #1 only need to give person #0 $4, and all debt is settled.
'''

from collections import Counter, deque

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        bal = Counter()
        for t in transactions:
            bal[t[0]] -= t[2]
            bal[t[1]] += t[2]
        net_profit = [v for k,v in bal.items() if v != 0]
        
        return self.traverse(net_profit, 0, 0)
    
    def traverse(self, net_profit, start_idx, num_trans):
        while start_idx < len(net_profit) and net_profit[start_idx] == 0:
            start_idx += 1
        if start_idx + 1 >= len(net_profit):
            return num_trans
        
        for i in range(start_idx + 1, len(net_profit)):
            if net_profit[start_idx] + net_profit[i] == 0: 
                net_profit[i] += net_profit[start_idx]
                min_num_trans = self.traverse(net_profit, start_idx + 1, num_trans + 1)
                net_profit[i] -= net_profit[start_idx]

                return min_num_trans
        
        min_num_trans = float("inf")
        for i in range(start_idx + 1, len(net_profit)):
            if net_profit[start_idx] * net_profit[i] < 0:
                net_profit[i] += net_profit[start_idx]
                min_num_trans = min(min_num_trans, self.traverse(net_profit, start_idx + 1, num_trans + 1))
                net_profit[i] -= net_profit[start_idx]
        
        return min_num_trans

