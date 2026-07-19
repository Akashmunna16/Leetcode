# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        
        while curr and curr.next:
            # If the next element is already in increasing order, just move forward
            if curr.val <= curr.next.val:
                curr = curr.next
            else:
                # Find where curr.next fits in the sorted prefix list
                prev = dummy
                while prev.next.val < curr.next.val:
                    prev = prev.next
                    
                # Pluck out the out-of-order node and insert it after prev
                target = curr.next
                curr.next = target.next
                target.next = prev.next
                prev.next = target
                
        return dummy.next
        