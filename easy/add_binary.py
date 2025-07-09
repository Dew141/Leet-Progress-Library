# Leetcode problem #67:
# URL: https://leetcode.com/problems/add-binary/
# Difficulty: Easy

# Time Complexity: O(n + m): length of a is n and length of b is m
# Space Complexity: O(n + m)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # int() converts string to an integer, second arg defines the base
        sum_val = int(a, 2) + int(b, 2)
        result = bin(sum_val)[2:]  # Remove '0b' prefix
        return result