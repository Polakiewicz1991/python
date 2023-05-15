
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        head = ListNode()
        current = head
        i = 0

        while list1 and list2:
            print("list1 and list2:",list1 and list2 )
            print("list1.val: ",list1.val)
            print("list2.val: ",list2.val)
            print("list1.val < list2.val: ",list1.val < list2.val)

            if list1.val < list2.val:
                current.next = list1
                list1, current = list1.next, list1
            else:
                current.next = list2
                list2, current = list2.next, list2
            i += 1
            print(i)

        if list1 or list2:
            current.next = list1 if list1 else list2

Rozwiazanie = Solution()
lista1 = ListNode([1,2,3])
lista2 = ListNode([1,3,4])
# print("lista1.val: ",lista1.val)
# print("lista1.next: ",lista1.next)
# print("lista2.val: ",lista2.val)
print((Rozwiazanie.mergeTwoLists(lista1,lista2)))
def mergeTwoLists(list1: list, list2: list) -> list:
    list3: list = list1 + list2
    list3.sort()
    return list3
#
# print(mergeTwoLists([1,2,3],[1,3,4]))
# print(mergeTwoLists([1,2,3],[]))
# print(mergeTwoLists([],[0]))
# print(mergeTwoLists([1,2,3],[6,2,2,2,1]))

