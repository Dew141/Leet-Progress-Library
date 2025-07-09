# Leetcode problem #88:
# URL: https://leetcode.com/problems/merge-sorted-array/
# Difficulty: Easy

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
 
   def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # I wanted to move numbers over from the back to the front to avoid explicitly 
        # overwriting when inserting
        for i in range(m + n - 1, -1, -1):
            # if we still have numbers needed to be sorted
            if m > 0 and n > 0:
                if nums1[m - 1] >= nums2[n - 1]:
                    nums1[i] = nums1[m - 1]
                    m -= 1
                else:
                    nums1[i] = nums2[n - 1]
                    n -= 1
            # no m > 0 necessary as that means they are all in place
            elif n > 0:
                nums1[i] = nums2[n - 1]
                n -= 1
