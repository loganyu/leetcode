'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

class Solution:
    letters_by_digit = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def letterCombinations(self, digits: str) -> List[str]:
        combos = []
        if digits:
            self.backtrack('', digits, combos)

        return combos

    def backtrack(self, combo, digits, combos):
        i = len(combo)
        if i == len(digits):
            combos.append(combo)
        else:
            for letter in self.letters_by_digit[digits[i]]:
                self.backtrack(combo + letter, digits, combos)
