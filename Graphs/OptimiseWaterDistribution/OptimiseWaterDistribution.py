from collections import defaultdict

class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        """
        :type n: int
        :type wells: List[int]
        :type pipes: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)

        # create virtual vertex
        for index, cost in enumerate(wells):
            graph[0].append((cost, index + 1))        
        
        # add costs (adjacency graph)
        for house_1, house_2, cost in pipes:
            graph[house_1].append((cost, house_2))
            graph[house_2].append((cost, house_1))

        # A set to maintain all the vertex that has been added to
        #   the final MST (Minimum Spanning Tree),
        #   starting from the vertex 0.

         # heap to maitain the order of edges to be visited
        mst_set = set([0])
        heapq.heapify(graph[0])
        edges_heap = graph[0]

        total_cost = 0

        while len(mst_set) < n + 1:
            cost, nextHouse = heapq.heappop(edges_heap)
            if nextHouse not in mst_set:
                mst_set.add(nextHouse)
                total_cost += cost
                for new_cost, neighbour in graph[nextHouse]:
                    if neighbour not in mst_set:
                        heapq.heappush(edges_heap, (new_cost, neighbour))

        return total_cost