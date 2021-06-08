# Leetcode
# https://leetcode.com/problems/replace-words/


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dict_set = set(dictionary)
        out = []
        for word in sentence.split():
            added = False
            temp = ''
            for letter in word:
                temp += letter
                if temp in dict_set:
                    break
            out.append(temp)
        return ' '.join(out)
