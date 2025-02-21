# 设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val和next。val是当前节点的值，next是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性prev以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。
#
# 在链表类中实现这些功能：
#
# get(index)：获取链表中第index个节点的值。如果索引无效，则返回-1。
# addAtHead(val)：在链表的第一个元素之前添加一个值为val的节点。插入后，新节点将成为链表的第一个节点。
# addAtTail(val)：将值为val 的节点追加到链表的最后一个元素。
# addAtIndex(index,val)：在链表中的第index个节点之前添加值为val 的节点。如果index等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
# deleteAtIndex(index)：如果索引index 有效，则删除链表中的第index 个节点。
#
#
# 示例：
#
# MyLinkedList linkedList = new MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
# linkedList.get(1);            //返回2
# linkedList.deleteAtIndex(1);  //现在链表是1-> 3
# linkedList.get(1);            //返回3
#
#
# 提示：
#
# 所有val值都在[1, 1000]之内。
# 操作次数将在[1, 1000]之内。
# 请不要使用内置的 LinkedList 库。




from leetcode.allcode.competition.mypackage import *
class MyLinkedList:

    def __init__(self):
        self.ll = []


    def get(self, index: int) -> int:
        if 0 <= index < len(self.ll):
            return -1
        print(self.ll)
        return self.ll[index]


    def addAtHead(self, val: int) -> None:
        self.ll.insert(0, val)


    def addAtTail(self, val: int) -> None:
        self.ll.append(val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index > len(self.ll): return
        if index == len(self.ll):
            self.ll.append(val)
            return
        self.ll.insert(index, val)
        return


    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < len(self.ll):
            del(self.ll[index])



# so = MyLinkedList(4, [2,1])
# print(so.pick())
# print(so.pick())
# print(so.pick())
# print(so.pick())



