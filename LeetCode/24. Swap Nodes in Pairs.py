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
    def swapPairs(self, head: ListNode) -> ListNode:

        headAux = head
        try:
            nodeLenght = 1 if (headAux.val != 0) else 0
        except AttributeError:
            return head

        while True:
            print("nodeLenght: ", nodeLenght)
            print("headAux: ",headAux)

            if headAux.next != None:
                headAux = headAux.next
                nodeLenght += 1
            else:
                break

        print("\n\n\n")
        head1st = head
        head2nd = head
        for x in range(nodeLenght) :
            print("\nhead1st:",head1st)
            print("head2nd:",head2nd)
            if x % 2 == 0:
                head2nd = head2nd.next
                tempVal = head1st.val
                try:
                    head1st.val = head2nd.val
                except AttributeError:
                    pass
            else:
                head1st.val = tempVal
                head2nd = head2nd.next
            print("\nhead1st after:", head1st)
            print("head2nd after:", head2nd)

            head1st = head1st.next
            # head2nd = head2nd.next

        return head

    def swapPairsInternet(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next): return head
        node = head.next
        print("node: ",node)
        head.next = self.swapPairsInternet(head.next.next)
        print("head.next: ",head.next)
        node.next = head
        print("node: ",node)
        return node

Wynik = Solution()

list = [1,2,3,4]
head = convert_list_to_linked_list(list)
Wynik1 = Wynik.swapPairsInternet(head)

# list = []
# head = convert_list_to_linked_list(list)
# Wynik2 = Wynik.swapPairs(head)
#
# list = [1]
# head = convert_list_to_linked_list(list)
# Wynik3 = Wynik.swapPairs(head)

print("Wynik1:" ,Wynik1)
# print("Wynik2:" ,Wynik2)
# print("Wynik3:" ,Wynik3)