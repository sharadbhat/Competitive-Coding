# Leetcode
# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self, is_word=False):
        self.d = {}
        self.is_word = is_word

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter in curr.d:
                curr = curr.d[letter]
            else:
                new_node = TrieNode()
                curr.d[letter] = new_node
                curr = new_node
        
        curr.is_word = True

    def search(self, word: str) -> bool:
        return self.findWord(self.root, word)
    
    def findWord(self, curr: TrieNode, word: str) -> bool:
        if len(word) == 0:
            return curr.is_word
        
        if word[0] not in curr.d and word[0] != '.':
            return False
        
        if word[0] == '.':
            for i in curr.d:
                if self.findWord(curr.d[i], word[1:]):
                    return True
            return False
        else:
            return self.findWord(curr.d[word[0]], word[1:])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)