class Solution(object):
    def maximumScore(self, nums, k):
        n = len(nums)
        left, right = [0] * n, [0] * n
        stack = []

        # Find the left boundaries of good subarrays
        for i in range(n):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []

        # Find the right boundaries of good subarrays
        for i in range(n - 1, -1, -1):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        max_score = 0

        for i in range(n):
            if left[i] < k < right[i]:
                score = nums[i] * (right[i] - left[i] - 1)
                max_score = max(max_score, score)

        return max_score
