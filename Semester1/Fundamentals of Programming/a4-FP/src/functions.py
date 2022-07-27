"""
  Program functionalities module
"""
from ui import *


def create_participant(P1, P2, P3):#tested
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


def init_list_of_participants():#tested
    """
    Function that creates a list of participants
    :return: List of participants
    """
    return [create_participant(5, 6, 7), create_participant(8, 5, 9), create_participant(10, 10, 9), create_participant(2, 8, 6)
            , create_participant(3, 4, 4), create_participant(5, 5, 5), create_participant(10, 3, 8), create_participant(9, 9, 6)
            , create_participant(0, 5, 4), create_participant(1, 10, 10)]


def average_score(participant):#tested
    """
    In this function we compute the average score of a participant
    :param participant: a participant
    :return: the average score of a chosen participant
    """
    average = round((get_first_problem(participant) +
                    get_second_problem(participant) +
                    get_third_problem(participant)) / 3, 2)
    return average


def get_first_problem(participant):#tested
    """
    Function to get the result of the participant's first problem
    :param participant: a participant
    :return: P1 - integer, the result of the participant's first problem
    """
    return participant[0]


def get_second_problem(participant):#tested
    """
    Function to get the result of the participant's first problem
    :param participant: a participant
    :return: P2 - integer, the result of the participant's second    problem
    """
    return participant[1]


def get_third_problem(participant):#tested
    """
    Function to get the result of the participant's first problem
    :param participant: a participant
    :return: P3 - integer, the result of the participant's third problem
    """
    return participant[2]


def get_lowest_score(list_of_participants, first_position, last_position):#tested
    """
    Function to get the lowest average score from a list
    :param list_of_participants: the list of participants
    :param first_position: the first position from where you want to find the minimum
    :param last_position: the last position you want to check for the minimum
    :return: the minimum from the list between the chosen positions
    """
    minimum = 11

    for i in range(first_position, last_position + 1):
        if min(minimum, average_score(list_of_participants[i])) < minimum:
            minimum = min(minimum, average_score(list_of_participants[i]))

    return minimum


def set_participant_0(list_of_participants, position):
    """
    In this function we set the scores of a participant to 0
    :param list_of_participants: the list of participants
    :param position: a position
    :return: Nothing
    """
    new_list = [0, 0, 0]
    list_of_participants[position] = new_list


def set_first_problem(list_of_participants, value, position):
    """
    In this function we set the value of the first score with a value
    :param list_of_participants: the list of participants
    :param value: a value
    :param position: a position
    :return: Nothing
    """
    new_list = [value, list_of_participants[position][1], list_of_participants[position][2]]
    list_of_participants[position] = new_list


def set_second_problem(list_of_participants, value, position):
    """
    In this function we set the value of the second score with a value
    :param list_of_participants: the list of participants
    :param value: a value
    :param position: a position
    :return: Nothing
    """
    new_list = [list_of_participants[position][0], value, list_of_participants[position][2]]
    list_of_participants[position] = new_list


def set_third_problem(list_of_participants, value, position):
    """
    In this function we set the value of the third score with a value
    :param list_of_participants: the list of participants
    :param value: a value
    :param position: a position
    :return: Nothing
    """
    new_list = [list_of_participants[position][0] , list_of_participants[position][1], value]
    list_of_participants[position] = new_list


def split_command_params(command):#tested
    """
    Divide user command into command word and parameters
    :param command: User command
    :return: A list: [command word, command parameters]
    """
    #remove whitespace at beginning and end of command
    command = command.strip()
    aux = command.split(sep=' ', maxsplit=1)
    return [aux[0].strip().lower(), aux[1].strip().lower()] if len(aux) == 2 else [aux[0].strip().lower(), None]


def create_average_list(list_of_participants):#tested
    """
    Function that creates a list with all the average scores
    :param list_of_participants: the list of participants
    :return: the list of average scores
    """
    average_list = []

    for i in range(len(list_of_participants)):
        average_list.append(average_score(list_of_participants[i]))

    return average_list


