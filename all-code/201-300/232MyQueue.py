class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.m_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        tmp = []
        while len(self.m_stack) > 1:
            t = self.m_stack.pop()
            tmp.append(t)
        res = self.m_stack.pop()
        while len(tmp) > 0:
            self.m_stack.append(tmp.pop())
        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        tmp = []
        while len(self.m_stack) > 0:
            t = self.m_stack.pop()
            tmp.append(t)
        res = t
        while len(tmp) > 0:
            self.m_stack.append(tmp.pop())
        return res


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.m_stack) == 0


# Your MyQueue object will be instantiated and called as such:
queue = MyQueue()
queue.push(1)
queue.push(2)
queue.peek()
queue.pop()
queue.empty()


