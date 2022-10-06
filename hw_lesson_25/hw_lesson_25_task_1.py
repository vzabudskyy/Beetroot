class Vertex:
    def __init__(self, name):
        self.name = name
        self._neighbours = set()
        self._marked: bool = False

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
        all_ways = [start]
        start_vertex = self._vertices[start]
        finish_vertex = self._vertices[finish]
        level_vertexes = [start_vertex]
        while level_vertexes:
            neighbours = []
            for vertex in level_vertexes:
                vertex.mark()
                for neighbour in vertex:
                    current_ways = []
                    for way in all_ways:
                        if way[-1] == vertex.name:
                            way_to_neighbor = way + neighbour.name
                            if len(way_to_neighbor) <= 2:
                                current_ways.append(way_to_neighbor)
                            elif len(way_to_neighbor) >= 3 and way_to_neighbor[-1] != way_to_neighbor[-3]:
                                current_ways.append(way_to_neighbor)
                    all_ways = all_ways + current_ways
                    if neighbour.is_marked():
                        continue
                    neighbours.append(neighbour)

            level_vertexes = neighbours
        result = None
        for path in all_ways:
            if path[-1] == finish and (result is None or len(path) < len(result)):
                result = path
        return result

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


graph = Graph(edges)
print(graph)
print(graph.find_shortest_way('1', '6'))