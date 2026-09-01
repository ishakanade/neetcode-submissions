class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # area = min(height) * (curr_idx - start_idx)
        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                area = height * (i - idx)
                start = idx
                max_area = max(max_area, area)
            stack.append([start,h])
        for i, h in stack:
            max_area = max(max_area, h*(len(heights)-i))
        return max_area