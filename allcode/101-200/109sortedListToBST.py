from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def helper(nums):
            if 0 == len(nums):
                return None
            N = len(nums)
            mid = N // 2
            node = TreeNode(nums[mid].val)
            node.left = helper(nums[:mid])
            node.right = helper(nums[mid+1:])
            return node
        c = head
        array = []
        while c is not None:
            array.append(c)
            c = c.next
        res = helper(array)
        return res

    def sortedListToBST1(self, head: ListNode) -> TreeNode:
        def countOfList(head):
            count = 0
            while head is not None:
                count += 1
                head = head.next
            return count
        def generateTree(num): # 构造一个平衡二叉树结构
            if num <= 0:
                return None
            node = TreeNode(0)
            right_num = (num - 1) // 2
            left_num = num - 1 - right_num
            node.left = generateTree(left_num)
            node.right = generateTree(right_num)
            return node
        def fillNumOfTree(root, head):
            stack =[]
            cur = root
            while True:
                if cur is not None:
                    stack.append(cur)
                    cur = cur.left
                else:
                    if 0 == len(stack):
                        break
                    cur = stack.pop()
                    cur.val = head.val
                    head = head.next
                    cur = cur.right
            return

        N = countOfList(head)
        root = generateTree(N)
        fillNumOfTree(root, head)
        return root

node = ListNode(-10)
node.next = ListNode(-3)
node.next.next = ListNode(0)
node.next.next.next = ListNode(5)
node.next.next.next.next = ListNode(9)
so = Solution()
print(so.sortedListToBST(node))
print(so.sortedListToBST1(node))
