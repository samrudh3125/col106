from maze import *
from exception import *
from stack import *
class PacMan:
    def __init__(self, grid : Maze) -> None:
        self.navigator_maze = grid.grid_representation
        self.stack=Stack()
        self.seen=set()
    def find_path(self, start : tuple[int, int], end : tuple[int, int]) -> list[tuple[int, int]]:
        ans=[]
        cur_x=start[0]
        cur_y=start[1]
        n=len(self.navigator_maze)
        m=len(self.navigator_maze[0])
        while cur_x!=end[0] or cur_y!=end[1]:
            self.stack.push((cur_x,cur_y))
            self.seen.add((cur_x,cur_y))
            if cur_x!=0 and (cur_x-1,cur_y) not in self.seen and self.navigator_maze[cur_x-1][cur_y]==0:
                cur_x-=1
                continue
            elif cur_y!=m-1 and (cur_x,cur_y+1) not in self.seen and self.navigator_maze[cur_x][cur_y+1]==0:
                cur_y+=1
                continue
            elif cur_x!=n-1 and (cur_x+1,cur_y) not in self.seen and self.navigator_maze[cur_x+1][cur_y]==0:
                cur_x+=1
                continue
            elif cur_y!=0 and (cur_x,cur_y-1) not in self.seen and self.navigator_maze[cur_x][cur_y-1]==0:
                cur_y-=1
                continue
            elif cur_x==start[0] and cur_y==start[1]:
                raise PathNotFoundException
            else:
                self.stack.pop()
                last=self.stack.top()
                cur_x=last[0]
                cur_y=last[1]
                self.stack.pop()
        while not self.stack.empty():
            ans.append(self.stack.pop())
        ans.reverse()
        ans.append(end)
        print(ans)
        return ans
        
            
