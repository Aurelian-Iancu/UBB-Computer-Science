"""
  Write non-UI functions below
"""


def create_participant(P1, P2, P3):
    """
    Function to create the results of a participant
    :param P1: The result of the first problem
    :param P2: The result of the second problem
    :param P3: The result of the third problem
    :return: The new participant, or None if the participant could not be created
    :except ValueError if P1, P2, P3 < 0 or P1, P2, P3 > 10
    """
    if P1 < 0 or P1 > 10:
        raise ValueError('The problem can be marked between 0 and 10')
    if P2 < 0 or P2 > 10:
        raise ValueError('The problem can be marked between 0 and 10')
    if P3 < 0 or P3 > 10:
        raise ValueError('The problem can be marked between 0 and 10')
    return [P1, P2, P3]


def test_create_participant():
    """
    Function to test the create_participant function
    :return: Nothing if the tests pass, AssertionError otherwise
    """
    assert create_participant(0, 1, 2) == [0, 1, 2]
    assert create_participant(5, 5, 10) == [5, 5, 10]
    try:
        assert create_participant(5, -1, 10) == [5, -1, 10]
    except ValueError:
        print("The problem has to be graded between 0 and 10")
    try:
        assert create_participant(10, 10, 11) == [10, 10, 11]
    except ValueError:
        print("The problem has to be graded between 0 and 10")


def init_list_of_participants():
    """
    Function that creates a list of participants
    :return: List of participants
    """
    return [create_participant(5, 6, 7), create_participant(8, 5, 9), create_participant(10, 10, 9), create_participant(2, 8, 6)
            , create_participant(3, 4, 4), create_participant(5, 5, 5), create_participant(10, 3, 8), create_participant(9, 9, 6)
            , create_participant(0, 5, 4), create_participant(1, 10, 10)]


def test_init_list_of_participants():
    """
    Function to test the init_list_of_participants function
    :return: Nothing if the tests pass, AssertionError otherwise
    """
    assert init_list_of_participants() == [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6], [3, 4, 4], [5, 5, 5], [10, 3, 8], [9, 9, 6], [0, 5, 4], [1, 10, 10]]


def average_score(participant):
    """
    In this function we compute the average score of a participant
    :param participant: a participant
    :return: the average score of a chosen participant
    """
    average = round((get_first_problem(participant) +
                    get_second_problem(participant) +
                    get_third_problem(participant)) / 3, 2)
    return average


def test_average_score():
    """
    In this function we the test_average_score function
    :return: Nothing if the tests pass, AssertionError otherwise
    """
    assert average_score([1, 2, 3]) == 2
    assert average_score([8, 5, 9]) == 7.33
    assert average_score([10, 10, 9]) == 9.67
    assert average_score([10, 10, 10]) == 10
    assert average_score([0, 0, 0]) == 0


def get_first_problem(participant):
    """
    Function to get the result of the participant's first problem
    :param participant: a participant
    :return: P1 - integer, the result of the participant's first problem
    """
    return participant[0]


def test_get_first_problem():
    """
    Function to test the get_first_problem function
    :return: Nothing if the tests pass, AssertionError otherwise
    """
    assert get_first_problem([1, 2, 3]) == 1


def get_second_problem(participant):
    """
    Function to get the result of the participant's first problem
    :param participant: a participant
    :return: P2 - integer, the result of the participant's second    problem
    """
    return participant[1]


def test_get_second_problem():
    """
    Function to test the get_second_problem function
    :return: Nothing if the tests pass, AssertionError otherwise
    """
    assert get_second_problem([1, 2, 3]) == 2


def get_third_problem(participant):
    """
    Function to get the result of the participant's first problem
    :param participant: a participant
    :return: P3 - integer, the result of the participant's third problem
    """
    return participant[2]


def test_get_third_problem():
    """
    Function to test the get_third_problem function
    :return: Nothing if the tests pass, AssertionError otherwise
    """
    assert get_third_problem([1, 2, 3]) == 3


def split_command_params(command):
    """
    Divide user command into command word and parameters
    :param command: User command
    :return: A list: [command word, command parameters]
    """
    #remove whitespace at beginning and end of command
    command = command.strip()
    aux = command.split(sep=' ', maxsplit=1)
    return [aux[0].strip().lower(), aux[1].strip().lower()] if len(aux) == 2 else [aux[0].strip().lower(), None]