def is_string_at(string):#not going to test
    """
    In this function we verify if a string is "at", otherwise we raise a ValueError
    :param string: a string
    :return: Nothing if the string is "at", ValueError otherwise
    """
    if string.lower() != "at":
        raise ValueError


def is_score_valid(score):#not going to test
    """
    In this function we verify if a score is correct
    :param score: a score
    :return: Nothing if the score is correct, ValueError otherwise
    """
    if score < 0 or score > 100:
        raise ValueError


def is_string_to(string):#not going to test
    """
    In this function we verify if a string is "to", otherwise we raise a ValueError
    :param string: a string
    :return: Nothing if the string is "to", ValueError otherwise
    """
    if string.lower() != "to":
        raise ValueError


def is_string_with(string):#not going to test
    """
    In this function we verify if a string is "with", otherwise we raise a ValueError
    :param string: a string
    :return: Nothing if the string is "with", ValueError otherwise
    """
    if string.lower() != "with":
        raise ValueError


def is_string_sorted(string):#not going to test
    """
    In this function we verify if a string is "sorted", otherwise we raise a ValueError
    :param string: a string
    :return: Nothing if the string is "sorted", ValueError otherwise
    """
    if string.lower() != "sorted":
        raise ValueError


def is_problem_valid(problem):#not going to test
    """
    In this function we verify if a problem is valid: the problem is marked between 0 and 10
    :param problem: a problem
    :return: Nothing if the problem is valid, ValueError otherwise
    """
    if problem < 0 or problem > 10:
        raise ValueError


def is_position_valid(position, list_of_participants):#not going to test
    """
    In this function we verify if a position is valid: the position exists in list
    :param position: a position
    :param list_of_participants: the entire list of participants
    :return: Nothing if the position is valid, ValueError otherwise
    """
    if position < 0 or position > len(list_of_participants):
        raise ValueError


def are_all_problems_valid(participant):#not going to test
    """
    In this function we verify if all the problems of a user are valid: they are marked between 0 and 10
    :param participant: a participant
    :return: Nothing if the problems are valid, ValueError otherwise
    """
    if len(participant) != 3:
        raise ValueError


def are_positions_valid(first_position, last_position):#not going to test
    """
    In this function we verify if the first position is smaller than the last position
    :param first_position: first position
    :param last_position: last position
    :return: Nothing if the positions are valid, ValueError otherwise
    """
    if first_position > last_position:
        raise ValueError


def is_sign(sign):#not going to test
    """
    In this function we verify if a string is <, > or =
    :param sign: a sign
    :return: Nothing if the sign is valid, ValueError otherwise
    """
    if sign != "<" and sign != ">" and sign != "=":
        raise ValueError


def is_string_problem(string):#not going to test
    """
    In this function we verify if a string is P1, P2 or P3
    :param string: a string
    :return: Nothing if the sign is valid, ValueError otherwise
    """
    if string != "p1" and string != "p2" and string != "p3":
        raise ValueError


def add_participant_to_list(list_of_participants, command_params, history):
    """
    In this function we add a new participant to our list of participants at the end of the list
    :param list_of_participants: the list of participants
    :param command_params: the parameters of add command which are the results of the 3 problems
    :param history: the history list
    :return: Nothing
    """
    copy = []
    participant = []
    params = command_params.split(" ")

    for param in params:
        copy.append(param.strip())

    P1 = int(get_first_problem(copy))
    P2 = int(get_second_problem(copy))
    P3 = int(get_third_problem(copy))
    participant.append(P1)
    participant.append(P2)
    participant.append(P3)
    for i in range(len(participant)):
        is_problem_valid(participant[i])
    are_all_problems_valid(participant)
    update_history(history, list_of_participants)
    list_of_participants.append(participant)


