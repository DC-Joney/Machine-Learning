class Node:
    '''

    '''
    def __init__(self,data,pnext=None):
        self.data = data
        self._next = pnext
    def __repr__(self):
        return self.data
class ChainTable(object):
    def __init__(self):
        self.head=None
        self.lenth = 0
    #判断链表是否为空
    def isEmpty(self):
        return (self.lenth == 0)
    #增加元素
    def append(self,dataOrNode):
        item = None
        if isinstance(dataOrNode,Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)
        if not self.head:
            self.head = item
            self.lenth += 1
        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.lenth += 1
    #删除元素
    def delete(self,index):
        if self.isEmpty():
            print("this chain table is empty")
            return
        if index < 0 or index >= self.lenth:
            print("error : out of index")
            return
        if index == 0:
            self.head = self.head._next
            self.lenth -= 1
            return
        j = 0
        node = self.head
        prev =  self.head
        #遍历得到上一个节点 和当前节点 和当前节点的索引值
        while node._next and j < index:
            prev = node
            node = node._next
            j+=1

        #当前界面的索引值 =  index 将上一个节点指向链表的下一个元素直接指向当前节点指向的下一个元素
        if j == index:
            prev._next = node._next
            self.lenth -= 1
    def insert(self,index,dataOrNode):
        if self.isEmpty():
            print("this chain table is empty")
            return
        if index < 0 or index >= self.lenth:
            print("error : out of index")
            return
        item =  None
        if isinstance(dataOrNode,Node):
            item = dataOrNode
        else:
            item =  Node(dataOrNode)
        if index == 0:
            item._next = self.head
            self.head = item
            self.lenth += 1
            return
        j = 0
        node =  self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j+=1
        if j == index:
            item._next = node
            prev._next  = item
            self.lenth += 1



    def update(self,index,data):
        if self.isEmpty() or index < 0 or index > self.lenth:
            print("error : out of index")
            return
        j = 0
        node = self.head
        while  node._next and j < index:
            node = node._next
            j += 1
        if  j == index:
            node.data = data

    def getItem(self,index):
        if self.isEmpty() or index < 0 or index > self.lenth:
            print("error : out of index")
            return
        j = 0
        node = self.head
        while node._next  and j < index :
            node = node._next
            j += 1
        return node.data

    def getIndex(self,data):
        j = 0
        if self.isEmpty():
            print ("this chain table is empty")
            return
        node = self.head
        while node:
            if node.data == data:
                return  j
            node = node._next
            j += 1
            if j == self.lenth:
                print("%s is not found",str(data))
            return
    def clear(self):
        self.head = None
        self.lenth = 0


    def __repr__(self):
        if self.isEmpty():
            return "empty chain table"
        node = self.head
        nlist = ''
        while node:
            nlist += str(node.data) + ''
            node = node._next
        return nlist
    def __getitem__(self, ind):
        if self.isEmpty() or ind < 0 or ind >= self.lenth:
            print("error:out of index")
            return
        return self.getItem(ind)
    def __setitem__(self, ind, value):
        if self.isEmpty() or ind<0 or ind>= self.lenth:
            print("error: out of index")
            return
        return self.update(ind,value)
    def __len__(self):
        return self.lenth

if __name__ == "__main__":
    table = ChainTable();
    table.append(1)
    table.append(2)
    table.delete(0)
    print(table.__len__())
    print(table.getItem(0))