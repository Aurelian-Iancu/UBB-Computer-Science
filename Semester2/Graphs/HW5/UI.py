from UndirectedGraph import UndirectedGraph
from Service import Service
from MyExceptions import GraphExceptions


class UI:
    def __init__(self, service):
        self._commands = {"1": self.__ui_read_from_a_file, "2": self.__ui_create_random_graph,
                          "3": self.__ui_get_number_of_vertices,
                          "4": self.__ui_parse_set_of_vertices, "5": self.__ui_is_edge,
                          "6":self.__ui_get_degree_of_vertex,
                          "7":self.__ui_iterate_over_edges,
                          "9":self.__ui_get_edge_cost, "10":self.__ui_change_edge_cost, "11":self.__ui_add_an_edge,
                          "12":self.__ui_remove_edge, "13":self.__ui_add_vertex, "14":self.__ui_remove_vertex,
                          "15":self.__ui_write_the_graph_in_a_textfile, "16":self.__ui_copy_graph,
                          "17": self.__ui_change_current_graph, "18": self.__ui_get_hamiltonian_cycle}
        self._service = service

    def __ui_read_from_a_file(self):
        filename = input("Enter filename for the graph: ")
        graph_name = input("Enter a name for the graph: ")
        try:
            self._service.read_graph_from_file(filename, graph_name)
        except FileNotFoundError:
            print("Name of file is wrong! Try again.")
        except GraphExceptions as e:
            print(e)

    def __ui_create_random_graph(self):
        try:
            vertices_number = int(input("Enter the number of vertices: "))
            edges_number = int(input("Enter the number of edges: "))
            graph_name = input("Enter a name for the graph: ")
            self._service.create_random_graph(vertices_number, edges_number, graph_name)
        except ValueError:
            print("Wrong input!")
        except GraphExceptions as e:
            print(e)

    def __ui_write_the_graph_in_a_textfile(self):
        if self._service.service_get_number_of_vertices == 0:
            print ("You must add or create a random graph.")
        else:
            filename = input("Enter filename: ")
            try:
                self._service.write_graph_to_file(filename)
            except FileNotFoundError:
                print("Name of file is wrong! Try again.")

    def __ui_get_number_of_vertices(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            print("The number of vertices is: ",  vertices_number)

    def __ui_parse_set_of_vertices(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            print("The vertices are: ")
            for vertex in self._service.service_get_iterable_of_vertices():
                print(vertex)

    def __ui_is_edge(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                source_vertex = int(input("Enter source vertex: "))
                destination_vertex = int(input("Enter destination vertex: "))
                if self._service.service_check_if_edge_exists(source_vertex, destination_vertex) is True:
                    print("There is an edge from vertex ", source_vertex, " to vertex ", destination_vertex)
                else:
                    print("There is NO edge from vertex ", source_vertex, " to vertex ", destination_vertex)
            except GraphExceptions as e:
                print (e)
            except ValueError:
                print("Wrong input!")

    def __ui_get_degree_of_vertex(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                vertex = int(input("Enter the vertex: "))
                result = self._service.get_degree_of_vertex(vertex)
                print("The degree of the vertex ", vertex, "is: ", result)
            except ValueError:
                print("Invalid input!")
            except GraphExceptions as e:
                print(e)

    def __ui_iterate_over_edges(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                vertex = int(input("Enter the vertex: "))
                print("The edges of the vertex ", vertex, " are: ")
                empty = True
                for destination_vertex in self._service.service_get_iterable_of_edges(vertex):
                    print("Edge: ", vertex, " -> ", destination_vertex)
                    empty = False
                if empty:
                    print("The vertex has no edges.")
            except ValueError:
                print("Invalid input!")
            except GraphExceptions as e:
                print(e)

    def __ui_get_edge_cost(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                source_vertex = int(input("Enter one vertex: "))
                destination_vertex = int(input("Enter second vertex: "))
                cost = self._service.service_get_edge_cost(source_vertex, destination_vertex)
                print("The integer attached (the cost) to the edge ", source_vertex, " -> ", destination_vertex, " is: ", cost)
            except GraphExceptions as e:
                print (e)
            except ValueError:
                print("Wrong input!")

    def __ui_change_edge_cost(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                source_vertex = int(input("Enter one vertex: "))
                destination_vertex = int(input("Enter second vertex: "))
                cost = int(input("Enter new integer for the specified edge: "))
                self._service.service_change_edge_cost(source_vertex, destination_vertex, cost)
            except GraphExceptions as e:
                print (e)
            except ValueError:
                print("Wrong input!")

    def __ui_add_an_edge(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                source_vertex = int(input("Enter one vertex: "))
                destination_vertex = int(input("Enter second vertex: "))
                cost = int(input("Enter new integer for the specified edge: "))
                self._service.service_add_edge(source_vertex, destination_vertex, cost)
            except GraphExceptions as e:
                print(e)
            except ValueError:
                print("Wrong input!")

    def __ui_remove_edge(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                source_vertex = int(input("Enter one vertex: "))
                destination_vertex = int(input("Enter second vertex: "))
                self._service.service_remove_edge(source_vertex, destination_vertex)
            except GraphExceptions as e:
                print(e)
            except ValueError:
                print("Wrong input!")

    def __ui_remove_vertex(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                vertex = int(input("Enter vertex: "))
                self._service.service_remove_vertex(vertex)
            except GraphExceptions as e:
                print(e)
            except ValueError:
                print("Wrong input!")

    def __ui_add_vertex(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                vertex = int(input("Enter vertex: "))
                self._service.service_add_vertex(vertex)
            except GraphExceptions as e:
                print(e)
            except ValueError:
                print("Wrong input!")

    def __ui_copy_graph(self):
        graph_name = input("Enter a name for the graph: ")
        copy_of_the_graph = self._service.copy_graph(graph_name)
        print("The copy was made.")
        print("Below is the list of the graphs vertices so you can see that it's an accurate copy of the original graph.")
        for vertex in copy_of_the_graph.get_iterable_of_vertices():
            print(vertex)

    def __ui_change_current_graph(self):
        graphs_names_list = self._service.get_graphs_name_list()
        print("The names of the existing graphs are: ")
        for name in graphs_names_list:
            print(name)
        graph_name = input("Enter the name of the graph that you want to use: ")
        try:
            self._service.change_the_current_graph(graph_name)
            print("Current graph is the ", graph_name, " graph.")
        except GraphExceptions as e:
            print(e)

    def __ui_get_hamiltonian_cycle(self):
        vertices_number = self._service.service_get_number_of_vertices()
        if vertices_number == 0:
            print("The graph is empty.")
        else:
            try:
                cycle, cost = self._service.get_hamiltonian_cycle()
                print("The hamiltonian cycle has the cost: ", cost)
                i = 0
                while i < len(cycle) - 1:
                    print(cycle[i], "-> ", end='')
                    i += 1
                print(cycle[i])
                print()
            except GraphExceptions as e:
                print(e)


    def print_commands(self):
        print("\n"
              "0: Stop app!\n"
              "1: Read the graph from a file.\n"
              "2: Generate a random graph.\n"
              "3: Show number of vertices.\n"
              "4: Parse the set of vertices.\n"
              "5: Check if there is an edge between two vertices.\n"
              "6: Get the degree of a vertex.\n"
              "7: Parse the set of edges of a specified vertex.\n"
              "9: Retrieve the information (the integer) attached to a specified edge.\n"
              "10: Change the information (the integer) attached to a specified edge.\n"
              "11: Add a new edge.\n"
              "12: Remove an edge.\n"
              "13: Add a new vertex.\n"
              "14: Remove a vertex.\n"
              "15: Write the graph in a file.\n"
              "16: Copy the graph.\n"
              "17: Change the graph that you are now doing operations on.\n"
              "18: Get a hamiltonian cycle.")

    def run_app(self):
        while True:
            self.print_commands()
            command = input("Enter command: ")
            if command == "0":
                break
            elif command not in ["1", "2", "3", "4", "5", "6", "7", "9", "10",
                                 "11", "12", "13", "14", "15", "16", "17", "18"]:
                print("Wrong command!")
            else:
                self._commands[command]()