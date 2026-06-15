class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        # [7,1,7,2,2,4]
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index
                maxarea = max(maxarea, width*height)
                start = index
            stack.append((start, h))
        for i, h in stack:
            maxarea = max(maxarea, h * (len(heights) - i))
        return maxarea
