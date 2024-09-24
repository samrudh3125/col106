class Stack:
    def __init__(self) -> None:
        self.list=[]
    def push(self,x:tuple[int,int]) -> None:
        self.list.append(x)
    def pop(self) -> tuple[int,int]:
        return self.list.pop()
    def top(self) -> tuple[int,int]:
        if len(self.list)==0:
            return -1
        return self.list[-1]
    def empty(self) -> bool:
        return len(self.list)==0