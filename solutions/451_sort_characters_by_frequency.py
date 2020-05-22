'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return s
        counts = Counter(s)
        max_freq = max(counts.values())
        buckets = [[] for _ in range(max_freq + 1)]
        for char, count in counts.items():
            buckets[count].append(char)
        
        string_builder = []
        for i in reversed(range(1, len(buckets))):
            for char in buckets[i]:
                string_builder.append(char * i)
        
        return "".join(string_builder)
        
