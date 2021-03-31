'''
You want to form a target string of lowercase letters.

At the beginning, your sequence is target.length '?' marks.  You also have a stamp of lowercase letters.

On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.  You can make up to 10 * target.length turns.

For example, if the initial sequence is "?????", and your stamp is "abc",  then you may make "abc??", "?abc?", "??abc" in the first turn.  (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)

If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped at each turn.  If the sequence is not possible to stamp, return an empty array.

For example, if the sequence is "ababc", and the stamp is "abc", then we could return the answer [0, 2], corresponding to the moves "?????" -> "abc??" -> "ababc".

Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within 10 * target.length moves.  Any answers specifying more than this number of moves will not be accepted.

 

Example 1:

Input: stamp = "abc", target = "ababc"
Output: [0,2]
([1,0,2] would also be accepted as an answer, as well as some other answers.)
Example 2:

Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]
 

Note:

1 <= stamp.length <= target.length <= 1000
stamp and target only contain lowercase letters.
'''

from collections import deque

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, m, t, s, res = len(target), len(stamp), list(target), list(stamp), []
        
        def check(i):
            changed = False
            for j in range(m):
                if t[i+j] == '?':
                    continue
                if t[i + j] != s[j]:
                    return False
                changed = True
            if changed:
                t[i:i + m] = ['?'] * m
                res.append(i)
                
            return changed
    
        changed = True
        while changed:
            changed = False
            for i in range(n-m+1):
                changed |= check(i)
        
        return res[::-1] if t == ['?'] * n else []

