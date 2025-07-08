# Leetcode problem #1394:
# URL: https://leetcode.com/problems/find-lucky-integer-in-an-array/
# Difficulty: Easy

# Time Complexity: O(n + m) n is the number of ints in the List, m is the number of keys
# Space Complexity: O(m)

from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dict = {}
        largest_vkey = -1
        for i in range(len(arr)):
            # if the key doesn't exist, set the default value to 0, and add 1 to it
            dict[arr[i]] = dict.get(arr[i], 0) + 1
        keys = dict.keys()
        for k in keys:
            # check for the number of repititions with the key
            if k == dict[k] and k > largest_vkey:
                largest_vkey = k
        return largest_vkey