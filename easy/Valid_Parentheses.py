# Leet Code Problem #20
# Difficulty: Easy
# Problem URL: https://leetcode.com/problems/valid-parentheses/

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        # An inner closing parentheses can not be seperated by a preceeding closing parentheses
        # Therefore a stack is used to keep track of validity
        stack = []
        # Dictionary to define the only 3 set of pairs
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                # if there is no string
                if not stack:
                    return False
                popped = stack.pop()
                # If a closing is before any opening
                if pairs[char] != popped:
                    return False
        
        return not stack