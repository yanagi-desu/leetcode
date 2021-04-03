
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        viewed = []
        i=0
        while head:
            if head in viewed:
                return head
            else:
                i+=1
                viewed.append(head)
                head = head.next
        return None