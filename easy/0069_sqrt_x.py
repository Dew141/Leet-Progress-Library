# Problem ID: 69
# Title: Sqrtx
# URL: https://leetcode.com/problems/sqrtx/
# Difficulty: Easy

# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def mySqrt(self, x: int) -> int:
        # Binary search to find a valid integer solution
        # we can treat integers as already sorted arrays
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            mid_sq = mid * mid
            if mid_sq == x:
                return mid
            elif mid_sq > x:
                right = mid - 1
            elif mid_sq < x:
                left = mid + 1
        return right