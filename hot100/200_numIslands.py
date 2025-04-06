class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res+=1
                    self.infect(grid,i,j)
        
        return res



    def infect(self,grid:list[list[str]],x:int,y:int):
        m = len(grid)
        n = len(grid[0])

        if x<0 or x>=m:
            return
        if y<0 or y>=n:
            return
        
        if grid[x][y]=="1":
            grid[x][y]="2"
        else:
            return 
        self.infect(grid,x+1,y)
        self.infect(grid,x-1,y)
        self.infect(grid,x,y-1)
        self.infect(grid,x,y+1)
    
if __name__ == "__main__":
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    s = Solution()
    print(s.numIslands(grid))  # Output: 1




