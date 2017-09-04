
#condig=utf-8

###二叉树
#树节点
class Node(object):
    def __init__(self,elem=-1, lchild =None,rchild = None):
        #节点的值
        self.elem = elem
        #左节点
        self.lchild = lchild
        #右节点
        self.rchild = rchild
#树
class Tree(object):
    def __init__(self):
        self.root = Node()
        self.myQueue = []
    def add(self,elem):
        node = Node(elem)
        if self.root.elem == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0] #为此节点的左右子节点赋值
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                print(list(f.elem for f in self.myQueue))
                treeNode.rchild=node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃。

    ###先序遍历
    def front_digui(self,root):
        if root == None:
            return
        print(root.elem)
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)


    ###递归中序遍历
    def middle_digui(self,root):
        if root == None:
            return
        self.middle_digui(root.lchild)
        print(root.elem)
        self.middle_digui(root.rchild)

    ###递归后序遍历
    def lafter_digui(self,root):
        if root == None:
            return
        self.middle_digui(root.lchild)
        self.middle_digui(root.rchild)
        print(root.elem)
    ###队列层次遍历
    def level_queue(self,root):
        if root == None:
            return
        myQueue=[]
        node = root
        myQueue.append(node)
        while myQueue:
            node=myQueue.pop(0)
            print(node.elem)
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)
    ###堆栈先序遍历

    def front_stack(self,root):
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:
                print(node.elem)
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()
            node =  node.rchild

        ###堆栈中序遍历
        def middle_stack(self, root):
            if root == None:
                return
            myStack = []
            node = root
            while node or myStack:
                while node:   #从根节点开始，一直找它的左子树
                    print(node.elem)
                    myStack.append(node)
                    node = node.lchild
                node = myStack.pop()  #while结束表示当前节点node为空，即前一个节点没有左子树了
                node = node.rchild   #开始查看它的右子树

        ##堆栈后序遍历
        def later_stack(self,root):
            if root == None:
                return
            myStack1 = []
            myStack2 = []
            node = root
            myStack1.append(node)
            while myStack1:  #这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
                node = myStack1.pop()
                if node.lchild:
                    myStack1.append(node.lchild)
                if node.rchild:
                    myStack1.append(node.rchild)
                myStack2.append(node)
            while myStack2:    #将myStack2中的元素出栈，即为后序遍历次序
                print(myStack2.pop().elem)

if __name__ == '__main__':
    pass
    # """主函数"""
    # elems = range(10)           #生成十个数据作为树节点
    # tree = Tree()          #新建一个树对象
    # for elem in elems:
    #     tree.add(elem)           #逐个添加树的节点
    #
    #
    # print ('\n\n递归实现先序遍历:')
    # # tree.front_digui(tree.root)
    # # tree.level_queue(tree.root)
    # # print(tree.root.elem)
    # # print(list(f.elem for f in tree.myQueue))
    # tree.middle_digui(tree.root)
