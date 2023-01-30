/*
You are given two strings current and correct representing two 24-hour times.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

In one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform this operation any number of times.

Return the minimum number of operations needed to convert current to correct.

 

Example 1:

Input: current = "02:30", correct = "04:35"
Output: 3
Explanation:
We can convert current to correct in 3 operations as follows:
- Add 60 minutes to current. current becomes "03:30".
- Add 60 minutes to current. current becomes "04:30".
- Add 5 minutes to current. current becomes "04:35".
It can be proven that it is not possible to convert current to correct in fewer than 3 operations.
Example 2:

Input: current = "11:00", correct = "11:01"
Output: 1
Explanation: We only have to add one minute to current, so the minimum number of operations needed is 1.
 

Constraints:

current and correct are in the format "HH:MM"
current <= correct
*/

impl Solution {
    pub fn convert_time(current: String, correct: String) -> i32 {
        if current == correct {
            return 0;
        }

        let to_num = |s: &str| -> i32 { s.parse().unwrap() };
        let (h2, m2) = (to_num(&correct[..2]), to_num(&correct[3..]));
        let (h1, m1) = (to_num(&current[..2]), to_num(&current[3..]));

        let mut delta = (m2 - m1) + 60 * if h2 >= h1 { h2 - h1 } else { h2 - h1 + 24 };
        let mut res = 0;

        for op in [60, 15, 5] {
            res += delta / op;
            delta %= op;
        }

        res + delta
    }
}

