# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        # Step 1: Split the list into two halves using fast/slow pointers
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        # Break the link to isolate the two sublists
        prev.next = None
        
        # Step 2: Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(slow)
        
        # Step 3: Merge the two sorted lists together
        return self.merge(left, right)
        
    def merge(self, list1, list2):
        dummy = ListNode(0)
        curr = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        # Append remaining elements if one list finishes early
        curr.next = list1 if list1 else list2
        return dummy.next
        