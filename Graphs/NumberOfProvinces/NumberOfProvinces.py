from typing import List

class Solution(object):
    def findCircleNum(self, isConnected):
        total = 0
        visit = [False] * len(isConnected)
        n_comps = 0

        def bfs(j):
            queue = []
            queue.append(j)
            while queue:
                node = queue.pop(0)
                visit[node] = True
                for i in range(len(isConnected)):
                    if isConnected[node][i] and not visit[i]:
                        queue.append(i)

        for j in range(len(isConnected)):
            if not visit[j]:
                n_comps += 1
                bfs(j)

        return n_comps
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        total = 0
        visit = [False] * len(isConnected)
        n_comps = 0

        def dfs(node, isConnected):
            visit[node] = True
            for i in range(len(isConnected)):
                if isConnected[node][i] and not visit[i]:
                    dfs(i, isConnected)

        for j in range(len(isConnected)):
            if not visit[j]:
                n_comps += 1
                dfs(j, isConnected)

        return n_comps
            