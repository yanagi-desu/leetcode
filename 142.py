
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        onestep = head
        twostep = head
        hasCycle = False
        while onestep and twostep:
            onestep = onestep.next
            if not twostep.next:
                return None
            twostep = twostep.next.next
            if twostep == onestep: 
                hasCycle = True
                break 
        if hasCycle:
            onestep = head
            while onestep!=twostep:
                onestep = onestep.next
                twostep = twostep.next
            return onestep
        return None

head = ListNode(3)
i = [2,0,-4]
cur = head
while i:
    cur.next = ListNode(i.pop(0))
    cur = cur.next

solve = Solution()
print(solve.detectCycle(head))