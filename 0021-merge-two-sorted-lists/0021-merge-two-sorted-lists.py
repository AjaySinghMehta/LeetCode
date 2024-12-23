# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merg(self, list1, list2):  # Added 'self' to the method
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.merg(list1.next, list2)  # Use 'self.merg' to call the instance method
            return list1
        else:
            list2.next = self.merg(list1, list2.next)  # Use 'self.merg' to call the instance method
            return list2

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.merg(list1, list2)