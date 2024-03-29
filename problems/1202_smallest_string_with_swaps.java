/*
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

 

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"
 

Constraints:

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
*/

class Solution {
    final static int n = 100001;
    boolean[] visited = new boolean[n];
    List<Integer>[] adj = new ArrayList[n];
    
    public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
        for (int i = 0; i < s.length(); i++) {
            adj[i] = new ArrayList<Integer>();
        }
        
        for (List<Integer> edge : pairs) {
            int source = edge.get(0);
            int destination = edge.get(1);
            adj[source].add(destination);
            adj[destination].add(source);
        }
        
        char[] answer = new char[s.length()];
        for (int vertex = 0; vertex < s.length(); vertex++) {
            if (!visited[vertex]) {
                List<Character> characters = new ArrayList<>();
                List<Integer> indices = new ArrayList<>();
                
                dfs(s, vertex, characters, indices);
                Collections.sort(characters);
                Collections.sort(indices);

                for (int index = 0; index < characters.size(); index++) {
                    answer[indices.get(index)] = characters.get(index);
                }
            }
        }
        return new String(answer);
    }
    
    private void dfs(String s, int vertex, List<Character> characters, List<Integer> indices) {
        characters.add(s.charAt(vertex));
        indices.add(vertex);
        
        visited[vertex] = true;
        
        for (int adjacent : adj[vertex]) {
            if (!visited[adjacent]) {
                dfs(s, adjacent, characters, indices);
            }
        }
    }
}

