from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)
        for origin, destination in tickets:
            graph[origin].append(destination)
        
        visited = {}

        for origin, destinations in graph.items():
            destinations.sort()
            visited[origin] = [False] * len(destinations)
            

        routes = []
        def backtracking(origin, route):
            if len(route) == len(tickets) + 1:
                routes.append(list(route))
                return
            
            
            for i, dest in enumerate(graph[origin]):
                if not visited[origin][i]:
                    visited[origin][i] = True
                    route.append(dest)
                    backtracking(dest, route)
                    route.pop()
                    visited[origin][i] = False
            
        
        backtracking("JFK", ["JFK"])
        return routes[0]

        