# Leetcode
# https://leetcode.com/problems/implement-trie-prefix-tree/


class TrieNode:
    def __init__(self, character=None, is_word=False):
        self.d = {}
        self.is_word = is_word


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
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
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for letter in word:
            curr = curr.d.get(letter)
            if not curr:
                return False
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for letter in prefix:
            curr = curr.d.get(letter)
            if not curr:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
