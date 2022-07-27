import copy


class Graph:
    def __init__(self, no_of_vertices=0, no_of_edges=0):
        self.__no_of_vertices = no_of_vertices
        self.__no_of_edges = no_of_edges
        self.__dictionary_in = {}
        self.__dictionary_out = {}
        self.__activities_duration = {}

    def initialise_in_and_out_for_random(self):
        for i in range(self.__no_of_vertices):
            self.__dictionary_in[i] = []
            self.__dictionary_out[i] = []

    @property
    def no_of_edges(self):
        return self.__no_of_edges

    @property
    def no_of_vertices(self):
        return self.__no_of_vertices

    @property
    def dictionary_in(self):
        return self.__dictionary_in

    @property
    def dictionary_out(self):
        return self.__dictionary_out

    @property
    def activities_duration(self):
        return self.__activities_duration

    def set_activity_duration(self, x, d):
        self.__activities_duration[x] = d

    def valid_vertex(self, x):
        return x in self.__dictionary_in and x in self.__dictionary_out

    def check_edge(self, x, y):
        return self.valid_vertex(x) and self.valid_vertex(y) and (x in self.__dictionary_in[y])

    def get_in_degree(self, x):
        if not self.valid_vertex(x):
            raise ValueError("Vertex not found")
        return len(self.__dictionary_in[x])

    def get_out_degree(self, x):
        if not self.valid_vertex(x):
            raise ValueError("Vertex not found")
        return len(self.__dictionary_out[x])

    def parse_vertices(self):
        sol = []
        for vertex in sorted(list(self.__dictionary_in)):
            sol.append(vertex)
        return sol

    def parse_inbound_edges(self, x):
        if not self.valid_vertex(x):
            raise ValueError("Vertex not found")
        sol = []
        for y in self.__dictionary_in[x]:
            sol.append(y)
        return sol

    def parse_outbound_edges(self, x):
        if not self.valid_vertex(x):
            raise ValueError("Vertex not found")
        sol = []
        for y in self.__dictionary_out[x]:
            sol.append(y)
        return sol

    def add_vertex(self, x):
        if self.valid_vertex(x):
            raise ValueError("The vertex already exists")
        # initialise the inbound and outbound neighbours
        self.__dictionary_in[x] = []
        self.__dictionary_out[x] = []
        self.__no_of_vertices += 1

    def add_vertex_from_file(self, x):
        self.__dictionary_in[x] = []
        self.__dictionary_out[x] = []

    def remove_vertex(self, x):
        if not self.valid_vertex(x):
            raise ValueError("The vertex doesn't belong to the graph")
        # remove x as a neighbour
        for y in self.__dictionary_in[x]:
            self.__dictionary_out[y].remove(x)
            self.__no_of_edges -= 1
        for y in self.__dictionary_out[x]:
            self.__dictionary_in[y].remove(x)
            self.__no_of_edges -= 1
        # pop x from inbound and outbound neighbours
        self.__dictionary_in.pop(x)
        self.__dictionary_out.pop(x)
        self.__no_of_vertices -= 1

    def add_edge(self, x, y):
        # check if x and y are valid vertices
        if not self.valid_vertex(x) or not self.valid_vertex(y):
            raise ValueError("Vertex not found")
        # check if the edge doesn't already exist
        if self.check_edge(x, y):
            raise ValueError("The edge already exists")
        self.__dictionary_in[y].append(x)
        self.__dictionary_out[x].append(y)
        self.__no_of_edges += 1

    def add_edge_from_file(self, x, y):
        if not self.valid_vertex(x):
            self.add_vertex_from_file(x)
        if not self.valid_vertex(y):
            self.add_vertex_from_file(y)
        self.__dictionary_in[y].append(x)
        self.__dictionary_out[x].append(y)

    def remove_edge(self, x, y):
        # check if the edge exists
        if self.check_edge(x, y) is None:
            raise ValueError("The edge doesn't exist")
        self.__dictionary_in[y].remove(x)
        self.__dictionary_out[x].remove(y)
        self.__no_of_edges -= 1

    def make_copy(self):
        return copy.deepcopy(self)

    def topological_sort_dfs(self, x, sorted_list, fully_processed, in_process):
        in_process.add(x)               # we want to do x
        for inbound_neighbour in self.parse_inbound_edges(x):   # we need to do every prerequisite of x
            if inbound_neighbour in in_process:    # doing x requires doing x => we have a cycle
                return False
            else:
                if inbound_neighbour not in fully_processed:    # if the activity was not done yet
                    ok = self.topological_sort_dfs(inbound_neighbour, sorted_list, fully_processed, in_process)
                    if not ok:    # in case we reached a cycle, return false every running stack
                        return False
        in_process.remove(x)    # we finished processing x
        sorted_list.append(x)   # now we can add it to the sorted list
        fully_processed.add(x)  # it is fully processed
        return True

    def dag(self):
        sorted_list = []    # the list containing the topological order, which is not unique
        fully_processed = set()     # store the elements already processed
        in_process = set()    # a set used for processing a current activity
        for vertex in self.parse_vertices():
            if vertex not in fully_processed:   # for every activity that is not yet processed
                ok = self.topological_sort_dfs(vertex, sorted_list, fully_processed, in_process)
                if not ok:   # in case we have a cycle => we do not have a Directed Acyclic Graph
                    return []
        return sorted_list

    def compute_times(self, sorted_list):
        first = -1
        last = len(sorted_list)
        infinity = 999999

        # add the fictive nodes: first and last
        self.add_vertex(first)
        self.add_vertex(last)

        # insert the first fictive activity
        sorted_list.insert(0, first)
        self.__activities_duration[first] = 0

        # add the edges between the first and the vertices with no predecessor
        for vertex in self.parse_vertices():
            if self.get_in_degree(vertex) == 0 and vertex != first and vertex != last:
                self.add_edge(first, vertex)

        # insert the fictive last activity
        sorted_list.append(last)
        self.__activities_duration[last] = 0

        # add the edges between the vertices with no successor and the last
        for vertex in self.parse_vertices():
            if self.get_out_degree(vertex) == 0 and vertex != first and vertex != last:
                self.add_edge(vertex, last)

        # initialise the dictionaries for earliest_start_time and earliest_end_time
        earliest_start_time = {}
        earliest_end_time = {}
        for vertex in self.parse_vertices():
            earliest_start_time[vertex] = 0
            earliest_end_time[vertex] = 0

        # initialise the dictionaries for latest_start_time and latest_end_time
        latest_start_time = {}
        latest_end_time = {}
        for vertex in self.parse_vertices():
            latest_start_time[vertex] = infinity
            latest_end_time[vertex] = infinity

        # compute the earliest start and end time for each activity
        for i in range(1, len(sorted_list)):
            # take as earliest start time the maximum earliest end time of the predecessors
            for predecessor in self.parse_inbound_edges(sorted_list[i]):
                earliest_start_time[sorted_list[i]] = max(earliest_start_time[sorted_list[i]], earliest_end_time[predecessor])
            # the earliest end time will be the earliest start time + duration of activity
            earliest_end_time[sorted_list[i]] = earliest_start_time[sorted_list[i]] + self.__activities_duration[sorted_list[i]]

        # compute the latest start and end time for each activity
        latest_end_time[last] = earliest_end_time[last]
        latest_start_time[last] = latest_end_time[last] - self.__activities_duration[last]
        latest_start_time[first] = 0
        latest_end_time[first] = 0

        # compute the latest start and end time of each activity
        for i in range(len(sorted_list) - 1, 0, -1):
            # take as latest end time the minimum of latest start time of the successors
            for successor in self.parse_outbound_edges(sorted_list[i]):
                latest_end_time[sorted_list[i]] = min(latest_end_time[sorted_list[i]], latest_start_time[successor])
            # the latest start time will be the latest end time - duration of activity
            latest_start_time[sorted_list[i]] = latest_end_time[sorted_list[i]] - self.__activities_duration[sorted_list[i]]

        # remove the fictive nodes
        sorted_list.pop(0)
        sorted_list.pop()
        self.remove_vertex(first)
        self.remove_vertex(last)

        # determine the critical activities
        critical_activities = []
        for activity in sorted_list:
            if earliest_start_time[activity] == latest_start_time[activity]:
                critical_activities.append(activity)

        return earliest_start_time, earliest_end_time, latest_start_time, latest_end_time, critical_activities

    def activities_scheduling(self):
        sorted_list = self.dag()
        if len(sorted_list) == 0:
            raise ValueError("The graph is not directed acyclic graph")
        print(f"Topological sorting: {sorted_list}")
        earliest_start_time, earliest_end_time, latest_start_time, latest_end_time, critical_activities = self.compute_times(sorted_list)
        for vertex in sorted_list:
            print(f"Activity {vertex}: earliest starting time: {earliest_start_time[vertex]} - "
                  f"{earliest_end_time[vertex]} | "
                  f"latest starting time: {latest_start_time[vertex]} - "
                  f"{latest_end_time[vertex]}")
        print(f"Total time of the project: {earliest_start_time[len(sorted_list)]}")
        print("Critical activities: ", end="")
        for activity in critical_activities:
            print(activity, end=" ")
        print("")


