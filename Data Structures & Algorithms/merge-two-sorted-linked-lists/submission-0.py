# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        ans = head
        while(list1 is not None and list2 is not None):
            v: int 
            if list1.val <= list2.val:
                v = list1.val
                list1 = list1.next
            else:
                v = list2.val
                list2 = list2.next
            ans.next = ListNode(v)
            ans = ans.next
        rest = list1 if list1 else list2
        while rest is not None:
            ans.next = ListNode(rest.val)
            ans = ans.next
            rest = rest.next
        return head.next 