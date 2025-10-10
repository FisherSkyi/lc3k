'''
course scheduler II
if many valid answers, return any of them
if no valid answer, return empty list

dfs-loop (graph G)
- mark all nodes unexplored
- current label = n (to keep track of ordering)
- for each vertex v of G:
    - if v has not been explored yet:
        - dfs(G, v)

dfs(graph G, starting_point s):
- mark s as explored
- for all outgoing neighbors of s, i.e. every edge (s, v):
    - if v is not explored yet:
        - dfs(G, v)
- set f(s) = current label
- current label -= 1
'''
from typing import List

class Solution:
    def findOrder(self, numOfCourse: int, prerequest: List[List[int]]):
        # set up the graph as adjacent list
        graph = {}
        for r in prerequest:
            s = r[1]
            e = r[0]
            graph[s] = graph.get(s, []) + [e]
        # print(graph)
        visited = [0 for _ in range(numOfCourse)]
        has_cycle = False
        ans = []
        def dfs(v: int):
            nonlocal has_cycle
            if has_cycle:
                return
            if visited[v] == 1: # children not fully explored
                has_cycle = True
                return
            if visited[v] == 2: # fully explored
                return
            visited[v] = 1
            for u in graph.get(v, []):
                dfs(u)
            visited[v] = 2
            ans.append(v)
        for v in range(numOfCourse):
            if not visited[v]:
                dfs(v)
        return ans[::-1]

def main():
    s = Solution()
    assert s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) == [0,2,1,3]


if __name__ == '__main__':
    main()