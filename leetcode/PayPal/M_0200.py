class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        no_of_islands = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def set_zeros_islands(grid, r, c):
            if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]=="1":
                grid[r][c]=0
                for (r_inc, c_inc) in directions:
                    set_zeros_islands(grid, r+r_inc, c+c_inc)
                    
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    no_of_islands += 1
                    set_zeros_islands(grid, r, c)
        return no_of_islands