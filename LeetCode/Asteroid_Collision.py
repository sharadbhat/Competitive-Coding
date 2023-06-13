# Leetcode
# https://leetcode.com/problems/asteroid-collision

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        while True:
            found = False
            for i in asteroids:
                if len(stack) > 0 and i < 0 and stack[-1] > 0:
                    found = True
                    if abs(i) > stack[-1]:
                        stack[-1] = i
                    elif abs(i) == stack[-1]:
                        stack.pop()
                else:
                    stack.append(i)

            if not found:
                break
            else:
                asteroids = list(stack)
                stack = []
        
        return stack