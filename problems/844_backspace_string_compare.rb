=begin
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
=end

# @param {String} s
# @param {String} t
# @return {Boolean}
def backspace_compare(s, t)
    i = s.length - 1
    j = t.length - 1
    skip_s = 0
    skip_t = 0
    while i >= 0 || j >= 0
        while i >= 0
            if s[i] == '#'
                skip_s += 1
                i -= 1
            elsif skip_s > 0
                skip_s -= 1
                i -= 1
            else
                break
            end
        end
        while j >= 0
            if t[j] == '#'
                skip_t += 1
                j -= 1
            elsif skip_t > 0
                skip_t -= 1
                j -= 1
            else
                break
            end
        end
        
        if i >= 0 && j >=0 && s[i] != t[j]
            return false
        end
        if i >= 0 != j >= 0
            return false
        end
        i -= 1
        j -= 1
    end
    
    return true
end

=begin
O(n+m) space solution
def backspace_compare(s, t)
    build(s) == build(t)
end

def build(string)
   ans = []
    string.each_char do |char|
        if char != '#'
            ans.push(char)
        elsif ans[0]
            ans.pop
        end
    end
    ans.join
end
=end

