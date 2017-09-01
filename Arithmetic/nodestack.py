###栈
class Stack(object):
    def __init__(self):
        self._top = 0
        self._stack =[]
    def put(self,data):
        self._stack.insert(self._top,data)
        self._top += 1
    def pop(self):
        if self.isEmpty():
            raise ValueError('stack 为空')
        self._top -= 1
        data = self._stack[self._top]
        return data
    def isEmpty(self):
        if self._top  == 0:
            return  True
        else:
            return False
    def __str__(self):
        return "Stack(%s)".format(self._stack)
    def __len__(self):
        return self._top
# stack = Stack()
# stack.put(1)
# stack.put(2)
# stack.put(3)
# stack.put(4)
# stack.put(5)
# stack.put(6)
# stack.put(7)
# print(stack.__len__(),stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.__len__())


###队列
class Queue(object):
    def __init__(self,max_size=float('inf')):
        self._max_size = max_size
        self._top = 0
        self._tail = 0
        self._queue = []
    def put(self,value):
        if self.isFull():
            raise ValueError('the queue is full')
        self._queue.insert(self._tail,value)
        self._tail+=1
    def pop(self):
        if self.isEmpty():
            raise ValueError('the queue is empty')
        data = self._queue[self._top]
        self._top += 1
        return data
    def isEmpty(self):
        if self._top == self._tail:
            return True
        else:
            return False
    def isFull(self):
        if self._tail == self._max_size:
            return  True
        else:
            return False
    def __len__(self):
        return self._tail - self._top
    def  getQueue(self):
        return self._queue
# queue = Queue()
# queue.put(1)
# queue.put(2)
# queue.put(2)
# queue.put(2)
# queue.put(2)
# queue.put(2)
# queue.pop()
# queue.pop()
# queue.pop()
# queue.pop()
# queue.pop()
# queue.pop()
# print(queue.__len__())
# queue.pop()

