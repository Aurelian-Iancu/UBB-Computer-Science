import random

from graph import Graph, read_from_file, write_to_file, read_from_activities_file


class Console:
    def __init__(self):
        self.__graph = Graph(0, 0)

    def generate_random_graph(self):
        no_of_vertices = int(input("number of vertices: "))
        no_of_edges = int(input("number of edges: "))
        if no_of_edges > no_of_vertices * no_of_vertices:
            self.__graph = Graph(0, 0)
            raise ValueError(f"the maximum number of edges in a graph with {no_of_vertices} vertices is "
                             f"{no_of_vertices * no_of_vertices}")
        graph = Graph(no_of_vertices, 0)
        graph.initialise_in_and_out_for_random()
        while graph.no_of_edges < no_of_edges:
            x = random.randint(0, no_of_vertices - 1)
            y = random.randint(0, no_of_vertices - 1)
            if x == y:
                continue
            if not graph.check_edge(x, y):
                graph.add_edge(x, y)
        self.__graph = graph

    def get_graph_from_file(self):
        path = input("path to the file: ")
        self.__graph = read_from_file(path)

    def get_graph_from_activities_file(self):
        path = input("path to the file: ")
        self.__graph = read_from_activities_file(path)

    def push_graph_to_file(self):
        path = input("path to the file: ")
        write_to_file(self.__graph, path)

    def get_number_of_vertices(self):
        print(f"number of vertices: {self.__graph.no_of_vertices}")

    def get_number_of_edges(self):
        print(f"number of edges: {self.__graph.no_of_edges}")

    def get_the_vertices(self):
        for vertex in self.__graph.parse_vertices():
            print(vertex, end=" ")
        print()

    @staticmethod
    def read_edge():
        print("edge x -> y")
        x = int(input("x: "))
        y = int(input("y: "))
        return x, y

    def test_edge(self):
        x, y = Console.read_edge()
        if self.__graph.check_edge(x, y):
            print(f"{x} -> {y} exists")
        else:
            print("edge not found")

    def get_in_degree_of_vertex(self):
        vertex = int(input("vertex: "))
        print(f"in degree of {vertex}: {self.__graph.get_in_degree(vertex)}")

    def get_out_degree_of_vertex(self):
        vertex = int(input("vertex: "))
        print(f"out degree of {vertex}: {self.__graph.get_out_degree(vertex)}")

    def get_inbound_edges(self):
        vertex = int(input("vertex: "))
        for x in self.__graph.parse_inbound_edges(vertex):
            print(f"({x}, {vertex})", end=" ")
        print()

    def get_outbound_edges(self):
        vertex = int(input("vertex: "))
        for x in self.__graph.parse_outbound_edges(vertex):
            print(f"({vertex}, {x})", end=" ")
        print()

    def add_vertex_to_graph(self):
        vertex = int(input("new vertex: "))
        self.__graph.add_vertex(vertex)

    def remove_vertex_from_graph(self):
        vertex = int(input("vertex to remove: "))
        self.__graph.remove_vertex(vertex)

    def add_edge_to_graph(self):
        x, y = Console.read_edge()
        self.__graph.add_edge(x, y)

    def remove_edge_from_graph(self):
        x, y = Console.read_edge()
        self.__graph.remove_edge(x, y)

    def get_copy(self):
        return self.__graph.make_copy()

    def parse_graph(self):
        for x in sorted(self.__graph.parse_vertices()):
            print(f"{x}: ", end="")
            for y in sorted(self.__graph.parse_outbound_edges(x)):
                print(f"{y} ", end="")
            print()

    def print_topological_sort_result(self):
        print(self.__graph.dag())

    def show_times(self):
        self.__graph.activities_scheduling()

    @staticmethod
    def print_menu():
        print("\n"
              "0. EXIT\n"
              "1. Generate a random graph\n"
              "2. Read the graph from a file\n"
              "3. Write the graph to a file\n"
              "4. Get the number of vertices\n"
              "5. Get the number of edges\n"
              "6. Get the in degree of a vertex\n"
              "7. Get the out degree of a vertex\n"
              "8. List the inbound edges of a vertex\n"
              "9. List the outbound edges of a vertex\n"
              "10. List the vertices\n"
              "11. Edge information\n"
              "12. Add vertex\n"
              "13. Remove vertex\n"
              "14. Add edge\n"
              "15. Remove edge\n"
              "16. Parse graph\n"
              "17. Read from activities file\n"
              "18. Do a topological sort\n"
              "19. Show times\n")

    @staticmethod
    def read_command():
        command = int(input("command: "))
        return command

    def start(self):
        print("Initially the graph contains nothing...")
        commands = {
            1: self.generate_random_graph,
            2: self.get_graph_from_file,
            3: self.push_graph_to_file,
            4: self.get_number_of_vertices,
            5: self.get_number_of_edges,
            6: self.get_in_degree_of_vertex,
            7: self.get_out_degree_of_vertex,
            8: self.get_inbound_edges,
            9: self.get_outbound_edges,
            10: self.get_the_vertices,
            11: self.test_edge,
            12: self.add_vertex_to_graph,
            13: self.remove_vertex_from_graph,
            14: self.add_edge_to_graph,
            15: self.remove_edge_from_graph,
            16: self.parse_graph,
            17: self.get_graph_from_activities_file,
            18: self.print_topological_sort_result,
            19: self.show_times
        }
        while True:
            try:
                Console.print_menu()
                command = Console.read_command()
                if command == 0:
                    return
                commands[command]()
            except Exception as e:
                print(str(e))