def test_split_command_params():
    """
    Function to test the split_command_params function
    :return: Nothing if the tests pass, AssertionError otherwise
    """
    assert split_command_params("add 3 8 10") == ['add', '3 8 10']
    assert split_command_params("AdD 3 8 10") == ['add', '3 8 10']
    assert split_command_params("      ADD     3 8 10") == ['add', '3 8 10']
    assert split_command_params("insert 10 10 9 at 5") == ['insert', '10 10 9 at 5']
    assert split_command_params("inSert 10 10 9 at 5") == ['insert', '10 10 9 at 5']
    assert split_command_params("       insERT       10 10 9 at 5") == ['insert', '10 10 9 at 5']
    assert split_command_params("remove 1") == ['remove', '1']
    assert split_command_params("Remove 1") == ['remove', '1']
    assert split_command_params("       reMove          1") == ['remove', '1']
    assert split_command_params("remove 1 to 3") == ['remove', '1 to 3']
    assert split_command_params("REMove 1 to 3") == ['remove', '1 to 3']
    assert split_command_params("         remove         1 to 3") == ['remove', '1 to 3']
    assert split_command_params("replace 4 P2 with 5") == ['replace', '4 p2 with 5']
    assert split_command_params("REplace 4 P2 with 5") == ['replace', '4 p2 with 5']
    assert split_command_params("           replace       4 P2 with 5") == ['replace', '4 p2 with 5']
    assert split_command_params("list") == ['list', None]
    assert split_command_params("LIST") == ['list', None]
    assert split_command_params("   list      ") == ['list', None]
    assert split_command_params("list sorted") == ['list', 'sorted']
    assert split_command_params("LIST Sorted") == ['list', 'sorted']
    assert split_command_params("       list       sorted") == ['list', 'sorted']
    assert split_command_params("list < 4") == ['list', '< 4']
    assert split_command_params("LIST < 4") == ['list', '< 4']
    assert split_command_params("     list      < 4") == ['list', '< 4']
    assert split_command_params("exit") == ['exit', None]
    assert split_command_params("eXiT") == ['exit', None]
    assert split_command_params("    ExIt         ") == ['exit', None]


def is_string_at(string):
    """
    In this function we verify if a string is "at", otherwise we raise a ValueError
    :param string: a string
    :return: Nothing if the string is "at", ValueError otherwise
    """
    if string.lower() != "at":
        raise ValueError


def is_string_to(string):
    """
    In this function we verify if a string is "to", otherwise we raise a ValueError
    :param string: a string
    :return: Nothing if the string is "to", ValueError otherwise
    """
    if string.lower() != "to":
        raise ValueError


def is_string_with(string):
    """
    In this function we verify if a string is "with", otherwise we raise a ValueError
    :param string: a string
    :return: Nothing if the string is "with", ValueError otherwise
    """
    if string.lower() != "with":
        raise ValueError


def is_string_sorted(string):
    """
    In this function we verify if a string is "sorted", otherwise we raise a ValueError
    :param string: a string
    :return: Nothing if the string is "sorted", ValueError otherwise
    """
    if string.lower() != "sorted":
        raise ValueError


def is_problem_valid(problem):
    """
    In this function we verify if a problem is valid: the problem is marked between 0 and 10
    :param problem: a problem
    :return: Nothing if the problem is valid, ValueError otherwise
    """
    if problem < 0 or problem > 10:
        raise ValueError


def is_position_valid(position, list_of_participants):
    """
    In this function we verify if a position is valid: the position exists in list
    :param position: a position
    :param list_of_participants: the entire list of participants
    :return: Nothing if the position is valid, ValueError otherwise
    """
    if position < 0 or position > len(list_of_participants):
        raise ValueError


def are_all_problems_valid(participant):
    """
    In this function we verify if all the problems of a user are valid: they are marked between 0 and 10
    :param participant: a participant
    :return: Nothing if the problems are valid, ValueError otherwise
    """
    if len(participant) != 3:
        raise ValueError


def are_positions_valid(first_position, last_position):
    """
    In this function we verify if the first position is smaller than the last position
    :param first_position: first position
    :param last_position: last position
    :return: Nothing if the positions are valid, ValueError otherwise
    """
    if first_position > last_position:
        raise ValueError


