/*
 * Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.


Follow up: Could you use search pruning to make your solution faster with a larger board?
*/

impl Solution {
    pub fn exist(mut board: Vec<Vec<char>>, word: String) -> bool {
        let (mut row, mut col) = (board.len(), board[0].len());
        if word.len() > row * col { return false }
        for r in 0..row {
            for c in 0..col {
                if Self::word_search(&mut board, &word, r, c, 0) {
                    return true
                }
            }
        }
        false
    }

    fn word_search(mut board: &mut Vec<Vec<char>>, word: &String, row: usize, col: usize, index: usize) -> bool {
        if index == word.len() { return true }
        if let Some(mut word_comb) = board.get_mut(row).and_then(|w| w.get_mut(col)) {
            if *word_comb == word.as_bytes()[index] as char {
                let prev = board[row][col];
                board[row][col] = '-';

                let found = (
                Self::word_search(board, word, row - 1, col, index + 1) ||
                Self::word_search(board, word, row + 1, col, index + 1) ||
                Self::word_search(board, word, row, col - 1, index + 1) ||
                Self::word_search(board, word, row, col + 1, index + 1));
                board[row][col] = prev;

                return found
            } else {
                false
            }
        } else {
            false
        }
    }
}

