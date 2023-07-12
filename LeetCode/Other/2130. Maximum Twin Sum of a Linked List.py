# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"<ListNode val:{self.val} next:{self.next}>"

    def __str__(self):
        return f"ListNode: val:{self.val}, next:{self.next}"

def convert_list_to_linked_list(lst):
    if not lst:
        return None

    head = ListNode(lst[0])
    current = head

    for i in range(1, len(lst)):
        new_node = ListNode(lst[i])
        current.next = new_node
        current = new_node

    return head

class Solution:
    def pairSumInternetFast(self, head: ListNode) -> int:

        slow, fast = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        res = 0
        while slow:
            res = max(res, slow.val + prev.val)
            slow = slow.next
            prev = prev.next

        return res

    def pairSum(self, head: ListNode) -> int:

        auxListNode = head
        auxList = []

        while auxListNode:
            auxList.append(auxListNode.val)
            auxListNode = auxListNode.next

        print(auxList)

        halfLen = int((len(auxList))/2)
        print(halfLen)

        res = 0
        for i in range(halfLen):
            j = len(auxList) - 1 - i
            print("i: ", i , " j: ",j)
            res = int(max(res, auxList[i] + auxList[j]))
            print(res)

        return res


Wynik = Solution()
list1 = [5,4,2,1]
head = convert_list_to_linked_list(list1)
print(head)
Wynik1 = Wynik.pairSum(head)

print("Wynik1: ", Wynik1)