def is_sign(sign):
    """
    In this function we verify if a string is <, > or =
    :param sign: a sign
    :return: Nothing if the sign is valid, ValueError otherwise
    """
    if sign != "<" and sign != ">" and sign != "=":
        raise ValueError


def is_string_problem(string):
    """
    In this function we verify if a string is P1, P2 or P3
    :param string: a string
    :return: Nothing if the sign is valid, ValueError otherwise
    """
    if string != "p1" and string != "p2" and string != "p3":
        raise ValueError


def add_participant_to_list(list_of_participants, command_params):
    """
    In this function we add a new participant to our list of participants at the end of the list
    :param list_of_participants: the list of participants
    :param command_params: the parameters of add command which are the results of the 3 problems
    :return: Nothing
    """
    copy = []
    participant = []
    params = command_params.split(" ")

    for param in params:
        copy.append(param.strip())

    try:
        P1 = int(get_first_problem(copy))
        P2 = int(get_second_problem(copy))
        P3 = int(get_third_problem(copy))
        participant.append(P1)
        participant.append(P2)
        participant.append(P3)
        for i in range(len(participant)):
            is_problem_valid(participant[i])
        are_all_problems_valid(participant)
        list_of_participants.append(participant)
    except ValueError:
        print("Invalid command!")


def insert_element_to_position(list_of_participants, command_params):
    """
    In this function we add a new participant to our list of participants at a given position
    :param list_of_participants: the list of participants
    :param command_params: the parameters of insert command which are the results of the 3 problems the string at and the position where you want to insert the participant
    :return: Nothing
    """
    copy = []
    participant = []
    params = command_params.split(" ")

    for param in params:
        copy.append(param.strip())

    try:
        P1 = int(get_first_problem(copy))
        P2 = int(get_second_problem(copy))
        P3 = int(get_third_problem(copy))
        participant.append(P1)
        participant.append(P2)
        participant.append(P3)
        is_string_at(copy[3])
        for i in range(len(participant)):
            is_problem_valid(participant[i])
        position = int(copy[4])
        is_position_valid(position, list_of_participants)
        are_all_problems_valid(participant)
        list_of_participants.insert(position, participant)
    except ValueError:
        print("Invalid command")


def remove_element_from_list(list_of_participants, command_params):
    """
    In this function we remove a participant from a given position by setting all his scores to 0
    :param list_of_participants: the list of participants
    :param command_params: the parameter of remove command which is the position you want to remove from the list
    :return: Nothing
    """
    copy = []
    params = command_params.split(" ")

    for param in params:
        copy.append(param.strip())

    try:
        position = int(copy[0])
        is_position_valid(position, list_of_participants)
        list_of_participants[position][0] = 0
        list_of_participants[position][1] = 0
        list_of_participants[position][2] = 0
    except ValueError:
        print("Invalid command")


def remove_more_elements_from_list(list_of_participants, command_params):
    """
    In this function we remove all the participants between 2 given positions by setting all their scores to 0
    :param list_of_participants: the list of participants
    :param command_params: the parameters of remove command which are the positions from where to where you want to remove
    :return: Nothing
    """
    copy = []
    params = command_params.split(" ")

    for param in params:
        copy.append(param.strip())

    try:
        first_position = int(copy[0])
        is_position_valid(first_position, list_of_participants)
        is_string_to(copy[1])
        last_position = int(copy[2])
        is_position_valid(last_position, list_of_participants)
        are_positions_valid(first_position, last_position)

        for i in range (first_position, last_position + 1):
            list_of_participants[i][0] = 0
            list_of_participants[i][1] = 0
            list_of_participants[i][2] = 0
    except (ValueError, IndexError):
        print("Invalid command")



def replace_element_in_list(list_of_participants, command_params):
    """
    In this funciton we replace the problem's score of choosen player
    :param list_of_participants: the list of participants
    :param command_params: parameters of replace command
    :return: Nothing
    """
    copy = []
    params = command_params.split(" ")

    for param in params:
        copy.append(param.strip())

    try:
        position = int(copy[0])
        is_position_valid(position, list_of_participants)
        problem = copy[1]
        is_string_problem(problem)
        is_string_with(copy[2])
        problem_value = int(copy[3])
        is_problem_valid(problem_value)
        if problem == "p1":
            list_of_participants[position][0] = problem_value
        elif problem == "p2":
            list_of_participants[position][1] = problem_value
        elif problem == "p3":
            list_of_participants[position][2] = problem_value
    except ValueError:
        print("Invalid command")


