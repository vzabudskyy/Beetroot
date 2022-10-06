class Vertex:
    def __init__(self, name):
        self.name = name
        self._neighbours = set()
        self._marked: bool = False
        self._previous =

    def add_neighbour(self, new_newigbour: 'Vertex'):
        self._neighbours.add(new_newigbour)

    def is_marked(self):
        return self._marked

    def mark(self):
        self._marked = True

    def __iter__(self):
        return iter(self._neighbours)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'Vertex {self.name} with neighbours ' \
               f'{[n.name for n in self._neighbours]}'

class Graph:
    def __init__(self, edges):
        vertices_names = ['1', '2', '3', '4', '5', '6', '7', '8']
        self._vertices = {name: Vertex(name) for name in vertices_names}

        for name, neighbours in edges.items():
            current_vertex = self._vertices[name]
            for neighbour in neighbours:
                current_vertex.add_neighbour(self._vertices[neighbour])

    def find_shortest_way(self, start: str, finish: str):
        start_vertex = self._vertices[start]
        print(start)
        finish_vertex = self._vertices[finish]
        for neighbor in start_vertex:
            if not neighbor.is_marked():
                self.find_shortest_way(neighbor.name, finish)
        start_vertex.marked()





    def __str__(self):
        return '\n'.join([str(vertex) for vertex in self._vertices.values()])


edges = {'1': ['2', '3', '4'],
                '2': ['1', '5', '6'],
                '3': ['1'],
                '4': ['1', '7', '8'],
                '5': ['2'],
                '6': ['2'],
                '7': ['4'],
                '8': ['4']}


if __name__ == "__main__":
    graph = Graph(edges)
    print(graph)
    graph.find_shortest_way('1', '6')