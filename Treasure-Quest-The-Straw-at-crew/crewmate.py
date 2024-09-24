'''
    Python file to implement the class CrewMate
'''
from heap import Heap

def treasure_comparator(treasure_1,treasure_2):
    if(treasure_1.size+treasure_1.arrival_time<treasure_2.size+treasure_2.arrival_time):
        return True
    elif treasure_1.size+treasure_1.arrival_time>treasure_2.size+treasure_2.arrival_time:
        return False
    else:
        if treasure_1.id<treasure_2.id:
            return True
        else:
            return False


class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        self.load=0
        self.treasures=Heap(treasure_comparator,[])
        
        # Write your code here
        pass
    
    def add_treasure(self, treasure):
        self.treasures.insert(treasure)
        self.load+=treasure.size

    