def insert_element_to_position(list_of_participants, command_params, history):
    """
    In this function we add a new participant to our list of participants at a given position
    :param list_of_participants: the list of participants
    :param command_params: the parameters of insert command which are the results of the 3 problems the string at and the position where you want to insert the participant
    :param history: the history list
    :return: Nothing
    """
    copy = []
    participant = []
    params = command_params.split(" ")

    for param in params:
        copy.append(param.strip())

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
    update_history(history, list_of_participants)
    list_of_participants.insert(position, participant)


def remove_element_from_list(list_of_participants, command_params, history):
    """
    In this function we remove a participant from a given position by setting all his scores to 0
    :param list_of_participants: the list of participants
    :param command_params: the parameter of remove command which is the position you want to remove from the list
    :param history: the history list
    :return: Nothing
    """
    copy = []
    params = command_params.split(" ")

    for param in params:
        copy.append(param.strip())

    position = int(copy[0])
    is_position_valid(position, list_of_participants)
    update_history(history, list_of_participants)
    set_participant_0(list_of_participants, position)


def remove_more_elements_by_positions(list_of_participants, command_params, history):
    """
    In this function we remove all the participants between 2 given positions by setting all their scores to 0
    :param list_of_participants: the list of participants
    :param command_params: the parameters of remove command which are the positions from where to where you want to remove
    :param history: the history list
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
    are_positions_valid(first_position, last_position)
    update_history(history, list_of_participants)

    for i in range(first_position, last_position + 1):
        set_participant_0(list_of_participants, i)


def replace_element_in_list(list_of_participants, command_params, history):
    """
    In this function we replace the problem's score of chosen player
    :param list_of_participants: the list of participants
    :param command_params: parameters of replace command
    :param history: the history list
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
    is_string_with(copy[2])
    problem_value = int(copy[3])
    is_problem_valid(problem_value)
    update_history(history, list_of_participants)

    if problem == "p1":
        set_first_problem(list_of_participants, problem_value, position)
    elif problem == "p2":
        set_second_problem(list_of_participants, problem_value, position)
    elif problem == "p3":
        set_third_problem(list_of_participants, problem_value, position)


def remove_more_elements_by_rule(list_of_participants, command_params, history):
    """
    In this function we remove all the participants that respect a rule
    :param list_of_participants: the list of participants
    :param command_params: the remove params with len(command_params) == 2
    :param history: the history list
    :return:
    """
    copy = []
    params = command_params.split(" ")

    for param in params:
        copy.append(param.strip())

    sign = copy[0]
    is_sign(sign)
    score = int(copy[1])
    is_score_valid(score)
    update_history(history, list_of_participants)
    if sign == "<":
        for i in range(len(list_of_participants)):
            if int(round(average_score(list_of_participants[i]),1) * 10) < score:
                set_participant_0(list_of_participants, i)
    elif sign == ">":
        for i in range(len(list_of_participants)):
            if int(round(average_score(list_of_participants[i]), 1) * 10) > score:
                set_participant_0(list_of_participants, i)
    elif sign == "=":
        for i in range(len(list_of_participants)):
            if int(round(average_score(list_of_participants[i]), 1) * 10) == score:
                set_participant_0(list_of_participants, i)


def update_history(history, list_of_participants):
    """
    In this function we update the history list everytime we make a command that updates the list
    :param history: the history list
    :param list_of_participants: the list of participants
    :return: nothing
    """
    new_list = list_of_participants[:]
    history.append(new_list)


def undo_preparation(history):
    """
    In this function we prepare the undo command
    :param history: the history list
    :return: the new list without the last command
    """
    if len(history) > 0:
        new_list = history[-1][:]
        history.pop()
        return new_list
    else:
        raise ValueError


def undo(list_of_participants, history):
    """
    In this function we make the undo command
    :param list_of_participants: the list of participants
    :param history: the history list
    :return: Nothing
    """
    new_list = undo_preparation(history)[:]
    if len(new_list) > 0:
        list_of_participants.clear()
        for item in new_list:
            list_of_participants.append(item)

