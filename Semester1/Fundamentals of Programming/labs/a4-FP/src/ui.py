"""
  User interface module
"""
from functions import *


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
    is_string_sorted(copy)
    copy_list_of_participants = list_of_participants.copy()
    copy_list_of_participants.sort(key=average_score, reverse=True)
    print(copy_list_of_participants)


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


def print_average_score(list_of_participants, command_params):
    """
    In this function we print the average score of the players between 2 chosen positions
    :param list_of_participants: the list of participants
    :param command_params: the avg command parameters which are the 2 positions and the word to
    :return: Nothing
    """
    copy = []
    params = command_params.split(" ")
    sum = 0
    nr = 0

    for param in params:
        copy.append(param.strip())

    first_position = int(copy[0])
    is_position_valid(first_position, list_of_participants)
    is_string_to(copy[1])
    last_position = int(copy[2])
    is_position_valid(last_position, list_of_participants)

    for i in range(first_position, last_position + 1):
        sum = sum + average_score(list_of_participants[i])
        nr = nr + 1
        print("The average score of player " + str(i) + " is: " + str(average_score(list_of_participants[i])))

    result = sum / nr
    print("The average score of the players is: " + str(round(result, 2)))


def print_lowest_score(list_of_participants, command_params):
    """
    In this function we print the lowest score of a player between 2 chosen positions
    :param list_of_participants: the list of participants
    :param command_params: the min command parameters which are the 2 positions and the word to
    :return: Nothing
    """
    copy = []
    params = command_params.split(" ")

    for param in params:
        copy.append(param.strip())

    first_position = int(copy[0])
    is_position_valid(first_position, list_of_participants)
    is_string_to(copy[1])
    last_position = int(copy[2])
    is_position_valid(last_position, list_of_participants)

    minimum = get_lowest_score(list_of_participants, first_position, last_position)
    print(minimum)


def print_top_players(list_of_participants, command_params):
    """
    In this function we print the top players by their average scores
    :param list_of_participants: the list of participants
    :param command_params: the top command parameters for len(command_params) = 1
    :return: Nothing
    """
    copy = []
    params = command_params.split(" ")

    for param in params:
        copy.append(param.strip())

    position = int(copy[0])
    is_position_valid(position, list_of_participants)
    copy_list_of_participants = list_of_participants.copy()
    copy_list_of_participants.sort(key=average_score, reverse=True)

    for i in range(0, position):
        print(copy_list_of_participants[i])


def print_top_by_problem_result(list_of_participants, command_params):
    """
    In this function we print the top players by a score of a problem
    :param list_of_participants: the list of participants
    :param command_params: the top command parameters for len(command_params) = 2
    :return: Nothing
    """
    copy = []
    params = command_params.split(" ")

    for param in params:
        copy.append(param.strip())

    position = int(copy[0])
    is_position_valid(position, list_of_participants)
    problem = copy[1]
    is_string_problem(problem)
    copy_list_of_participants = list_of_participants.copy()

    if problem == "p1":
        copy_list_of_participants.sort(key=get_first_problem, reverse=True)
        for i in range(0, position):
            print(copy_list_of_participants[i])
    elif problem == "p2":
        copy_list_of_participants.sort(key=get_second_problem, reverse=True)
        for i in range(0, position):
            print(copy_list_of_participants[i])
    elif problem == "p3":
        copy_list_of_participants.sort(key=get_third_problem, reverse=True)
        for i in range(0, position):
            print(copy_list_of_participants[i])


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
    print("avg <start position> to <end position> - ex: avg 1 to 5")
    print("min <start position> to <end position> - ex: min 2 to 7")
    print("top <number> -ex: top 3")
    print("top <number> <P1 | P2 | P3> -ex: top 4 P3")
    print("remove [ < | = | > ] <score> -ex: remove < 70(7.0) or remove < 89(8.9)")
    print("undo -ex:undo")
    print("exit - ex:exit")
    print("")

def run_menu():
    """
    In this function we call the functions by the command word given by the user in an infinite loop, until the user wants to exit
    :return: Nothing
    """
    list_of_participants = init_list_of_participants()
    print_menu()
    history = []
    while True:
        command = input("prompt> ")
        command_word, command_params = split_command_params(command)

        if command_params != None:
            params = command_params.split(" ")

        try:
            if command_word == "add":
                add_participant_to_list(list_of_participants, command_params, history)
            elif command_word == "insert":
                insert_element_to_position(list_of_participants, command_params, history)
            elif command_word == "remove" and len(params) == 1:
                remove_element_from_list(list_of_participants, command_params, history)
            elif command_word == "remove" and len(params) == 3:
                remove_more_elements_by_positions(list_of_participants, command_params, history)
            elif command_word == "replace":
                replace_element_in_list(list_of_participants, command_params, history)
            elif command_word == "list" and command_params == None:
                print_all_participants(list_of_participants)
            elif command_word == "list" and len(params) == 1:
                print_participants_sorted(list_of_participants, command_params)
            elif command_word == "list" and len(params) == 2:
                print_participants_by_rule(list_of_participants, command_params)
            elif command_word == "avg":
                print_average_score(list_of_participants, command_params)
            elif command_word == "min":
                print_lowest_score(list_of_participants, command_params)
            elif command_word == "top" and len(params) == 1:
                print_top_players(list_of_participants, command_params)
            elif command_word == "top" and len(params) == 2:
                print_top_by_problem_result(list_of_participants, command_params)
            elif command_word == "remove" and len(params) == 2:
                remove_more_elements_by_rule(list_of_participants, command_params, history)
            elif command_word == "undo":
                undo(list_of_participants, history)
            elif command_word == "exit":
                return
            else:
                print("Invalid command!")
        except (AttributeError, UnboundLocalError, ValueError, IndexError):
            print("Invalid command")