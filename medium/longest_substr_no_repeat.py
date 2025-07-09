# Leetcode problem #3:
# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Difficulty: Medium

# Time Complexity: O(n)
# Space Complexity: O(n)












"""
Naive solution:

Time: O(nm) n the length of string, m the length of substring
Space = O(n)
"""
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         longest = 0
#         current = 0
#         dict = {}
#         for i in range(len(s)):
#             letter = s[i]
#             index = i
#             while letter not in dict and index <= len(s):
#                 dict[letter] = 1
#                 current += 1
#                 index += 1
#                 if index == len(s):
#                     break
#                 letter = s[index]
#             dict = {}
#             if current > longest:
#                 longest = current
#             current = 0
#         return longest