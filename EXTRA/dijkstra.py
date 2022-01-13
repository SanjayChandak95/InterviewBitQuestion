import collections


class Solution:
    def dijkstra(self, edges, n, src):
        graph = collections.defaultdict(dict)

        for u, v, weight in edges:
            graph[u][v] = weight
        dist = [float("inf")] * n
        dist[src] = 0
        visited = set()

        def get_min():
            min_index = -1
            min_val = float("inf")
            for i, val in enumerate(dist):
                if i not in visited:
                    if val < min_val:
                        min_val = val
                        min_index = i
            return min_index

        for _ in range(n):
            x = get_min()
            visited.add(x)

            for node in graph[x]:
                if graph[x][node] > 0 and (node not in visited) and dist[node] > dist[x] + graph[x][node]:
                    dist[node] = dist[x] + graph[x][node]
        print(dist)


    def bellmon(self, edges, n, src):
        graph = collections.defaultdict(dict)

        for u, v, weight in edges:
            graph[u][v] = weight
        dist = [float("inf")] * n
        dist[src] = 0

        for _ in range(n):
            for src in graph.keys():
                for dest, weight in graph[src].items():
                    if dist[src] != float("inf") and dist[dest] > dist[src] + weight:
                        dist[dest] = dist[src] + weight

        # checking -ve cycle
        for src in graph.keys():
            for dest, weight in graph[src].items():
                if dist[src] != float("inf") and dist[dest] > dist[src] + weight:
                    print("negative cycle detected!!")
        print(dist)


if __name__ == "__main__":
    n = 4
    edges = [(0,1,100),(0,2,10),(2,1,10),(0,3,5), (3,2,1)]
    Solution().dijkstra(edges, n, 0)
    Solution().bellmon(edges,n,0)
