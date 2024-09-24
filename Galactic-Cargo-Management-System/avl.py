from node import Node

def comp_1(key_1, key_2):
    if key_1.capacity < key_2.capacity:
        return 1
    elif key_1.capacity>key_2.capacity:
        return 0
    else:
        return key_1.id<key_2.id

def height(node):
    if not node:
        return 0
    return node.height
class AVLTree:
    def __init__(self, compare_function=comp_1):
        self.root:Node = None
        self.size = 0
        self.comparator = compare_function

    def compactFit(self,node,size):
        if not node:
            return None
        curr=node
        while curr:
            if curr.key.capacity==size:
                break
            elif curr.key.capacity<size:
                curr=curr.right
            else:
                pre=self.compactFit(curr.left,size)
                if not pre or pre.key.capacity==curr.key.capacity:
                    break
                curr=curr.left
        return curr

    def largestFit(self,node,size):
        if not node:
            return None
        curr=node
        while curr.right:
            if curr.right.key.capacity==curr.key.capacity:
                succ=self.largestFit(curr.right,size)
                if not succ or succ.key.capacity==curr.key.capacity:
                    break
            curr=curr.right
        if curr.key.capacity<size:
            return None
        return curr
    
    def predecessor(self,node):
        if not node.left:
            return node
        curr=node.left
        while curr.right:
            curr=curr.right
        return curr

    def successor(self,node):
        if not node.right:
            return node
        curr=node.right
        while curr.left:
            curr=curr.left
        return curr

    def left_rotate(self,node):
        y=node.right
        node.right=y.left
        y.left=node
        node.height=1+max(height(node.left),height(node.right))
        y.height=1+max(height(y.left),height(y.right))
        return y

    def right_rotate(self,node):
        y=node.left
        node.left=y.right
        y.right=node
        node.height=1+max(height(node.left),height(node.right))
        y.height=1+max(height(y.left),height(y.right))
        return y

    def inorder(self,node,ans):
        if not node:
            return
        self.inorder(node.left,ans)
        ans.append(node.key.id)
        self.inorder(node.right,ans)
        return

    def fix_height(self,node):
        balance=height(node.left)-height(node.right)
        if balance<-1:
            x=node.right
            if height(x.left)>height(x.right):
                node.right=self.right_rotate(x)
            node=self.left_rotate(node)
        elif balance>1:
            x=node.left
            if height(x.left)<height(x.right):
                node.left=self.left_rotate(x)
            node=self.right_rotate(node)
        return node

    def search(self,id):
        if not self.root:
            return None
        curr=self.root
        while curr:
            if curr.key.id==id:
                return curr.key
            elif curr.key.id>id:
                curr=curr.left
            else:
                curr=curr.right
        return None

    def insert(self,key):
        if not self.root:
            self.root=Node(key)
        else:
            self.root=self._insert(self.root,key)

    def _insert(self,node,key):
        if not node:
            return Node(key)
        if self.comparator(node.key,key):
            node.right=self._insert(node.right,key)
        else:
            node.left=self._insert(node.left,key)
        
        node.height=1+max(height(node.left),height(node.right))
        node=self.fix_height(node)
        return node

    def delete(self, key):
        if not self.root:
            raise Exception()
        else:
            self.root=self._delete(self.root,key)
            return

    def _delete(self,node,key):
        if not node:
            return
        if node.key.id==key.id:
            if node.right and node.left:
                pre=node.left
                while pre.right:
                    pre=pre.right
                node.key=pre.key
                node.left=self._delete(node.left,pre.key)
            elif node.left:
                node=node.left
            else:
                node=node.right
            return node
        elif self.comparator(node.key,key):
            node.right=self._delete(node.right,key)  
        else:
            node.left=self._delete(node.left,key)

        node.height=1+max(height(node.right),height(node.left))
        node=self.fix_height(node)
        return node