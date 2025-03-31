'''
You are given an array nums of n positive integers and an integer k.

Initially, you start with a score of 1. You have to maximize your score by applying the following operation at most k times:

Choose any non-empty subarray nums[l, ..., r] that you haven't chosen previously.
Choose an element x of nums[l, ..., r] with the highest prime score. If multiple such elements exist, choose the one with the smallest index.
Multiply your score by x.
Here, nums[l, ..., r] denotes the subarray of nums starting at index l and ending at the index r, both ends being inclusive.

The prime score of an integer x is equal to the number of distinct prime factors of x. For example, the prime score of 300 is 3 since 300 = 2 * 2 * 3 * 5 * 5.

Return the maximum possible score after applying at most k operations.

Since the answer may be large, return it modulo 109 + 7.



Example 1:

Input: nums = [8,3,9,3,8], k = 2
Output: 81
Explanation: To get a score of 81, we can apply the following operations:
- Choose subarray nums[2, ..., 2]. nums[2] is the only element in this subarray. Hence, we multiply the score by nums[2]. The score becomes 1 * 9 = 9.
- Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 1, but nums[2] has the smaller index. Hence, we multiply the score by nums[2]. The score becomes 9 * 9 = 81.
It can be proven that 81 is the highest score one can obtain.
Example 2:

Input: nums = [19,12,14,6,10,18], k = 3
Output: 4788
Explanation: To get a score of 4788, we can apply the following operations:
- Choose subarray nums[0, ..., 0]. nums[0] is the only element in this subarray. Hence, we multiply the score by nums[0]. The score becomes 1 * 19 = 19.
- Choose subarray nums[5, ..., 5]. nums[5] is the only element in this subarray. Hence, we multiply the score by nums[5]. The score becomes 19 * 18 = 342.
- Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 2, but nums[2] has the smaller index. Hence, we multipy the score by nums[2]. The score becomes 342 * 14 = 4788.
It can be proven that 4788 is the highest score one can obtain.


Constraints:

1 <= nums.length == n <= 105
1 <= nums[i] <= 105
1 <= k <= min(n * (n + 1) / 2, 109)
'''

class Solution:
    MOD = int(1e9 + 7)

    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prime_scores = [0] * n
        max_element = max(nums)
        primes = self.get_primes(max_element)
        for index in range(n):
            num = nums[index]
            for prime in primes:
                if prime * prime > num:
                    break
                if num % prime != 0:
                    continue

                prime_scores[index] += 1
                while num % prime == 0:
                    num //= prime
            if num > 1:
                prime_scores[index] += 1
        next_dominant = [n] * n
        prev_dominant = [-1] * n
        decreasing_prime_score_stack = deque()
        for index in range(n):
            while (
                decreasing_prime_score_stack
                and prime_scores[decreasing_prime_score_stack[-1]]
                < prime_scores[index]
            ):
                top_index = decreasing_prime_score_stack.pop()
                next_dominant[top_index] = index
            if decreasing_prime_score_stack:
                prev_dominant[index] = decreasing_prime_score_stack[-1]
            decreasing_prime_score_stack.append(index)
        num_of_subarrays = [
            (next_dominant[i] - i) * (i - prev_dominant[i]) for i in range(n)
        ]
        sorted_array = sorted(enumerate(nums), key=lambda x: -x[1])
        score = 1

        def _power(base, exponent):
            res = 1
            while exponent > 0:
                if exponent % 2:
                    res = (res * base) % self.MOD
                base = (base * base) % self.MOD
                exponent //= 2

            return res

        processing_index = 0

        while k > 0:
            index, num = sorted_array[processing_index]
            processing_index += 1
            operations = min(k, num_of_subarrays[index])
            score = (score * _power(num, operations)) % self.MOD
            k -= operations

        return score

    def get_primes(self, limit: int) -> List[int]:
        is_prime = [True] * (limit + 1)
        primes = []
        for number in range(2, limit + 1):
            if not is_prime[number]:
                continue
            primes.append(number)
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False

        return primes

