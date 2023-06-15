# ╔════════════════════════════════════╗
# ║ Drzewo binarne val, left, right    ║
# ║                                    ║
# ║                                    ║
# ╚════════════════════════════════════╝

# Definition for singly-linked list.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"<ListNode val:{self.val} left:{self.left}, right:{self.right}>"

    def __str__(self):
        return f"<ListNode val:{self.val} left:{self.left}, right:{self.right}>"

def convert_list_to_linked_list(lst):
    if not lst:
        return None

    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10 ,11, 12]
    # 0->1,2    |
    # 1->3,4    | 2->5,6
    # 3->7,8    | 4->9,10 | 5-> 11,12 | 6->13,14
    # 7->15,16  | 8->17,18| 9->19,20  |10->21,22|11->23,24  |12->25,26|13->27,28  |14->29,30|
    # 15
    #+1         | +2     | +3     | +4
    head = TreeNode(lst[0])
    current = head
    i = 0
    print(len(lst))
    #list = [4,2,6,1,3]
    while i*2 + 1 <= len(lst):
        j = i
        while j < i*2 + 1:
            print("i", i, "j:", j, 2*j+1, 2*j+2, "next i :", i*2 + 1)

            if j % 2 == 0:
                try:
                    new_node = TreeNode(lst[2 * j + 1])
                    current.left = new_node
                except IndexError:
                    new_node = TreeNode(None)
            else:
                try:
                    new_node = TreeNode(lst[2 * j + 2])
                    current.left = new_node
                except IndexError:
                    new_node = TreeNode(None)

            current = new_node
            j += 1

        i = i*2 + 1

    return head

def create_tree(nums):
    if not nums:
        return None

    root = TreeNode(nums[0])
    queue = [root]
    i = 1

    while queue:
        #W tym miejscy root przypisany jest do node node = root + queue = [None]
        node = queue.pop(0)
        # print(i, "queue", queue)
        # print("node", node)

        if i < len(nums):
            if nums[i] is not None:
                node.left = TreeNode(nums[i])
                queue.append(node.left)
            i += 1

        if i < len(nums):
            if nums[i] is not None:
                node.right = TreeNode(nums[i])
                queue.append(node.right)
            i += 1

    return root
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = 0
        result = 0
        def dp(root: Optional[TreeNode],res) -> int:
            # print(root)
            res += root.val
            result = min()
            # print(res)
            if root.left != None:
                dp(root.left,res)
            # print("lh", res)
            if root.right != None:
                # res += root.val
                dp(root.right,res)
            print("rh",res)

            return res

        return dp(root,res)



Wynik = Solution()

# list = [4,2,6,1,3]
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10 ,11, 12]
head = create_tree(list)
# print(head)
Wynik1 = Wynik.getMinimumDifference(head)
print("Wynik1", Wynik1)

# list = [1,0,48,None,None,12,49]
# head = create_tree(list)
# print(head)
# Wynik1 = Wynik.getMinimumDifference(head)

