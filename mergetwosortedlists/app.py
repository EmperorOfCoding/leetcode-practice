from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        d = ListNode()
        cur = d

        while list1 and list2:

            if list1.val < list2.val:
                cur.next = list1


      



#solucao = Solution()
#resultado = solucao.mergeTwoLists()
#print(resultado)