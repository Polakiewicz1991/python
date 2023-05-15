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
    def swapNodesInternet(self, head: ListNode, k: int) -> ListNode:

        left_node = head
        print("left_node: ", left_node)
        print("head: ", head)
        print("\n\n\n")
        for i in range(1, k):
            left_node = left_node.next
            print("left_node: ", left_node)

        print("\n\n\n")
        right_node = head
        current = left_node
        while current.next:
            current = current.next
            right_node = right_node.next
            print("right_node: ", right_node)

        left_node.val, right_node.val = right_node.val, left_node.val

        return head

    # def swapNodes(self, head: ListNode, k: int) -> [ListNode]:
    #
    #     print("head: ",head)
    #     head1 = head
    #     head2 = head
    #
    #     i = 1
    #     for i in range(1,k):
    #         head1 = head1.next
    #         print("i: ",i," head1: ",head1)
    #
    #     # head1.valk-1],head1.val[listLen - k] = head1.val[listLen - k],head1.valk-1]
    #
    #     for i in range(1,k):
    #         head1 = head1.next
    #         print("i: ",i," head1: ",head1)
    #     return 0

Wynik = Solution()
# head = [1,2,3,4,5]
# k = 2
# Wynik1 = Wynik.swapNodes(head,k)


list1 = [7, 9, 6, 6, 7, 8, 3, 0, 9, 5]
linked_list = convert_list_to_linked_list(list1)

# Przykład użycia klasy ListNode
# current = linked_list
# while current:
#     print("val: ", current.val," next: ",current.next)
#     current = current.next

k = 5
Wynik2 = Wynik.swapNodesInternet(linked_list,k)

# print("Wynik1: ",Wynik1)
print("Wynik2: ",Wynik2)