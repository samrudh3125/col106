from avl import AVLTree
from exceptions import NoBinFoundException
def id_compare(key_1,key_2):
    if key_1.id<key_2.id:
        return True
    else:
        return False

class Bin:
    def __init__(self, bin_id, capacity):
        self.id=bin_id
        self.capacity=capacity
        self.objects=AVLTree(compare_function=id_compare)

    def add_object(self, object):
        if object.size>self.capacity:
            raise NoBinFoundException()
        self.capacity-=object.size
        self.objects.insert(object)
        return True

    def remove_object(self, object_id):
        object=self.objects.search(object_id)
        if not object:
            raise Exception("Object not found")
        self.capacity+=object.size
        self.objects.delete(object)
        return True
            
