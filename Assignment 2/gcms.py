from bin import Bin
from avl import AVLTree
from node import Node
from object import Object, Color
from exceptions import NoBinFoundException

def id_compare(key_1,key_2):
    if key_1.id<key_2.id:
        return True
    else:
        return False

class GCMS:
    def __init__(self):
        self.bin_tree=AVLTree()
        self.object_tree=AVLTree(compare_function=id_compare)
        self.bin_id_tree=AVLTree(compare_function=id_compare)

    def add_bin(self, bin_id, capacity):
        bin=Bin(bin_id,capacity)
        self.bin_tree.insert(bin)
        self.bin_id_tree.insert(bin)
    
    def add_object(self, object_id, size, color):
        object=Object(object_id,size,color)
        if color==Color.BLUE or color==Color.YELLOW:
            curr=self.bin_tree.compactFit(self.bin_tree.root,size)
            if not curr:
                raise NoBinFoundException()
            if color==Color.BLUE:
                flag=True
                while flag:
                    while curr.left:
                        if curr.left.key.capacity!=curr.key.capacity:
                            break
                        curr=curr.left
                    temp=curr.left
                    while temp:
                        if temp.key.capacity==curr.key.capacity:
                            break
                        temp=temp.right
                    if not temp:
                        flag=False
                    else:
                        curr=temp  
            else:
                flag=True
                while flag:
                    while curr.right:
                        if curr.right.key.capacity!=curr.key.capacity:
                            break
                        curr=curr.right
                    temp=curr.right
                    while temp:
                        if temp.key.capacity==curr.key.capacity:
                            break
                        temp=temp.left
                    if not temp:
                        flag=False
                    else:
                        curr=temp
        elif color==Color.RED or color==Color.GREEN:
            curr=self.bin_tree.largestFit(self.bin_tree.root,size)
            if not curr:
                raise NoBinFoundException
            if color==Color.RED:
                flag=True
                while flag:
                    while curr.left:
                        if curr.left.key.capacity!=curr.key.capacity:
                            break
                        curr=curr.left
                    temp=curr.left
                    while temp:
                        if temp.key.capacity==curr.key.capacity:
                            break
                        temp=temp.right
                    if not temp:
                        flag=False
                    else:
                        curr=temp
            else:
                flag=True
                while flag:
                    while curr.right:
                        if curr.right.key.capacity!=curr.key.capacity:
                            break
                        curr=curr.right
                    temp=curr.right
                    while temp:
                        if temp.key.capacity==curr.key.capacity:
                            break
                        temp=temp.left
                    if not temp:
                        flag=False
                    else:
                        curr=temp
        else:
            raise Exception()
        bin=curr.key
        self.bin_tree.delete(bin)
        bin.add_object(object)
        object.bin_id=bin.id
        self.bin_tree.insert(bin)
        self.object_tree.insert(object)
        return

    def delete_object(self, object_id):
        temp=self.object_tree.search(object_id)
        if not temp:
            return None
        self.object_tree.delete(temp)
        bin=self.bin_id_tree.search(temp.bin_id)
        if not bin:
            raise NoBinFoundException()
        self.bin_tree.delete(bin)
        bin.remove_object(object_id)
        self.bin_tree.insert(bin)

    def bin_info(self, bin_id):
        temp=self.bin_id_tree.search(bin_id)
        if not temp:
            raise NoBinFoundException()
        else:
            objects=[]
            temp.objects.inorder(temp.objects.root,objects)
            return (temp.capacity,objects)

    def object_info(self, object_id):
        temp=self.object_tree.search(object_id)
        if not temp:
            return None
        return temp.bin_id
    
    