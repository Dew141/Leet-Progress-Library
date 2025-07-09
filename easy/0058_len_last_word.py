# Problem ID: 58
# Title: Length of last word
# URL: https://leetcode.com/problems/length-of-last-word/
# Difficulty: Easy

# Time Complexity: O(m) where m is the length of the last word; O(n) worst case 
# Space Complexity: O(1)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_length = 0
        for i in reversed(s):
            if i == ' ' and str_length != 0:
                break
            elif i != ' ':
                str_length += 1
        return str_length