"""
  Write the command-driven UI below
"""


def print_all_participants(list_of_participants):
    """
    In this function we print on the screen all the participants
    :param list_of_participants: the list of participants
    :return: Nothing
    """
    print(list_of_participants)


def print_participants_sorted(list_of_participants, command_params):
    """
    In this function we print on the screen the participants sorted in decreasing order of average score
    :param list_of_participants: the list of participants
    :param command_params: the string "sorted"
    :return: Nothing
    """
    """
                    ASK THIS!!! ZIP AAAAAAAA
    average_list = create_average_list(list_of_participants)
    zipped_lists = zip(average_list, list_of_participants)
    sorted_zipped_lists = sorted(zipped_lists, reverse=True)
    sorted_list_of_participants = [element for _, element in sorted_zipped_lists]
    print(sorted_list_of_participants)
    """
    copy = command_params

    try:
        is_string_sorted(copy)
        copy_list_of_participants = list_of_participants.copy()
        copy_list_of_participants.sort(key=average_score, reverse=True)
        print(copy_list_of_participants)
    except ValueError:
        print("Invalid command")


def print_participants_by_rule(list_of_participants, command_params):
    """
    In this function we print on the screen the participant that respect a given rule
    :param list_of_participants: the list of participants
    :param command_params: list command params
    :return: Nothing
    """
    copy = []
    params = command_params.split(" ")
    print_list = []

    for param in params:
        copy.append(param.strip())

    try:
        sign = copy[0]
        is_sign(sign)
        average = int(copy[1])
        is_problem_valid(average)
        if sign == "<":
            for participant in list_of_participants:
                if average_score(participant) < average:
                    print_list.append(participant)
        elif sign == ">":
            for participant in list_of_participants:
                if average_score(participant) > average:
                    print_list.append(participant)
        elif sign == "=":
            for participant in list_of_participants:
                if average_score(participant) == average:
                    print_list.append(participant)
        print(print_list)
    except ValueError:
        print("Invalid command")




def print_menu():
    """
    In this function we print the commands the user can use
    :return: Nothing
    """
    print("              THE MENU OF COMMANDS IS:")
    print("add <P1 score> <P2 score> <P3 score> - ex:add 3 8 10")
    print("insert <P1 score> <P2 score> <P3 score> at <position> - ex:insert 10 10 9 at 5")
    print("remove <position> - ex:remove 1")
    print("remove <start position> to <end position> - ex:remove 1 to 3")
    print("replace <old score> <P1 | P2 | P3> with <new score> - ex:replace 4 P2 with 5")
    print("list - ex:list")
    print("list sorted - ex:list sorted")
    print("list [ < | = | > ] <score> - ex:list < 4 or list = 6")
    print("exit - ex:exit")
    print("")


def run_menu():
    """
    In this function we call the functions by the command word given by the user in an infinite loop, until the user wants to exit
    :return: Nothing
    """
    list_of_participants = init_list_of_participants()
    print_menu()

    while True:
        command = input("promp> ")
        command_word, command_params = split_command_params(command)

        if command_params != None:
            params = command_params.split(" ")

        try:
            if command_word == "add":
                add_participant_to_list(list_of_participants, command_params) #done!!!
            elif command_word == "insert":
                insert_element_to_position(list_of_participants, command_params) #MORE THAN DONE!!!!!
            elif command_word == "remove" and len(params) == 1: #done
                remove_element_from_list(list_of_participants, command_params)
            elif command_word == "remove" and len(params) == 3: #done
                remove_more_elements_from_list(list_of_participants, command_params)
            elif command_word == "replace":#
                replace_element_in_list(list_of_participants, command_params)
            elif command_word == "list" and command_params == None: #done
                print_all_participants(list_of_participants)
            elif command_word == "list" and len(params) == 1: # done
                print_participants_sorted(list_of_participants, command_params)
            elif command_word == "list" and len(params) == 2: #
                print_participants_by_rule(list_of_participants, command_params)
            elif command_word == "exit": #done!!!
                return
            else:
                print("Invalid command!")
        except (AttributeError, UnboundLocalError):
            print("Invalid command")


def start():
    list_of_participants = init_list_of_participants()
    run_menu()



start()


