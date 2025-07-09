# Problem ID: 66
# Title: Plus one
# URL: https://leetcode.com/problems/plus-one/description/
# Difficulty: Easy

# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Perform the + 1 on the last digit
        digits[-1] += 1

        for i in range(len(digits) - 1, -1, -1):
            # if there is no carry, no further change necessary
            if digits[i] < 10:
                return digits
            digits[i] = 0
            # Case if we reach the end with a carry
            if i == 0:
                digits.insert(0, 1)
            # Otherwise, propogate the carry through
            else:
                digits[i - 1] += 1
        # will only return once it ends
        return digits