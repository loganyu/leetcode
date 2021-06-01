=begin
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
=end

# @param {Integer[]} nums
# @return {String[]}
def summary_ranges(nums)
    if nums.empty?
        return []
    end
    summary = []
    prev_num = nil
    range_start = nil
    nums.each do |num|
        if range_start.nil?
            range_start = num
        elsif prev_num + 1 != num
            add_range_to_summary(range_start, prev_num, summary)
            range_start = num
        end
        prev_num = num
    end
    add_range_to_summary(range_start, prev_num, summary)

    return summary
end

def add_range_to_summary(range_start, prev_num, summary)
    if range_start == prev_num
        summary << "#{range_start}"
    else
        summary << "#{range_start}->#{prev_num}"
    end
end

