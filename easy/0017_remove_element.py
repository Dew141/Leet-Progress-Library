# Problem ID: 17
# Title: Remove element
# URL: https://leetcode.com/problems/remove-element/
# Difficulty: Easy

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
