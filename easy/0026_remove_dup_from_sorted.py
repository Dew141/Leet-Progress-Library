# Problem ID: 26
# Title: Remove duplicates from sorted array
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# Difficulty: Easy

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        # should have been done with a set() but works in the same way
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
                nums[k] = nums[i]
                k += 1
        return k