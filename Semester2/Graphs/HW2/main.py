from random import randint

from graph import UndirectedGraph, write_graph_to_file, read_graph_from_file


class UI:
    def __init__(self):
        self._graphs = []  # a list of graphs
        self._current = None  # the number of the graph in use

    def add_empty_graph(self):
        if self._current is None:
            self._current = 0
        graph = UndirectedGraph(0, 0)
        self._graphs.append(graph)
        self._current = len(self._graphs) - 1  # make the empty graph the current one

    def create_random_graph_ui(self):
        vertices = int(input("Enter the number of vertices: "))
        edges = int(input("Enter the number of edges: "))
        graph = self.generate_random(vertices,
                                     edges)  # generates a random graph with the given number of vertices and edges
        if self._current is None:
            self._current = 0
        self._graphs.append(graph)
        self._current = len(self._graphs) - 1  # make the generated graph the current graph

    def generate_random(self, vertices, edges):
        if edges > vertices * (vertices - 1) // 2:  # check if the numbers are valid
            raise ValueError("Too many edges!")
        graph = UndirectedGraph(vertices, 0)
        i = 0
        while i < edges:
            x = randint(0, vertices - 1)
            y = randint(0, vertices - 1)
            if graph.add_edge(x, y):  # if the edge is valid increase the count
                i += 1
        return graph

    def read_graph_from_file_ui(self):
        filename = input("Enter the name of the file: ")  # the name of the file to read from
        if self._current is None:
            self._current = 0
        graph = read_graph_from_file(filename)
        self._graphs.append(graph)
        self._current = len(self._graphs) - 1

    def write_graph_to_file_ui(self):
        current_graph = self._graphs[self._current]
        output_file = "output" + str(self._current) + ".txt"  # creating the name of the output file
        write_graph_to_file(current_graph, output_file)

    def switch_graph_ui(self):
        print("You are on the graph number: {}".format(self._current))
        print("Available graphs: 0 - {}".format(str(len(self._graphs) - 1)))
        number = int(input("Enter the graph number you want to switch to: "))  # the number of the graph to switch to
        if not 0 <= number < len(self._graphs):
            raise ValueError("Trying to switch to a non existing graph!")
        self._current = number

    def get_number_of_vertices_ui(self):
        print("The number of vertices is: {}.".format(self._graphs[self._current].number_of_vertices))

    def get_number_of_edges_ui(self):
        print("The number of edges is: {}.".format(self._graphs[self._current].number_of_edges))

    def list_all_bound(self):
        for x in self._graphs[self._current].parse_vertices():
            line = str(x) + " :"
            for y in self._graphs[self._current].parse_bound(x):
                line = line + " " + str(y)
            print(line)  # prints a list of vertices with the corresponding vertices that form an edge

    def list_bound(self):
        vertex = int(input("Enter the vertex: "))
        line = str(vertex) + " :"
        for y in self._graphs[self._current].parse_bound(vertex):
            line = line + " " + "({}, {})".format(str(vertex), str(y))
        print(line)  # prints the list of edges that contain the specified vertex

    def parse_all_vertices(self):
        for vertex in self._graphs[self._current].parse_vertices():
            print("{}".format(vertex))  # parse all the vertices

    def add_vertex_ui(self):
        vertex = int(input("Enter the new vertex: "))
        added = self._graphs[self._current].add_vertex(vertex)  # check if the vertex is valid and add it if it is
        if added:
            print("Vertex added successfully!")
        else:
            print("Cannot add this vertex, it already exists!")

    def delete_vertex_ui(self):
        vertex = int(input("Enter the vertex to be deleted: "))
        deleted = self._graphs[self._current].remove_vertex(
            vertex)  # check if the vertex is valid and delete it if it is
        if deleted:
            print("Vertex deleted successfully!")
        else:
            print("Cannot delete this vertex, it does not exist!")

    def add_edge_ui(self):
        print("Add an edge (an edge is (x, y))")
        vertex_x = int(input("Enter x = "))
        vertex_y = int(input("Enter y = "))
        added = self._graphs[self._current].add_edge(vertex_x,
                                                     vertex_y)  # check if the edge is valid and add it if it is
        if added:
            print("Edge added successfully!")
        else:
            print("Cannot add this edge!")

    def remove_edge_ui(self):
        print("Remove an edge (an edge is (x, y))")
        vertex_x = int(input("Enter x = "))
        vertex_y = int(input("Enter y = "))
        deleted = self._graphs[self._current].remove_edge(vertex_x,
                                                          vertex_y)  # check if the edge is valid and delete it if it is
        if deleted:
            print("Edge deleted successfully!")
        else:
            print("Cannot remove this edge, it does not exist!")

    def get_degree_ui(self):
        vertex = int(input("Enter the vertex:"))
        degree = self._graphs[self._current].degree(
            vertex)  # get the degree of a vertex; an invalid vertex will return -1
        if degree == -1:
            print("The vertex does not exist!")
        else:
            print("The in degree of the vertex {} is {}.".format(vertex, degree))

    def check_if_edge_ui(self):
        vertex_x = int(input("Enter x = "))
        vertex_y = int(input("Enter y = "))
        edge = self._graphs[self._current].find_if_edge(vertex_x, vertex_y)  # check if there is an edge
        if edge is True:
            print("({}, {}) is an edge!".format(vertex_x, vertex_y))
        else:
            print("({}, {}) is not an edge!".format(vertex_x, vertex_y))

    def copy_current_graph_ui(self):
        copy = self._graphs[self._current].make_copy()
        self._graphs.append(copy)  # make a copy of the current graph

    def find_connected_components_ui(self):
        all_connected = self._graphs[self._current].find_connected_components()  # find the connected components
        for index in range(len(all_connected)):
            print(all_connected[index])

    def print_menu(self):
        print("MENU:\n"
              "0. EXIT.\n"
              "1. Create a random graph with specified number of vertices and edges.\n"
              "2. Read the graph from a text file.\n"
              "3. Write the graph in a text file.\n"
              "4. Switch the graph.\n"
              "5. Get the number of vertices.\n"
              "6. Get the number of edges.\n"
              "7. List the bound edges of a vertex.\n"
              "8. List all the bound vertices.\n"
              "9. Add a vertex.\n"
              "10. Remove a vertex.\n"
              "11. Add an edge.\n"
              "12. Remove an edge.\n"
              "13. Get the degree of a vertex.\n"
              "14. Check if there is an edge between two given vertices.\n"
              "15. Make a copy of the graph.\n"
              "16. Add an empty graph.\n"
              "17. Parse all the vertices.\n"
              "18. Get the connected components using a breadth-first traversal.")

    def start(self):
        print("Welcome!")
        done = False
        self.add_empty_graph()
        print("The current graph is an empty graph!")
        command_dict = {"1": self.create_random_graph_ui, "2": self.read_graph_from_file_ui,
                        "3": self.write_graph_to_file_ui, "4": self.switch_graph_ui,
                        "5": self.get_number_of_vertices_ui, "6": self.get_number_of_edges_ui,
                        "7": self.list_bound, "8": self.list_all_bound,
                        "9": self.add_vertex_ui, "10": self.delete_vertex_ui,
                        "11": self.add_edge_ui, "12": self.remove_edge_ui,
                        "13": self.get_degree_ui, "14": self.check_if_edge_ui,
                        "15": self.copy_current_graph_ui, "16": self.add_empty_graph,
                        "17": self.parse_all_vertices, "18": self.find_connected_components_ui}
        while not done:  # continue until the user selects the exit option
            try:
                self.print_menu()
                option = input("Choose an option from the menu: \n")
                if option == "0":
                    done = True
                    print("Good bye!")
                elif option in command_dict:
                    command_dict[option]()
                else:
                    print("Bad input!\n")
            except ValueError as ve:
                print(str(ve))
            except FileNotFoundError as fnfe:
                print(str(fnfe).strip("[Errno 2] "))


UI().start()
