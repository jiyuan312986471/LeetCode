# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def to_val(l):
            return l.val + 10 * to_val(l.next) if l else 0

        def to_listnode(v):
            l = ListNode(v % 10)
            next_l = int(v / 10)
            l.next = to_listnode(next_l) if next_l else None
            return l

        return to_listnode(to_val(l1) + to_val(l2))
