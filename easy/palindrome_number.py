# Leetcode problem #9:
# URL: https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy

# Time Complexity: O(log(n))
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (but not 0 itself) can't be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even digits: x == reversed_half
        # For odd digits: x == reversed_half // 10 (ignore middle digit)
        return x == reversed_half or x == reversed_half // 10


