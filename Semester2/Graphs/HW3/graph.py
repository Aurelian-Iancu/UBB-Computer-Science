import copy
import math


class TripleDictGraph:
    def __init__(self, number_of_vertices, number_of_edges):
        self._number_of_vertices = number_of_vertices
        self._number_of_edges = number_of_edges
        self._dictionary_in = {}
        self._dictionary_out = {}
        self._dictionary_cost = {}
        for index in range(number_of_vertices):
            self._dictionary_in[index] = []
            self._dictionary_out[index] = []

    @property
    def dictionary_cost(self):
        return self._dictionary_cost

    @property
    def dictionary_in(self):
        return self._dictionary_in

    @property
    def dictionary_out(self):
        return self._dictionary_out

    @property
    def number_of_vertices(self):
        return self._number_of_vertices

    @property
    def number_of_edges(self):
        return self._number_of_edges

    def parse_vertices(self):
        vertices = list(self._dictionary_in.keys())
        for v in vertices:
            yield v

    def parse_inbound(self, x):
        for y in self._dictionary_in[x]:
            yield y

    def parse_outbound(self, x):
        for y in self._dictionary_out[x]:
            yield y

    def parse_cost(self):
        keys = list(self._dictionary_cost.keys())
        for key in keys:
            yield key

    def add_vertex(self, x):
        if x in self._dictionary_in.keys() and x in self._dictionary_out.keys():
            return False
        self._dictionary_in[x] = []
        self._dictionary_out[x] = []
        self._number_of_vertices += 1
        return True

    def remove_vertex(self, x):
        if x not in self._dictionary_in.keys() and x not in self._dictionary_out.keys():
            return False
        self._dictionary_in.pop(x)
        self._dictionary_out.pop(x)
        for key in self._dictionary_in.keys():
            if x in self._dictionary_in[key]:
                self._dictionary_in[key].remove(x)
            elif x in self._dictionary_out[key]:
                self._dictionary_out[key].remove(x)
        keys = list(self._dictionary_cost.keys())
        for key in keys:
            if key[0] == x or key[1] == x:
                self._dictionary_cost.pop(key)
                self._number_of_edges -= 1
        self._number_of_vertices -= 1
        return True

    def in_degree(self, x):
        if x not in self._dictionary_in.keys():
            return -1
        return len(self._dictionary_in[x])

    def out_degree(self, x):
        if x not in self._dictionary_out.keys():
            return -1
        return len(self._dictionary_out[x])

    def add_edge(self, x, y, cost):
        if x in self._dictionary_in[y]:
            return False
        elif y in self._dictionary_out[x]:
            return False
        elif (x, y) in self._dictionary_cost.keys():
            return False
        self._dictionary_in[y].append(x)
        self._dictionary_out[x].append(y)
        self._dictionary_cost[(x, y)] = cost
        self._number_of_edges += 1
        return True

    def remove_edge(self, x, y):
        if x not in self._dictionary_in.keys() or y not in self._dictionary_in.keys() or x not in self._dictionary_out.keys() or y not in self._dictionary_out.keys():
            return False
        if x not in self._dictionary_in[y]:
            return False
        elif y not in self._dictionary_out[x]:
            return False
        elif (x, y) not in self._dictionary_cost.keys():
            return False
        self._dictionary_in[y].remove(x)
        self._dictionary_out[x].remove(y)
        self._dictionary_cost.pop((x, y))
        self._number_of_edges -= 1
        return True

    def find_if_edge(self, x, y):
        if x in self._dictionary_in[y]:
            return self._dictionary_cost[(x, y)]
        elif y in self._dictionary_out[x]:
            return self._dictionary_cost[(x, y)]
        return False

    def change_cost(self, x, y, cost):
        if (x, y) not in self._dictionary_cost.keys():
            return False
        self._dictionary_cost[(x, y)] = cost
        return True

    def make_copy(self):
        return copy.deepcopy(self)

    def check_edge(self, first_vertex, second_vertex):
        for vertex in self._dictionary_out[first_vertex]:
            if vertex == second_vertex:
                return True
        return False

    def get_cost(self, edge):
        return self._dictionary_cost[edge]

    # For homework 3
    def get_matrix_of_graph(self):
        infinity = math.inf
        matrix = [[infinity for index1 in self.parse_vertices()] for index2 in self.parse_vertices()]
        for index1 in self.parse_vertices():
            for index2 in self.parse_vertices():
                if self.check_edge(index1, index2):
                    matrix[index1][index2] = self.get_cost((index1, index2))
        return matrix

    def extend(self, matrix, adjacencyMatrix, prevMatrix, lengthPath, startVertex):
        copyOfMatrix = copy.deepcopy(matrix)
        for index1 in range(len(matrix)):
            for index2 in range(len(matrix)):
                if index1 != index2:
                    matrix[index1][index2] = math.inf
                    for index3 in range(len(matrix)):
                        if startVertex == index1:
                            if prevMatrix[lengthPath][index2] == -1:
                                if matrix[index1][index2] > copyOfMatrix[index1][index3] + adjacencyMatrix[index3][index2]:
                                    prevMatrix[lengthPath][index2] = index3
                                else:
                                    prevMatrix[lengthPath][index2] = prevMatrix[lengthPath - 1][index2]
                        matrix[index1][index2] = min(matrix[index1][index2],
                                                     copyOfMatrix[index1][index3] + adjacencyMatrix[index3][index2])
        return matrix, prevMatrix

    def slow_apsp(self, startVertex, endVertex):
        matrix = self.get_matrix_of_graph()
        adjacencyMatrix = self.get_matrix_of_graph()
        prevMatrix = [[-1 for index1 in range(len(matrix))] for index2 in range(len(matrix))]
        for index in range(len(matrix)):
            matrix[index][index] = 0
            if self.check_edge(startVertex, index):
                prevMatrix[1][index] = startVertex

        for index in range(2, len(matrix)):
            copyOfMatrix = copy.deepcopy(matrix)
            matrix, prevMatrix = self.extend(copyOfMatrix, adjacencyMatrix, prevMatrix, index, startVertex)

        for index1 in range(len(matrix)):
            for index2 in range(len(matrix)):
                if matrix[index1][index2] < 0:
                    raise Exception("There are negative cycles in the graph!\n")

        if matrix[startVertex][endVertex] == math.inf:
            raise Exception("There is no path between the start and the end vertex!\n")

        return matrix

    def get_shortest_cost(self, vertex1, vertex2):
        matrix = self.slow_apsp(vertex1, vertex2)
        return matrix[vertex1][vertex2]


