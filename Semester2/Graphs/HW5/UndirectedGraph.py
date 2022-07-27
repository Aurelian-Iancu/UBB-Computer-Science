import copy
import sys
import math
from random import randrange


class UndirectedGraph:
    def __init__(self, vertices_number):
        self._dictNeighbours = {}
        self._dictCosts = {}
        self._vertices_number = vertices_number
        self._edges_number = 0

    def initialize_dictionaries_of_the_graph(self, number_of_vertices):
        self._vertices_number = number_of_vertices
        for index in range(0, number_of_vertices):
            self._dictNeighbours[index] = []

    def add_vertex(self, new_vertex):
        self._dictNeighbours[new_vertex] = []
        self._vertices_number += 1

    def is_vertex(self, searched_vertex):
        for vertex in self._dictNeighbours:
            if searched_vertex == vertex:
                return True
        return False

    def add_edge(self, one_vertex, second_vertex, cost):
        self._dictNeighbours[one_vertex].append(second_vertex)
        self._dictNeighbours[second_vertex].append(one_vertex)
        self._dictCosts[(one_vertex, second_vertex)] = cost
        # self._dictCosts[(second_vertex, one_vertex)] = cost
        self._edges_number += 1

    def _get_position_of_vertex_in_list(self, vertex, vertices_list):
        vertex_index = 0
        while vertex_index < len(vertices_list):
            if vertices_list[vertex_index] == vertex:
                return vertex_index
            vertex_index += 1
        return -1

    def _remove_vertex_from_dNeighbours(self, neighbour_vertex, vertex_to_remove):
        index_vertex_to_remove = self._get_position_of_vertex_in_list(vertex_to_remove,
                                                                      self._dictNeighbours[neighbour_vertex])
        if index_vertex_to_remove == -1:
            return -1
        self._dictNeighbours[neighbour_vertex].pop(index_vertex_to_remove)

    def remove_edge(self, one_vertex, second_vertex):
        try:
            del self._dictCosts[one_vertex, second_vertex]
        except KeyError:
            del self._dictCosts[second_vertex, one_vertex]
        self._remove_vertex_from_dNeighbours(one_vertex, second_vertex)
        self._remove_vertex_from_dNeighbours(second_vertex, one_vertex)
        self._edges_number -= 1

    def remove_vertex(self, vertex):
        for neighbour_vertex in self._dictNeighbours[vertex]:
            self._remove_vertex_from_dNeighbours(neighbour_vertex, vertex)
            try:
                del self._dictCosts[(vertex, neighbour_vertex)]
            except KeyError:
                del self._dictCosts[(neighbour_vertex, vertex)]
            self._edges_number -= 1
        del self._dictNeighbours[vertex]
        self._vertices_number -= 1

    def get_number_of_vertices(self):
        return self._vertices_number

    def get_iterable_of_vertices(self):
        for vertex in list(self._dictNeighbours.keys()):
            yield vertex

    def get_degree(self, vertex):
        return len(self._dictNeighbours[vertex])

    def is_edge(self, one_vertex, second_vertex):
        for vertex in self._dictNeighbours[one_vertex]:
            if second_vertex == vertex:
                return True
        return False

    def get_iterable_of_edges(self, vertex):
        for neighbour_vertex in self._dictNeighbours[vertex]:
            yield neighbour_vertex

    def get_edge_cost(self, one_vertex, second_vertex):
        val = 0
        try:
            val = self._dictCosts[(one_vertex, second_vertex)]
        except KeyError:
            val = self._dictCosts[(second_vertex, one_vertex)]
        return val

    def change_edge_cost(self, one_vertex, second_vertex, new_cost):
        try:
            self._dictCosts[(one_vertex, second_vertex)] = new_cost
        except KeyError:
            self._dictCosts[(second_vertex, one_vertex)] = new_cost

    def get_copy_of_graph(self):
        new_graph = copy.deepcopy(self)
        return new_graph

    def get_number_of_edges(self):
        return self._edges_number

    def create_random_edge(self):
        valid = False
        while not valid:
            start_vertex = randrange(0, self._vertices_number)
            end_vertex = randrange(0, self._vertices_number)
            cost = randrange(-10000, 10000)
            if start_vertex != end_vertex and not self.is_edge(start_vertex, end_vertex):
                valid = True
                self.add_edge(start_vertex, end_vertex, cost)

    def get_graph_in_format_for_textfile(self):
        lines = [str(self.get_number_of_vertices()) + " " + str(self.get_number_of_edges())]
        for edge in self._dictCosts:
            lines.append(str(edge[0]) + " " + str(edge[1]) + " " + str(self._dictCosts[edge]))
        for vertex in self._dictNeighbours:
            if len(self._dictNeighbours[vertex]) == 0:
                lines.append(str(vertex) + " -1")
        return lines

    def _get_vertex_root(self, vertex, vertex_root):
        # if vertex is the root
        if vertex_root[vertex] == vertex:
            return vertex

        return self._get_vertex_root(vertex_root[vertex], vertex_root)

    def edge_can_be_added(self, vertex_root, one_vertex, second_vertex):
        degree_of_vertex_one = len(self._dictNeighbours[one_vertex])
        degree_of_second_vertex = len(self._dictNeighbours[second_vertex])
        root_of_one_vertex = self._get_vertex_root(one_vertex, vertex_root)
        root_of_one_second_vertex = self._get_vertex_root(second_vertex, vertex_root)

        if root_of_one_vertex != root_of_one_second_vertex and degree_of_vertex_one < 2 \
                and degree_of_second_vertex < 2:
            return True

        return False

    def change_vertex_parent_array(self, vertex_root, one_vertex, second_vertex):
        if len(self._dictNeighbours[one_vertex]) > 0:
            vertex_root[second_vertex] = vertex_root[one_vertex]
        elif len(self._dictNeighbours[second_vertex]) > 0:
            vertex_root[one_vertex] = vertex_root[second_vertex]
        elif vertex_root[one_vertex] > vertex_root[second_vertex]:
            vertex_root[second_vertex] = vertex_root[one_vertex]
        else:
            vertex_root[one_vertex] = vertex_root[second_vertex]

    def get_hamiltonian_cycle(self):
        ordered_edges = dict(sorted(self._dictCosts.items(), key=lambda arr: arr[1]))
        cost = 0

        # initialize the new graph
        cycle_H = UndirectedGraph(self._vertices_number)
        cycle_H.initialize_dictionaries_of_the_graph(self._vertices_number)

        # this will contain the "root"/ parent of every vertex
        vertex_root = {}
        for vertex in cycle_H.get_iterable_of_vertices():
            vertex_root[vertex] = vertex

        for edge in ordered_edges:
            if cycle_H.get_number_of_edges() == cycle_H.get_number_of_vertices() - 1:
                break
            if cycle_H.edge_can_be_added(vertex_root, edge[0], edge[1]):
                cycle_H.change_vertex_parent_array(vertex_root, edge[0], edge[1])
                cycle_H.add_edge(edge[0], edge[1], self._dictCosts[edge])
                cost += self._dictCosts[edge]

        # we determine the two vertices that have degree one and we will add the edge between them to our cycle
        start_vertex = -1
        end_vertex = -1
        for vertex in cycle_H._dictNeighbours:
            if len(cycle_H._dictNeighbours[vertex]) == 1:
                if start_vertex == -1:
                    start_vertex = vertex
                else:
                    end_vertex = vertex
                    break
        cycle_H.add_edge(end_vertex, start_vertex, self.get_edge_cost(end_vertex, start_vertex))
        cost += cycle_H._dictCosts[end_vertex, start_vertex]

        # we will put the hamiltonian cycle (the vertices) obtained in a list
        hamiltonian_cycle = [start_vertex]
        vertex = cycle_H._dictNeighbours[start_vertex][0]
        while vertex != start_vertex:
            hamiltonian_cycle.append(vertex)
            if cycle_H._dictNeighbours[vertex][0] in hamiltonian_cycle:
                vertex = cycle_H._dictNeighbours[vertex][1]
            else:
                vertex = cycle_H._dictNeighbours[vertex][0]
        hamiltonian_cycle.append(start_vertex)
        return hamiltonian_cycle, cost

