from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def recoverTree(self, root: TreeNode) -> List[int]:
        stack =[]
        exchange1, exchange2 = None, None
        cur = root
        find_exchange1 = False
        while True:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                if 0 == len(stack):
                    break
                cur = stack.pop()
                # res.append(cur.val)
                if not find_exchange1:
                    if exchange2 is not None and cur.val < exchange2.val:
                        find_exchange1 = True
                    exchange1, exchange2 = exchange2, cur
                else:
                    if cur.val < exchange1.val:
                        exchange2 = cur
                    else:
                        break
                cur = cur.right
        exchange1.val, exchange2.val = exchange2.val, exchange1.val
        return root


root = TreeNode(1)
root.left = TreeNode(3)
root.left.right = TreeNode(2)


so = Solution()

print(so.recoverTree(root))
