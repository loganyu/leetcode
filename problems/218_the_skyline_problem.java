/*
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

Buildings Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
*/

class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        int n = buildings.length;
        List<List<Integer>> output = new ArrayList<List<Integer>>();
        
        if (n == 0) return output;
        if (n == 1) {
            int xStart = buildings[0][0];
            int xEnd = buildings[0][1];
            int y = buildings[0][2];
            
            output.add(new ArrayList<Integer>() {{add(xStart); add(y); }});
            output.add(new ArrayList<Integer>() {{add(xEnd); add(0); }});
            
            return output;
        }
        
        List<List<Integer>> leftSkyline, rightSkyline;
        leftSkyline = getSkyline(Arrays.copyOfRange(buildings, 0, n / 2));
        rightSkyline = getSkyline(Arrays.copyOfRange(buildings, n / 2, n));
        
        return mergeSkylines(leftSkyline, rightSkyline);
    }
    
    public List<List<Integer>> mergeSkylines(List<List<Integer>> left, List<List<Integer>> right) {
        int nL = left.size(), nR = right.size();
        int pL = 0, pR = 0;
        int currY = 0, leftY = 0, rightY = 0;
        int x, maxY;
        List<List<Integer>> output = new ArrayList<List<Integer>>();
        
        while ((pL < nL) && (pR < nR)) {
            List<Integer> pointL = left.get(pL);
            List<Integer> pointR = right.get(pR);
            
            if (pointL.get(0) < pointR.get(0)) {
                x = pointL.get(0);
                leftY = pointL.get(1);
                pL++;
            }
            else {
                x = pointR.get(0);
                rightY = pointR.get(1);
                pR++;
            }
            
            maxY = Math.max(leftY, rightY);
            if (currY != maxY) {
                updateOutput(output, x, maxY);
                currY = maxY;
            }
        }
        appendSkyline(output, left, pL, nL, currY);
        appendSkyline(output, right, pR, nR, currY);

        return output;
    }
    
    public void updateOutput(List<List<Integer>> output, int x, int y) {
        if (output.isEmpty() || output.get(output.size() - 1).get(0) != x)
            output.add(new ArrayList<Integer>() {{add(x); add(y); }});
        else
            output.get(output.size() - 1).set(1, y);
    }
    
    public void appendSkyline(List<List<Integer>> output, List<List<Integer>> skyline, int p, int n, int currY) {
        while (p < n) {
            List<Integer> point = skyline.get(p);
            int x = point.get(0);
            int y = point.get(1);
            p++;
            
            if (currY != y) {
                updateOutput(output, x, y);
                currY = y;
            }
        }
    }
}

