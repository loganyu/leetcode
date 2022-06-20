/*
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
 

Constraints:

1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * 104
All the strings of products are unique.
products[i] consists of lowercase English letters.
1 <= searchWord.length <= 1000
searchWord consists of lowercase English letters.
*/

type Trie struct {
	Children   []*Trie
	Suggestion []string
}

func NewTrie() *Trie {
	return &Trie{
		Children:   make([]*Trie, 26),
		Suggestion: []string{},
	}
}

func (t *Trie) insert(p string) {
	for i := range p {
		if t.Children[p[i]-'a'] == nil {
			t.Children[p[i]-'a'] = NewTrie()
		}
		t = t.Children[p[i]-'a']
		t.Suggestion = append(t.Suggestion, p)
		sort.Strings(t.Suggestion)
		if len(t.Suggestion) > 3 {
			t.Suggestion = t.Suggestion[:3]
		}
	}
}

func (t *Trie) search(word string) [][]string {
	var res [][]string
	for i := range word {
		if t != nil {
			t = t.Children[word[i]-'a']
		}
		if t == nil {
			res = append(res, []string{})
		} else {
			res = append(res, t.Suggestion)
		}
	}

	return res
}

func suggestedProducts(products []string, searchWord string) [][]string {
	root := NewTrie()
	for _, p := range products {
		root.insert(p)
	}

	return root.search(searchWord)
}

