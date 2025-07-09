from typing import Optional
# Leetcode problem #2:
# URL: https://leetcode.com/problems/climbing-stairs/
# Difficulty: Medium

# Time Complexity: O(n)
# Space Complexity: O(n)
# Theoretically can be space can be O(1) by addition in place if we don't care about l1 or l2 anymore after

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sums = ListNode()
        # Storing of the pointer of the original head
        head = sums
        carry = 0
        # If we haven't reached the end of the linked list
        while l1 or l2:
            # Case of addition of both digits within two linked list
            if l1 and l2:
                sum = l1.val + l2.val + carry
                carry = 0
                if sum >= 10:
                    sum -= 10
                    carry += 1
                sums.next = ListNode(sum)
                sums = sums.next
                l1 = l1.next
                l2 = l2.next
            # Case of l1 being larger than l2
            elif l1:
                sum = l1.val + carry
                carry = 0
                if sum >= 10:
                    sum -= 10
                    carry += 1
                sums.next = ListNode(sum)
                sums = sums.next
                l1 = l1.next
            # case of l2 being larger than l1
            else:
                sum = l2.val + carry
                carry = 0
                if sum >= 10:
                    sum -= 10
                    carry += 1
                sums.next = ListNode(sum)
                sums = sums.next
                l2 = l2.next

        # if we have a leftover carry after we reached the end, we need another digit
        if carry:
            sums.next = ListNode(1)

        # first head is pointing to a 0 val head, actual start is head.next
        return head.next