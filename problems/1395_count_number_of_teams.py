'''
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).



Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4


Constraints:

n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 105
All the integers in rating are unique.
'''

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        max_rating = 0
        for r in rating:
            max_rating = max(max_rating, r)
        left_BIT = [0] * (max_rating + 1)
        right_BIT = [0] * (max_rating + 1)
        for r in rating:
            self._update_BIT(right_BIT, r, 1)
        teams = 0
        for current_rating in rating:
            self._update_BIT(right_BIT, current_rating, -1)
            smaller_ratings_left = self._get_prefix_sum(
                left_BIT, current_rating - 1
            )
            smaller_ratings_right = self._get_prefix_sum(
                right_BIT, current_rating - 1
            )
            larger_ratings_left = self._get_prefix_sum(
                left_BIT, max_rating
            ) - self._get_prefix_sum(left_BIT, current_rating)
            larger_ratings_right = self._get_prefix_sum(
                right_BIT, max_rating
            ) - self._get_prefix_sum(right_BIT, current_rating)
            teams += smaller_ratings_left * larger_ratings_right
            teams += larger_ratings_left * smaller_ratings_right
            self._update_BIT(left_BIT, current_rating, 1)

        return teams

    def _update_BIT(self, BIT: List[int], index: int, value: int) -> None:
        while index < len(BIT):
            BIT[index] += value
            index += index & (-index)

    def _get_prefix_sum(self, BIT: List[int], index: int) -> int:
        sum = 0
        while index > 0:
            sum += BIT[index]
            index -= index & (-index)
        return sum

