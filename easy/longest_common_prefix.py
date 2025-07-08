# Leetcode problem #14:
# URL: https://leetcode.com/problems/longest-common-prefix/
# Difficulty: Easy

# Time Complexity: O(n * m) n is the number of strings, m is the length of prefix
# Space Complexity: O(m)

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        for i in strs:
            # if the List is empty, then we return an empty string
            if pre == "":
                return pre

            # storage variable for the new prefix
            newPre = ""

            # checks for only the shortest string to avoid index out of bounds
            mini = min(len(pre), len(i))
            for a in range(mini):
                if pre[a] == i[a]:
                    newPre += pre[a]
                else:
                    break
            
            # store the new "shortest" prefix
            pre = newPre
        return pre
        
        