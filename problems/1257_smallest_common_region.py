'''
You are given some lists of regions where the first region of each list includes all other regions in that list.

Naturally, if a region x contains another region y then x is bigger than y. Also, by definition, a region x contains itself.

Given two regions: region1 and region2, return the smallest region that contains both of them.

If you are given regions r1, r2, and r3 such that r1 includes r3, it is guaranteed there is no r2 such that r2 includes r3.

It is guaranteed the smallest region exists.



Example 1:

Input:
regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York"
Output: "North America"
Example 2:

Input: regions = [["Earth", "North America", "South America"],["North America", "United States", "Canada"],["United States", "New York", "Boston"],["Canada", "Ontario", "Quebec"],["South America", "Brazil"]], region1 = "Canada", region2 = "South America"
Output: "Earth"


Constraints:

2 <= regions.length <= 104
2 <= regions[i].length <= 20
1 <= regions[i][j].length, region1.length, region2.length <= 20
region1 != region2
regions[i][j], region1, and region2 consist of English letters.
'''

class Solution:
    def fetch_path_for_region(self, curr_node, child_parent_map):
        path = []
        path.append(curr_node)
        while curr_node in child_parent_map:
            parent_node = child_parent_map[curr_node]
            path.append(parent_node)
            curr_node = parent_node
        path.reverse()
        return path

    def findSmallestRegion(
        self, regions: List[List[str]], region1: str, region2: str
    ) -> str:
        child_parent_map = {}
        for region_array in regions:
            parent_node = region_array[0]
            for i in range(1, len(region_array)):
                child_parent_map[region_array[i]] = parent_node
        path1 = self.fetch_path_for_region(region1, child_parent_map)
        path2 = self.fetch_path_for_region(region2, child_parent_map)

        i, j = 0, 0
        lowest_common_ancestor = ""
        while i < len(path1) and j < len(path2) and path1[i] == path2[j]:
            lowest_common_ancestor = path1[i]
            i += 1
            j += 1

        return lowest_common_ancestor

