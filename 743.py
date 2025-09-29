from collections import defaultdict
from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Dijkstra Algorithm
        time complexity: O(E log V) E is the number of edges, V is the number of vertices
        space complexity: O(V)

        This is the link state routing algorithm, which requires each node to have the complete network topology.
        Bellman-Ford algorithm is the distance vector routing algorithm, which requires each node to know only the distance to its neighbors.
        """
        # construct the adjacent list
        adjList = defaultdict(list)
        for e in times:
            s = e[0]
            t = e[1]
            w = e[2]
            adjList[s].append((t,w)) # if use dictionary, need to check if key exists
                                     # otherwise, key error
        print(adjList)

        # use min-heap as priority queue
        pq = []

        dist = [float('inf')] * (n + 1) # unuse index 0, use 1 to n
        heapq.heappush(pq, (k, 0))
        dist[k] = 0

        while pq:
            node = heapq.heappop(pq)[0]
            for neighbor in adjList[node]:
                v, w = neighbor[0], neighbor[1]
                # relax the edge
                if dist[node] + w < dist[v]:
                    dist[v] = dist[node] + w
                    heapq.heappush(pq, (v, dist[v]))
        
        ans = max(dist[1:])

        return ans if ans < float('inf') else -1 # type: ignore

# test
s = Solution()
print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)) # 2
print(s.networkDelayTime([[1,2,1]], 2, 1)) # 1
print(s.networkDelayTime([[1,2,1]], 2, 2)) # -1
print(s.networkDelayTime([[1,2,1],[2,3,2],[1,3,2]], 3, 1)) # 2
print(s.networkDelayTime([[1,2,1],[2,3,2],[1,3,4]], 3, 1)) # 3
print(s.networkDelayTime([[1,2,1],[2,3,2],[1,3,1]], 3, 1)) # 1
