/*
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

 

Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
*/

class Solution {
    int[][] mat;
    int n, m;
    
    public int[][] diagonalSort(int[][] mat) {
        this.mat = mat;
        n = mat.length;
        m = mat[0].length;
        
        for (int x = 0; x < n; ++x) 
            sort(x, 0);
        for (int y = 0; y < m; ++y)
            sort(0, y);
        
        return mat;
    }
    
    public void sort(int x, int y) {
        List<Integer> diagonal = new ArrayList<>();
        while (x < n && y < m) {
            diagonal.add(mat[x][y]);
            ++x;
            ++y;
        }
        
        Collections.sort(diagonal);
        
        while (x > 0 && y > 0) {
            --x;
            --y;
            mat[x][y] = diagonal.remove(diagonal.size() - 1);
        }
    }
}	

