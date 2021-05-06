# Leetcode
# https://leetcode.com/problems/implement-magic-dictionary/


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        for i in dictionary:
            self.d[len(i)].add(i)

    def search(self, searchWord: str) -> bool:
        words = self.d[len(searchWord)]
        for word in words:
            diff = 0
            for i, j in zip(word, searchWord):
                if i != j:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                return True

        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
