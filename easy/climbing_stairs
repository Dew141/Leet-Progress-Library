# Leetcode problem #70:
# URL: https://leetcode.com/problems/climbing-stairs/
# Difficulty: Easy

# Time Complexity: O(n)
# Space Complexity: O(n)
# Space complexity can be optimized to O(1) by storing only the previous two values

class Solution:
    def climbStairs(self, n: int) -> int:
        # the number of combinations of the current stair, n, 
        # is the sum of previous two (n - 1 and n - 2) stairs
        steps = [1, 2]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        for i in range(n-2):
            end_val = steps[-1]
            end_val2 = steps[-2]
            new_val = end_val + end_val2
            steps.append(new_val)
        return steps[n - 1]