def read_from_file(path):
    with open(path, "r") as file_pointer:
        lines = file_pointer.readlines()
        if lines[0] == "The graph is empty or couldn't be generated":
            return Graph(0, 0)
        first_line_tokens = lines[0].split()
        no_of_vertices = int(first_line_tokens[0].strip())
        no_of_edges = int(first_line_tokens[1].strip())
        graph = Graph(no_of_vertices, no_of_edges)
        # now add the edges
        for i in range(1, len(lines)):
            line_tokens = lines[i].split()
            if len(line_tokens) == 0:
                break
            if len(line_tokens) == 1:
                graph.add_vertex_from_file(int(line_tokens[0].strip()))
            else:
                graph.add_edge_from_file(int(line_tokens[0].strip()), int(line_tokens[1].strip()))
        return graph


def read_from_activities_file(path):
    with open(path, "r") as file_pointer:
        lines = file_pointer.readlines()
        graph = Graph(0, 0)
        # now add the edges
        for i in range(0, len(lines)):
            line_tokens = lines[i].split()
            if len(line_tokens) == 0:
                break
            node = int(line_tokens[0])
            time = int(line_tokens[1])
            if not graph.valid_vertex(node):
                graph.add_vertex(node)
            graph.set_activity_duration(node, time)
            if line_tokens[2] == "-":
                continue
            neighbours_tokens = line_tokens[2].split(",")
            neighbours = [int(el) for el in neighbours_tokens]
            for el in neighbours:
                if el != "-":
                    if not graph.valid_vertex(el):
                        graph.add_vertex(el)
                    graph.add_edge(el, node)
        return graph


def write_to_file(graph, path):
    with open(path, "w") as file_pointer:
        if graph.no_of_vertices == 0 and graph.no_of_edges == 0:
            file_pointer.write("The graph is empty or couldn't be generated")
            return
        file_pointer.write(f"{graph.no_of_vertices} {graph.no_of_edges}\n")
        # write isolated vertices
        for x in graph.parse_vertices():
            if graph.get_in_degree(x) == 0 and graph.get_out_degree(x) == 0:
                file_pointer.write(f"{x}\n")
        for edge in graph.dictionary_cost:
            file_pointer.write(f"{edge[0]} {edge[1]} {graph.dictionary_cost[edge]}\n")
