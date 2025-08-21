/*
 * Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.



Example 1:

Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.
Example 2:

Input: n = 6, k = 1, maxPts = 10
Output: 0.60000
Explanation: Alice gets a single card, then stops.
In 6 out of 10 possibilities, she is at or below 6 points.
Example 3:

Input: n = 21, k = 17, maxPts = 10
Output: 0.73278


Constraints:

0 <= k <= n <= 104
1 <= maxPts <= 104
*/

impl Solution {
    pub fn new21_game(n: i32, k: i32, max_pts: i32) -> f64 {
        if k == 0 || n >= k - 1 + max_pts {
            return 1.0;
        }

        let n_usize = n as usize;
        let k_usize = k as usize;
        let max_pts_usize = max_pts as usize;
        let max_pts_f64 = max_pts as f64;

        let mut dp = vec![0.0; n_usize + 1];

        dp[0] = 1.0;

        let mut s = 1.0;

        for i in 1..=n_usize {
            dp[i] = s / max_pts_f64;
            if i < k_usize {
                s += dp[i];
            }
            if i >= max_pts_usize && i - max_pts_usize < k_usize {
                s -= dp[i - max_pts_usize];
            }
        }

        dp[k_usize..].iter().sum()
    }
}
