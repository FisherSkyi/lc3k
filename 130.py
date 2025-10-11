from typing import List

class Solution:
    def solve(self, board: List[List[str]]):
        """
        Do not return anything, modify board in-place instead.
        """
        visited = [[0 for c in range(len(board[0]))] for r in range(len(board))]
        def isX(letter):
            return True if letter == 'X' else False
        def isNotBorder(r, c):
            return 0 < r < len(board)-1 and 0 < c < len(board[0])-1
        def dfs(r, c):
            if visited[r][c] == 2: # already visited
                return isX(board[r][c])
            elif visited[r][c] == 1:
                return True
            elif isX(board[r][c]): # visited[r][c] = 0 or 1 and is 'X'
                visited[r][c] = 2
                return True
            elif not isNotBorder(r, c): # visited[r][c] = 0 or 1 and is 'O' and at border
                visited[r][c] = 2
                return False
            else: # visited[r][c] = 0 or 1 and is 'O' and not at border
                visited[r][c] = 1
                right = left = up = down = True
                right = dfs(r+1, c)
                left = dfs(r-1, c)
                down = dfs(r, c+1)
                up = dfs(r, c-1)
                state = right and left and up and down
                
                visited[r][c] = 2
                return state
                
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O': dfs(r, c)

'''
why not work: 
dfs(a) depends on dfs(b)
dfs(b) depends on dfs(a)
=> infinite recursion or wrong caching.
'''


                
                
                
        