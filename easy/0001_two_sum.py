# Problem ID : 1
# Title: Two sum
# Difficulty: Easy
# Problem URL: https://leetcode.com/problems/two-sum/

# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i