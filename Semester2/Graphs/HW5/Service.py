from MyExceptions import GraphExceptions
from UndirectedGraph import UndirectedGraph
import copy


class Service:
    def __init__(self):
        self._graph = UndirectedGraph(0)
        self._current_graph_name = 'empty_graph'
        self._graphs_list = {'empty_graph': copy.deepcopy(self._graph)}

    def read_graph_from_file(self, filename, graph_name):
        if graph_name in self._graphs_list.keys():
            raise GraphExceptions("There exist already a graph with this name. Try again")
        with open(filename, 'r') as file:
            lines = file.readlines()
            non_isolated_vertices_edges = []
            isolated_vertices = []
            non_consecutive_vertices_edges = []
            first_line = lines[0]
            first_line = first_line.split(" ")
            vertices_number = int(first_line[0])
            lines[0] = ""
            self._graph = UndirectedGraph(vertices_number)
            for line in lines:
                line = line.strip()
                if line != "":
                    line = line.split(" ")
                    if len(line) == 3:
                        source = int(line[0])
                        destination = int(line[1])
                        if source >= vertices_number or destination >= vertices_number:
                            non_consecutive_vertices_edges.append(line)
                            vertices_number -= 1
                        else:
                            non_isolated_vertices_edges.append(line)
                    elif len(line) == 2:
                        vertex = int(line[0])
                        isolated_vertices.append(vertex)
                        if vertex >= vertices_number:
                            vertices_number -= 1
            self._graph.initialize_dictionaries_of_the_graph(vertices_number)
            for edge in non_isolated_vertices_edges:
                source = int(edge[0])
                destination = int(edge[1])
                cost = int(edge[2])
                self._graph.add_edge(source, destination, cost)
            if len(non_consecutive_vertices_edges):
                for edge in non_consecutive_vertices_edges:
                    source = int(edge[0])
                    destination = int(edge[1])
                    cost = int(edge[2])
                    if source > vertices_number:
                        self._graph.add_vertex(source)
                    if destination > vertices_number:
                        self._graph.add_vertex(destination)
                    self._graph.add_edge(source, destination, cost)
            if len(isolated_vertices) > 0:
                for vertex in isolated_vertices:
                    self._graph.add_vertex(vertex)
        self._graphs_list[graph_name] = copy.deepcopy(self._graph)
        self._current_graph_name = graph_name

    def write_graph_to_file(self, filename):
        with open(filename, 'w') as file:
            lines = self._graph.get_graph_in_format_for_textfile()
            for line in lines:
                file.write(line)
                file.write('\n')

    def create_random_graph(self, vertices_number, edges_number, graph_name):
        if graph_name in self._graphs_list.keys():
            raise GraphExceptions("There exist already a graph with this name. Try again")
        self._graph = UndirectedGraph(vertices_number)
        self._graph.initialize_dictionaries_of_the_graph(vertices_number)
        i = 0
        if edges_number > vertices_number * (vertices_number - 1):
            raise GraphExceptions("The number of edges is too big for this graph! Graph was not created.")
        while i < edges_number:
            self._graph.create_random_edge()
            i += 1
        self._graphs_list[graph_name] = copy.deepcopy(self._graph)
        self._current_graph_name = graph_name

    def service_get_number_of_vertices(self):
        return self._graph.get_number_of_vertices()

    def service_get_iterable_of_vertices(self):
        return self._graph.get_iterable_of_vertices()

    def service_check_if_edge_exists(self, source_vertex, destination_vertex):
        if self._graph.is_vertex(source_vertex) is False or self._graph.is_vertex(destination_vertex) is False:
            raise GraphExceptions("Wrong values of vertices!")
        return self._graph.is_edge(source_vertex, destination_vertex)

    def get_degree_of_vertex(self, vertex):
        if self._graph.is_vertex(vertex) is False:
            raise GraphExceptions("Vertex does not exist!")
        return self._graph.get_degree(vertex)

    def service_get_iterable_of_edges(self, vertex):
        if self._graph.is_vertex(vertex) is False:
            raise GraphExceptions("Vertex does not exist!")
        return self._graph.get_iterable_of_edges(vertex)

    def service_get_edge_cost(self, source_vertex, destination_vertex):
        if self._graph.is_vertex(source_vertex) is False or self._graph.is_vertex(destination_vertex) is False:
            raise GraphExceptions("One or both of the vertices do not exist!")
        if not self._graph.is_edge(source_vertex, destination_vertex):
            raise GraphExceptions("The edge does not exist.")
        return self._graph.get_edge_cost(source_vertex, destination_vertex)

    def service_change_edge_cost(self, source_vertex, destination_vertex, cost):
        if self._graph.is_vertex(source_vertex) is False or self._graph.is_vertex(destination_vertex) is False:
            raise GraphExceptions("One or both of the vertices do not exist!")
        if not self._graph.is_edge(source_vertex, destination_vertex):
            raise GraphExceptions("The edge does not exist.")
        self._graph.change_edge_cost(source_vertex, destination_vertex, cost)

    def service_add_edge(self, source_vertex, destination_vertex, cost):
        if self._graph.is_vertex(source_vertex) is False or self._graph.is_vertex(destination_vertex) is False:
            raise GraphExceptions("One or both of the vertices do not exist!")
        if self._graph.is_edge(source_vertex, destination_vertex):
            raise GraphExceptions("The edge already exist.")
        self._graph.add_edge(source_vertex, destination_vertex, cost)

    def service_remove_edge(self, source_vertex, destination_vertex):
        if self._graph.is_vertex(source_vertex) is False or self._graph.is_vertex(destination_vertex) is False:
            raise GraphExceptions("One or both of the vertices do not exist!")
        if not self._graph.is_edge(source_vertex, destination_vertex):
            raise GraphExceptions("The edge does not exist.")
        self._graph.remove_edge(source_vertex, destination_vertex)

    def service_add_vertex(self, vertex):
        if self._graph.is_vertex(vertex) is True:
            raise GraphExceptions("Vertex already exists.")
        else:
            self._graph.add_vertex(vertex)

    def service_remove_vertex(self, vertex):
        if self._graph.is_vertex(vertex) is True:
            self._graph.remove_vertex(vertex)
        else:
            raise GraphExceptions("Vertex doesn't exists.")

    def copy_graph(self, graph_name):
        copy_graph = self._graph.get_copy_of_graph()
        self._graphs_list[graph_name] = copy.deepcopy(copy_graph)
        return copy_graph

    def change_the_current_graph(self, graph_name):
        if graph_name not in self._graphs_list.keys():
            raise GraphExceptions("There is no graph with this name. Try again")
        self._graphs_list[self._current_graph_name] = copy.deepcopy(self._graph)
        self._graph = copy.deepcopy(self._graphs_list[graph_name])
        self._current_graph_name = graph_name

    def get_graphs_name_list(self):
        return self._graphs_list.keys()

    def get_hamiltonian_cycle(self):
        vertices_number = self._graph.get_number_of_vertices()
        edges_number = self._graph.get_number_of_edges()

        if edges_number != (vertices_number*(vertices_number -1))/2:
            raise GraphExceptions("The graph is not complete!\n")

        return self._graph.get_hamiltonian_cycle()