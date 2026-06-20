class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])


     
    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex]= []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other in self.adj_list[vertex]:
                self.adj_list[other].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    def bfs(self, start):
        if start not in self.adj_list:
            return []
        visited = set()
        queue = [start]
        visited.add(start)
        result = []
        while queue:
            vertex = queue.pop(0)
            result.append(vertex)
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start):
        if start not in self.adj_list:
            return []
        visited = set()
        result = []

        def _dfs(vertex):
            visited.add(vertex)
            result.append(vertex)
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start)
        return result


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')


my_graph.remove_vertex('D')

my_graph.print_graph()
                    