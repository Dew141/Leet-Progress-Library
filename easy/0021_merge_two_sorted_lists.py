# Problem ID: 21
# Title: Merge two sorted lists
# URL: https://leetcode.com/problems/merge-two-sorted-lists/description/
# Difficulty: Easy

# Time Complexity: O(n + m) n is the number of nodes in list1, m is the number of nodes in list2
# Space Complexity: O(n + m)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # End recurrsion condition if either of two lists have reached the end
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        # We want to see the next node if the nodes are smaller
        # That way we are left with the largest values in the back
        # Attach larger values to the smaller values in that list
        if list1.val >= list2.val:
            Node2 = list2.next
            list2.next = self.mergeTwoLists(list1, Node2)
            return list2
        else:
            Node1 = list1.next
            list1.next = self.mergeTwoLists(Node1, list2)
            return list1
