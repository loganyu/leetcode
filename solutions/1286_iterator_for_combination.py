'''
Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
 

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
 

Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.
'''

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        n, k = len(characters), combinationLength
        
        def backtrack(first = 0, curr = []):
            if len(curr) == k:
                self.combinations.append(''.join(curr))
                return
            for i in range(first, n):
                curr.append(characters[i])
                backtrack(i+1, curr)
                curr.pop()
        backtrack()
        self.combinations.reverse()

    def next(self) -> str:
        return self.combinations.pop()

    def hasNext(self) -> bool:
        return self.combinations
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        n, k = len(characters), combinationLength
        
        for bitmask in range(1 << n):
            if bin(bitmask).count('1') == k:
                curr = [characters[j] for j in range(n) if bitmask & (1 << n - j - 1)]
                self.combinations.append(''.join(curr))

    def next(self) -> str:
        return self.combinations.pop()

    def hasNext(self) -> bool:
        return self.combinations
        
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.n = n = len(characters)
        self.k = k = combinationLength
        self.chars = characters
        
        self.b = (1 << n) - (1 << n - k)

    def next(self) -> str:
        curr = [self.chars[j] for j in range(self.n) if self.b & (1 << self.n - j - 1)]
        self.b -= 1
        while self.b > 0 and bin(self.b).count('1') != self.k:
            self.b -= 1
        
        return ''.join(curr)

    def hasNext(self) -> bool:
        return self.b > 0

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.n = len(characters)
        self.k = k = combinationLength
        self.chars = characters
        
        self.nums = list(range(k))
        self.has_next = True

    def next(self) -> str:
        nums = self.nums
        n, k = self.n, self.k
        curr = [self.chars[j] for j in nums]
        
        j = k - 1
        while j >= 0 and nums[j] == n - k + j:
            j -= 1
        nums[j] += 1
        
        if j >= 0:
            for i in range(j+1, k):
                nums[i] = nums[j] + i - j
        else:
            self.has_next = False
        
        return ''.join(curr)

    def hasNext(self) -> bool:
        return self.has_next

