# Problem ID: 13
# Title: Roman to integer
# URL: https://leetcode.com/problems/roman-to-integer/
# Difficulty: Easy

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        # Pair roman numerals to their respective values using a dictionary (hash)
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        val = 0
        n = len(s)
        
        for i in range(n):
            # Storage of current and next values to avoid index out of bounds
            current_val = roman_values[s[i]]
            next_val = roman_values[s[i+1]] if i + 1 < n else 0
            
            # Check for preceeding roman numerals
            if current_val < next_val:
                val -= current_val
            else:
                val += current_val
        
        return val
