from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre


#a = Solution()
l1 = ListNode([1, 2, 3, 4])
print(l1.val)
pre = Solution().reverseList(l1)
print(pre.val)
