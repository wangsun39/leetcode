class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class PairNode:
    def __init__(self, idx, listNode):
        self.idx = idx
        self.listNode = listNode
class Solution:
    def get_h_n_k(self, d, n, k):
        #对于某个k, 表示最后弹出的是第k个右括号，那么前k-1对括号都在左边，后面n-k对括号都在第k对括号之中
        l = []
        for i in d[k-1]:
            for j in d[n-k]:
                str = i + '(' + j + ')'
                l.append(str)
        return l
    def get_h_n(self, d, n):
        # 获取h(n)的所有组合，依据h(0), h(1),...h(n-1)
        for i in range(1, n+1):
            d[n] = d[n] + self.get_h_n_k(d, n, i)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # h(n) = h(0)h(n-1) + h(1)h(n-2) + ... + h(n-1)h(0)
        d = {0: [''], 1: ['()']}
        for i in range(2, n+1):
            d[i] = []
            self.get_h_n(d, i)
        return d[n]

    def sortKListHead(self, lists):
        # 将k个list的首个node排序，放入一个list中
        sort_l = []
        k = len(lists)
        for i in range(k):
            if lists[i] is None:
                continue
            sort_l.append(PairNode(i, lists[i]))
        k = len(sort_l)
        for i in range(k):
            for j in range(i+1, k):
                if sort_l[i].listNode.val > sort_l[j].listNode.val:
                    sort_l[i], sort_l[j] = sort_l[j], sort_l[i]
        return sort_l

    def insert_List(self, sort_l, node):
        i, j = 0, len(sort_l) - 1
        if j < 0:
            sort_l.append(node)
        while i <= j:
            if node.listNode.val <= sort_l[i].listNode.val:
                sort_l.insert(i, node)
                return
            if node.listNode.val >= sort_l[j].listNode.val:
                sort_l.insert(j + 1, node)
                return
            mid = int((i + j) / 2)
            if sort_l[mid].listNode.val < node.listNode.val:
                i = max(mid, i+1)
            elif sort_l[mid].listNode.val > node.listNode.val:
                j = min(mid, j-1)
            else:
                sort_l.insert(mid, node)
                return

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        sort_l = self.sortKListHead(lists)
        if len(sort_l) == 0:
            return None
        head_node = ListNode(sort_l[0].listNode.val)
        cur_node = head_node
        while len(sort_l) >= 1:
            # 从sort_l中取出一个最小的sort_l[0].listNode，再把sort_l[0]列表的下一个用二分法插入sort_l中
            to_del_idx = sort_l[0].idx
            to_del_node = sort_l[0].listNode
            del sort_l[0]
            if to_del_node.next is not None:
                self.insert_List(sort_l, PairNode(to_del_idx, to_del_node.next))
            elif len(sort_l) == 0:
                break
            cur_node.next = ListNode(sort_l[0].listNode.val)
            cur_node = cur_node.next
        return head_node

    def transList2Dic(self, head):
        cur = head
        i = int(0)
        d = {}
        while cur is not None:
            d[i] = cur
            i += 1
            cur = cur.next
        return d
    def reverseKGroup(self, head: 'ListNode', k: 'int') -> 'ListNode':
        d = self.transList2Dic(head)
        node_num = len(d)
        loop_num = int(node_num/k)
        last_num = node_num % k
        for i in range(loop_num):
            if i < loop_num - 1:
                d[i*k].next = d[(i + 2) * k - 1]
                for j in range(1, k):
                    d[i*k+j].next = d[i*k+j-1]
            elif i == loop_num - 1:
                if last_num == 0:
                    d[i * k].next = None
                else:
                    d[i*k].next = d[(i + 1) * k]
                for j in range(1, k):
                    d[i*k+j].next = d[i*k+j-1]
            else:
                if last_num == 0:
                    d[i * k].next = None
                    for j in range(1, k):
                        d[i * k + j].next = d[i * k + j - 1]
        if loop_num == 0:
            return head
        return d[k-1]




l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l3 = ListNode(2)
l3.next = ListNode(6)

so = Solution()
'''a=so.mergeKLists([l1,l2,l3])
while a is not None:
    print(a.val)
    a = a.next
so.mergeKLists([None, None])'''
a=so.mergeKLists([l1])
b=so.reverseKGroup(l1, 1)
while b is not None:
    print(b.val)
    b = b.next
