/*
 * You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.



Example 1:


Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
Example 2:


Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.


Constraints:

1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
*/

use std::collections::HashMap;

impl Solution {
    pub fn find_itinerary(tickets: Vec<Vec<String>>) -> Vec<String> {
        let mut graph: HashMap<String, Vec<String>> = HashMap::new();

        for ticket in &tickets {
            let (src, dst) = (ticket[0].clone(), ticket[1].clone());
            graph.entry(src.clone()).or_insert(vec![]).push(dst);
        }

        for destinations in graph.values_mut() {
            destinations.sort_by(|a, b| b.cmp(a));
        }

        let mut itinerary = vec![];

        fn dfs(graph: &mut HashMap<String, Vec<String>>, airport: &str, itinerary: &mut Vec<String>) {
            while let Some(next) = graph.get_mut(airport).and_then(|dests| dests.pop()) {
                dfs(graph, &next, itinerary);
            }
            itinerary.push(airport.to_string());
        }

        dfs(&mut graph, "JFK", &mut itinerary);

        itinerary.reverse();

        itinerary
    }
}

