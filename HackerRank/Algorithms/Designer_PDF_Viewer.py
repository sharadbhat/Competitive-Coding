# HACKERRANK
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

import sys

def designerPdfViewer(h, word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    heights = {i:h[letters.index(i)] for i in letters}
    maximum = 0
    for i in word:
        if maximum < heights[i]:
            maximum = heights[i]
    return (maximum * len(word))

if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)
