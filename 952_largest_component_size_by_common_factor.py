'''
Given a non-empty array of unique positive integers A, consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

 

Example 1:

Input: [4,6,15,35]
Output: 4

Example 2:

Input: [20,50,9,63]
Output: 2

Example 3:

Input: [2,3,6,7,4,12,21,39]
Output: 8

Note:

1 <= A.length <= 20000
1 <= A[i] <= 100000
'''

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        dsu = DisjointSetUnion(max(A))
        for a in A:
            for factor in range(2, int(sqrt(a))+1):
                if a % factor == 0:
                    dsu.union(a, factor)
                    dsu.union(a, a // factor)
        
        group_count = defaultdict(int)
        for a in A:
            group_id = dsu.find(a)
            group_count[group_id] += 1
        
        return max(group_count.values())

class DisjointSetUnion(object):
    def __init__(self, size):
        self.parent = [i for i in range(size+1)]
        self.size = [1] * (size+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return px
        if self.size[px] > self.size[py]:
                px, py = py, px
        self.parent[px] = py
        self.size[py] += self.size[px]
        
        return py
               
# prime decompose
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        dsu = DisjointSetUnion(max(A))
        num_factor_map = {}
        
        for num in A:
            prime_factors = list(set(self.primeDecompose(num)))
            num_factor_map[num] = prime_factors[0]
            for i in range(len(prime_factors)-1):
                dsu.union(prime_factors[i], prime_factors[i+1])
        
        group_count = defaultdict(int)
        for num in A:
            group_id = dsu.find(num_factor_map[num])
            group_count[group_id] += 1
        
        return max(group_count.values())
    
    def primeDecompose(self, num):
        factor = 2
        prime_factors = []
        while num >= factor * factor:
            if num % factor == 0:
                prime_factors.append(factor)
                num = num // factor
            else:
                factor += 1
        prime_factors.append(num)
        
        return prime_factors
            

class DisjointSetUnion(object):
    def __init__(self, size):
        self.parent = [i for i in range(size+1)]
        self.size = [1] * (size+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return px
        if self.size[px] > self.size[py]:
                px, py = py, px
        self.parent[px] = py
        self.size[py] += self.size[px]
        
        return py
               
