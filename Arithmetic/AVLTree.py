#coding=utf-8
'''
    AVL树的python实现
    AVL树是带有平衡条件的二叉查找树，一般要求每个节点的左子树和右子树的高度最多差1(空树的高度定义为-1)。
    在高度为h的AVL树中，最少的节点数S(h)由S(h)=S(h-1)+S(h-2)+1得出，其中S(0)=1，S(1)=2。
'''

import  os
class Node(object):
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0

class AVLTree(object):
    def __init__(self):
        self.root=None
    def find(self,key):
        if self.root is None:
            return None
        else:
            return self._find(key,self.root)
    def _find(self,key,node):
        if node is None:
            return None
        elif key < node.key:
            return self._find(key,self.left)
        elif key > node.key:
            return  self._find(key,self.right)
        else:
            return node
    def findMin(self):
        if self.root is None:
            return None
        else:
            return  self._findMin(self.root)
    def _findMin(self,node):
        if node.left:
            return self._findMin(self.left)
        else:
            return node
    def findMax(self):
        if self.root is None:
            return  None
        else:
            return  self._findMax(self.root)
    def _findMax(self,node):
        if self.root is None:
            return node
        else:
            return self._findMax(self.root)
    def height(self,node):
        if node is None:
            return -1
        else:
            return node.height
    # RR 旋转平衡 将非平衡子树
    def singleLeftRotate(self,node):
        k1 = node.left
        node.left = k1.right
        k1.right=node
        node.height = max(self.height(node.right),self.height(node.left)+1)
        k1.height = max(self.height(k1.left),node.height)+1
        return k1

    #LL 向左旋转保持树平衡
    def singleRightRotate(self,node):
        k1 = node.right
        node.right = k1.left
        k1.left = node
        node.height = max(self.height(node.right),self.height(node.left)+1)
        k1.height = max(self.height(k1.right),node.height)+1
        return k1
    #LR 双旋 先左旋 然后右旋转   先对右子树进行旋转 然后对整棵树进行旋转
    def doubleRightRoatate(self,node):
        node.right = self.singleLeftRotate(node.right)
        return  self.singleRightRotate(node)

    #RL双旋 先右旋然后在左旋 先对 左子树进行旋转 然后对整棵树进行宣传
    def doubleLeftRatate(self,node):
        node.left = self.singleRightRotate(node.left)
        return self.singleLeftRotate(node)
    #插入
    def add(self,key):
        if not self.root:
            self.root = Node(key)
        else:
            self.root = self._put(key,self.root)
    def _put(self,key,node):
        if node is None:
            node = Node(key)
        elif key < node.key:
            node.left = self._put(key,node.left)
            if(self.height(node.left)-self.height(node.right))==2:
                if key < node.left.key:
                    node = self.singleLeftRotate(node)
                else:
                    node =  self.doubleLeftRatate(node)
        elif key > node.key:
            node.right = self._put(key,node.right)
            if (self.height(node.right)-self.height(node.left)) == 2:
                if key < node.right.key:
                    node = self.doubleRightRoatate(node)
                else:
                    node = self.singleRightRotate(node)
        node.height = max(self.height(node.right),self.height(node.left))+1
        return  node

    def delete(self,key):
        self.root = self.remove(key,self.root)
    def remove(self,key,node):
        if node is None:
            raise KeyError("key不能为空")
        elif key < node.key:
            node.left =  self.remove(key,node.left)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if self.height(node.right.right) >= self.height(node.right.left):
                    node = self.singleRightRotate(node)
                else:
                    node = self.doubleRightRotate(node)
            node.height = max(self.height(node.left))

        elif key > node.key:
            node.right = self.remove(key,node.right)
            if(self.height(node.left)-self.height(node.right))==2:
                if self.height(node.left.left)>= self.height(node.left.right):
                    node = self.singleLeftRotate(node)
                else:
                    node = self.doubleLeftRatate(node)
            node.height =  max(self.height(node.left),self.height(node.right))+1

        elif node.left and node.right:
            if node.left.hegiht <=  node.right.height:
                minNode = self._findMin(node.right)
                node.key = minNode.key
                node.right = self.remove(node.key,node.right)
            else:
                maxNode = self._findMax(node.left)
                node.key = maxNode.key
                node.left = self.remove(node.key,node.left)
            node.height = max(self.height(node.left),self.height(node.right))+1
        else:
            if node.right:
                node = node.right
            else:
                node = node.left
        return node

if __name__ == '__main__':
     avlTree = AVLTree();
     number_list = (10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
     for i  in number_list:
         avlTree.add(i)
     a = set("23")
     # b = set("2333")
     # c = a | b
     # print(c)
     # print(8>>4)
     # A = 001010
     # B = 101100
     # A ^ B = 100110