def write_graph_to_file(graph, file):
    file = open(file, "w")
    first_line = str(graph.number_of_vertices) + ' ' + str(graph.number_of_edges) + '\n'
    file.write(first_line)
    if len(graph.dictionary_cost) == 0 and len(graph.dictionary_in) == 0:
        raise ValueError("There is nothing that can be written!")
    for edge in graph.dictionary_cost.keys():
        new_line = "{} {} {}\n".format(edge[0], edge[1], graph.dictionary_cost[edge])
        file.write(new_line)
    for vertex in graph.dictionary_in.keys():
        if len(graph.dictionary_in[vertex]) == 0 and len(graph.dictionary_out[vertex]) == 0:
            new_line = "{}\n".format(vertex)
            file.write(new_line)
    file.close()


def read_graph_from_file(filename):
    file = open(filename, "r")
    line = file.readline()
    line = line.strip()
    vertices, edges = line.split(' ')
    graph = TripleDictGraph(int(vertices), int(edges))
    line = file.readline().strip()
    while len(line) > 0:
        line = line.split(' ')
        if len(line) == 1:
            graph.dictionary_in[int(line[0])] = []
            graph.dictionary_out[int(line[0])] = []
        else:
            graph.dictionary_in[int(line[1])].append(int(line[0]))
            graph.dictionary_out[int(line[0])].append(int(line[1]))
            graph.dictionary_cost[(int(line[0]), int(line[1]))] = int(line[2])
        line = file.readline().strip()
    file.close()
    return graph