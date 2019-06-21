'''
Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

 

Example:
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
 

Notes:

0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters
'''
# run length encoding solution
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        s_letters, s_counts = self.RLE(S)
        stretchy = 0
        for word in words:
            w_letters, w_counts = self.RLE(word)
            if w_letters != s_letters:
                continue
            if all(s_count >= max(w_count, 3) or s_count == w_count
                    for s_count, w_count in zip(s_counts, w_counts)):
                stretchy += 1
                
        return stretchy
        
    def RLE(self, S):
        letters = []
        counts = []
        for char in S:
            if not letters or letters[-1] != char:
                letters.append(char)
                counts.append(1)
            else:
                counts[-1] += 1
        return (letters, counts)

# pointer solution
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        count = 0
        for W in words:
            if self.is_expressive(S, W):
                count += 1
        
        return count
    
    def is_expressive(self, S, W):
        i, j, i2, j2, n, m = 0, 0, 0, 0, len(S), len(W)
        while i < n and j < m:
            if S[i] != W[j]:
                return False
            while i2 < n and S[i2] == S[i]:
                i2 += 1
            while j2 < m and W[j2] == W[j]:
                j2 += 1
            if i2 - i != j2 - j and i2 - i < max(j2 - j, 3):
                return False
            i, j = i2, j2
        
        return i == n and j == m
