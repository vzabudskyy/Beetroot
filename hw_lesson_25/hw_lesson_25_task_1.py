from typing import List


class Vertex:
    def __init__(self, name):
        self.name = name
        self._neighbours = set()
        self._marked: bool = False
        self.path = []

    def add_neighbour(self, new_newigbour: 'Vertex'):
        self._neighbours.add(new_newigbour)

    def unmark(self):
        self._marked = False

    @property
    def neighbours(self):
        return self._neighbours

    def is_marked(self):
        return self._marked

    def mark(self):
        self._marked = True

    def __iter__(self):
        return iter(self.neighbours)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'Vertex "{self.name}"'




class Graph:
    def __init__(self, edges):
        self._vertices = {name: Vertex(name) for name in edges.keys()}

        for name, neighbours in edges.items():
            current_vertex = self._vertices[name]
            for neighbour in neighbours:
                current_vertex.add_neighbour(self._vertices[neighbour])

    def depth_search(self, start: str, finish: str):
        start_vertex = self._vertices[start]
        start_vertex.mark()
        start_vertex.path.append(start_vertex)
        if start == finish:
            return start_vertex.path
        for neighbor in start_vertex:
            if not neighbor.is_marked():
                neighbor.path = start_vertex.path.copy()
                path = self.depth_search(neighbor.name, finish)
                if path:
                    return path

    def breadth_search(self, start: str, finish: str) -> List[Vertex]:
        finish_vertex = self._vertices[finish]
        all_ways = [[self._vertices[start]]]
        level_vertexes = [self._vertices[start]]
        while level_vertexes:
            vertex = level_vertexes.pop(0)
            vertex.mark()
            current_ways = []
            for neightbor in vertex:
                if neightbor.is_marked():
                    continue
                level_vertexes.append(neightbor)
                for way in all_ways:
                    if way[-1] == vertex:
                        way_to_neighbor = way.copy() + [neightbor]
                        if neightbor == finish_vertex:
                            return way_to_neighbor
                        current_ways.append(way_to_neighbor)
            all_ways = all_ways + current_ways
        return all_ways

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

edges2 = {'1': ['2', '3', '4'],
          '2': ['1', '5', '6'],
          '3': ['1'],
          '4': ['1', '7', '8'],
          '5': ['2', '9', '10'],
          '6': ['2', '14'],
          '7': ['4', '13', '11', '12'],
          '8': ['4'],
          '9': ['5'],
          '10': ['5'],
          '11': ['7'],
          '12': ['7'],
          '13': ['7', '14'],
          '14': ['6', '13']}


if __name__ == "__main__":
    graph = Graph(edges2)
    print(graph.depth_search('1', '8'))
    for i in graph._vertices.values():
        i.unmark()
    print(graph.breadth_search('1', '8'))
