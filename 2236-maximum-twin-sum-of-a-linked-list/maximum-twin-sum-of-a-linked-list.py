# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast,slow = head,head
        count = 0

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr,prev = slow, None

        while curr:
            curr.next,prev,curr = prev,curr,curr.next
        while prev:
            count = max(count,head.val + prev.val)
            prev = prev.next
            head = head.next
        return count

        