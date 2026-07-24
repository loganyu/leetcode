'''
You are given a binary string s of length n, where:

'1' represents an active section.
'0' represents an inactive section.
You can perform at most one trade to maximize the number of active sections in s. In a trade, you:

Convert a contiguous block of '1's that is surrounded by '0's to all '0's.
Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.
Additionally, you are given a 2D array queries, where queries[i] = [li, ri] represents a substring s[li...ri].

For each query, determine the maximum possible number of active sections in s after making the optimal trade on the substring s[li...ri].

Return an array answer, where answer[i] is the result for queries[i].

Note

For each query, treat s[li...ri] as if it is augmented with a '1' at both ends, forming t = '1' + s[li...ri] + '1'. The augmented '1's do not contribute to the final count.
The queries are independent of each other.


Example 1:

Input: s = "01", queries = [[0,1]]

Output: [1]

Explanation:

Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

Example 2:

Input: s = "0100", queries = [[0,3],[0,2],[1,3],[2,3]]

Output: [4,3,1,1]

Explanation:

Query [0, 3] → Substring "0100" → Augmented to "101001"
Choose "0100", convert "0100" → "0000" → "1111".
The final string without augmentation is "1111". The maximum number of active sections is 4.

Query [0, 2] → Substring "010" → Augmented to "10101"
Choose "010", convert "010" → "000" → "111".
The final string without augmentation is "1110". The maximum number of active sections is 3.

Query [1, 3] → Substring "100" → Augmented to "11001"
Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

Query [2, 3] → Substring "00" → Augmented to "1001"
Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

Example 3:

Input: s = "1000100", queries = [[1,5],[0,6],[0,4]]

Output: [6,7,2]

Explanation:

Query [1, 5] → Substring "00010" → Augmented to "1000101"
Choose "00010", convert "00010" → "00000" → "11111".
The final string without augmentation is "1111110". The maximum number of active sections is 6.

Query [0, 6] → Substring "1000100" → Augmented to "110001001"
Choose "000100", convert "000100" → "000000" → "111111".
The final string without augmentation is "1111111". The maximum number of active sections is 7.

Query [0, 4] → Substring "10001" → Augmented to "1100011"
Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 2.

Example 4:

Input: s = "01010", queries = [[0,3],[1,4],[1,3]]

Output: [4,4,2]

Explanation:

Query [0, 3] → Substring "0101" → Augmented to "101011"
Choose "010", convert "010" → "000" → "111".
The final string without augmentation is "11110". The maximum number of active sections is 4.

Query [1, 4] → Substring "1010" → Augmented to "110101"
Choose "010", convert "010" → "000" → "111".
The final string without augmentation is "01111". The maximum number of active sections is 4.

Query [1, 3] → Substring "101" → Augmented to "11011"
Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 2.



Constraints:

1 <= n == s.length <= 105
1 <= queries.length <= 105
s[i] is either '0' or '1'.
queries[i] = [li, ri]
0 <= li <= ri < n

'''

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n, m = len(s), len(queries)
        cnt1 = s.count("1")

        left = [-1] * n
        right = [-1] * n
        for i in range(n):
            left[i] = left[i - 1] + 1 if i > 0 and s[i - 1] == s[i] else 1
        for i in range(n - 1, -1, -1):
            right[i] = right[i + 1] + 1 if i < n - 1 and s[i + 1] == s[i] else 1

        ans = [-1] * m
        block_size = isqrt(n)

        longQueries = []

        def brute_force(l, r) -> int:
            i = l
            best = 0
            prev = -inf

            while i <= r:
                start = i

                while i <= r and s[i] == s[start]:
                    i += 1

                if s[start] == "0":
                    cur = i - start
                    best = prev + cur if prev + cur > best else best
                    prev = cur
            return best

        for i, (l, r) in enumerate(queries):
            if r - l + 1 > block_size:
                longQueries.append((l // block_size, l, r, i))
            else:
                ans[i] = cnt1 + brute_force(l, r)

        longQueries.sort(key=lambda q: (q[0], q[2]))
        subZeroBlocks = deque()

        for i, (bid, l, r, qid) in enumerate(longQueries):
            if (i == 0 or bid > longQueries[i - 1][0]):
                L = (bid + 1) * block_size - 1
                R = (bid + 1) * block_size
                subZeroBlocks.clear()
                bestGain = 0

            while R <= r:
                sz = min(r - R + 1, right[R])
                if s[R] == "0":
                    if subZeroBlocks and s[R - 1] == "0":
                        subZeroBlocks[-1] += sz
                    else:
                        subZeroBlocks.append(sz)
                    if len(subZeroBlocks) >= 2:
                        bestGain = max(
                            subZeroBlocks[-1] + subZeroBlocks[-2], bestGain
                        )
                R += sz

            tmp_bestGain = bestGain
            tmp_firstValue = subZeroBlocks[0] if subZeroBlocks else None
            cnt = 0

            while L >= l:
                sz = min(L - l + 1, left[L])
                if s[L] == "0":
                    if subZeroBlocks and s[L + 1] == "0":
                        subZeroBlocks[0] += sz
                    else:
                        subZeroBlocks.appendleft(sz)
                        cnt += 1
                    if len(subZeroBlocks) >= 2:
                        bestGain = max(
                            subZeroBlocks[0] + subZeroBlocks[1], bestGain
                        )
                L -= sz

            ans[qid] = bestGain + cnt1

            L = (bid + 1) * block_size - 1

            bestGain = tmp_bestGain

            for _ in range(cnt):
                subZeroBlocks.popleft()
            if tmp_firstValue:
                subZeroBlocks[0] = tmp_firstValue
        return ans

