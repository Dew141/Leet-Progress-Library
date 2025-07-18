# Problem ID: 65
# Title: Search insert position
# URL: https://leetcode.com/problems/search-insert-position/
# Difficulty: Easy

# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                return mid
        return left
            