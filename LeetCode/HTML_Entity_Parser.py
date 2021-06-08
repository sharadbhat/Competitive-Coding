# Leetcode
# https://leetcode.com/problems/html-entity-parser/


class Solution:
    def entityParser(self, text: str) -> str:
        d = {
            "&quot;": '"',
            "&apos;": "'",
            "&gt;": '>',
            "&lt;": '<',
            "&frasl;": '/',
            "&amp;": '&',
        }

        for i in d:
            text = text.replace(i, d[i])

        return text
