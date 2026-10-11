from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        h = 0

        for i in range(len(heights)):
            start = i

            while stack and stack[-1][1] > heights[i]:
                top = stack.pop()
                h1 = top[1] * (i - top[0])
                h = max(h, h1)
                start = top[0]

            stack.append([start, heights[i]])

        for i in range(len(stack)):
            top = stack[i]
            h1 = top[1] * (len(heights) - top[0])
            h = max(h, h1)

        return h

