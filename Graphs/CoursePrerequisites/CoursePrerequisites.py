from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        self.prereqs = defaultdict(list)

        for prereq, crs in prerequisites:
            self.prereqs[crs].append(prereq)

        self.topological_order = []

        self.visited = [0 for x in range(numCourses)] # DAG detection 
        for x in range(numCourses):
            if not self.dfs(x):
                return []
             # continue to search the whole graph
        return self.topological_order[::-1]

    def dfs(self, node):

        if self.visited[node] == -1: # cycle detected
            return False
        if self.visited[node] == 1:
            return True # has been finished, and been added to self.res
        self.visited[node] = -1 # mark as visited
        for neighbour in self.prereqs[node]:
            if not self.dfs(neighbour):
                return False
        self.visited[node] = 1 # mark as finished
        self.topological_order.append(node) # add to solution as the course depenedent on previous ones
        return True