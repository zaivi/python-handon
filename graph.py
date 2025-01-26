from collections import deque


class Graph:
    def __init__(self, edges, n):
        self.n = n
        self.adj_lst = [[] for _ in range(n)]

        for (src, des) in edges:
            self.adj_lst[src].append(des)
            self.adj_lst[des].append(src)
        
    def bfs(self, v):
        discovered = [False] * self.n

        queue = deque()
        queue.append(v)

        discovered[v] = True

        while queue:
            value = queue.popleft()
            print(f"{value=}")

            for adj in self.adj_lst[value]:
                if not discovered[adj]:
                    queue.append(adj)
                    discovered[adj] = True
    
    def bfs_recur(self, queue, discovered):
        if not queue:
            return

        while queue:
            value = queue.popleft()
            print(f"{value=}")

            for adj in self.adj_lst[value]:
                if not discovered[adj]:
                    queue.append(adj)
                    discovered[adj] = True
            
            self.bfs_recur(queue, discovered)

    def dfs(self, v):
        discovered = [False] * self.n

        stack = deque()
        stack.append(v)

        discovered[v] = True

        while stack:
            value = stack.pop()
            print(f"{value=}")

            for adj in reversed(self.adj_lst[value]):
                if not discovered[adj]:
                    stack.append(adj)
                    discovered[adj] = True
    
    def dfs_recur(self, v, discovered):

        print(f"{v=}")
        discovered[v] = True

        for adj in self.adj_lst[v]:
            if not discovered[adj]:
                self.dfs_recur(adj, discovered)


if __name__ == "__main__":
    edges = [
        # Notice that node 0 is unconnected
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (4, 5), (7, 8), (8, 9), (8, 12), (9, 10), (9, 11)
    ]
    # total number of nodes in the graph (labelled from 0 to 12)
    n = 13

    g = Graph(edges, n)

    discovered = [False] * n

    # g.bfs(1)

    print("----____-----")

    queue = deque()
    queue.append(1)

    # g.bfs_recur(queue, discovered)

    print("----____-----")

    g.dfs(1)

    print("----____-----")

    g.dfs_recur(1, discovered)
