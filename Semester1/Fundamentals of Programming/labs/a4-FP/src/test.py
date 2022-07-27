"""
    Tests module
"""

from functions import *


def test_create_participant():
    """
    Function to test the create_participant function
    :return: Nothing if the tests pass, AssertionError otherwise
    """
    assert create_participant(0, 1, 2) == [0, 1, 2]
    assert create_participant(5, 5, 10) == [5, 5, 10]


def test_init_list_of_participants():
    """
    Function to test the init_list_of_participants function
    :return: Nothing if the tests pass, AssertionError otherwise
    """
    assert init_list_of_participants() == [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6], [3, 4, 4], [5, 5, 5], [10, 3, 8], [9, 9, 6], [0, 5, 4], [1, 10, 10]]


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


def test_get_first_problem():
    """
    Function to test the get_first_problem function
    :return: Nothing if the tests pass, AssertionError otherwise
    """
    assert get_first_problem([1, 2, 3]) == 1


def test_get_second_problem():
    """
    Function to test the get_second_problem function
    :return: Nothing if the tests pass, AssertionError otherwise
    """
    assert get_second_problem([1, 2, 3]) == 2


def test_get_third_problem():
    """
    Function to test the get_third_problem function
    :return: Nothing if the tests pass, AssertionError otherwise
    """
    assert get_third_problem([1, 2, 3]) == 3


def test_get_lowest_score():
    assert get_lowest_score([[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6], [3, 4, 4], [5, 5, 5], [10, 3, 8], [9, 9, 6], [0, 5, 4], [1, 10, 10]], 2, 7) == 3.67
    assert get_lowest_score([[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6], [3, 4, 4], [5, 5, 5], [10, 3, 8], [9, 9, 6], [0, 5, 4], [1, 10, 10]], 2, 8) == 3.0
    assert get_lowest_score([[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6], [3, 4, 4], [5, 5, 5], [10, 3, 8], [9, 9, 6], [0, 5, 4], [1, 10, 10]], 1, 3) == 5.33
    assert get_lowest_score([[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6], [3, 4, 4], [5, 5, 5], [10, 3, 8], [9, 9, 6], [0, 5, 4], [1, 10, 10]], 1, 1) == 7.33
    assert get_lowest_score([[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6], [3, 4, 4], [5, 5, 5], [10, 3, 8], [9, 9, 6], [0, 5, 4], [1, 10, 10]], 0, 9) == 3.0


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


def test_create_average_list():
    assert create_average_list([[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6], [3, 4, 4], [5, 5, 5], [10, 3, 8], [9, 9, 6], [0, 5, 4], [1, 10, 10]]) == [6.0, 7.33, 9.67, 5.33, 3.67, 5.0, 7.0, 8.0, 3.0, 7.0]


def test_add_participant_to_list():
    list = [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]
    history = []

    add_participant_to_list(list, "3 8 8", history)
    assert list == [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6], [3, 8, 8]]

    add_participant_to_list(list, "3 8 8", history)
    assert list == [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6], [3, 8, 8], [3, 8, 8]]


def test_insert_element_to_position():
    list = [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]
    history = []

    insert_element_to_position(list, "1 2 3 at 0", history)
    assert list == [[1, 2, 3], [5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]

    insert_element_to_position(list, "1 1 2 at 1", history)
    assert list == [[1, 2, 3], [1, 1, 2], [5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]

    insert_element_to_position(list, "10 10 10 at 6", history)
    assert list == [[1, 2, 3], [1, 1, 2], [5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6], [10, 10, 10]]


def test_remove_element_from_list():
    list = [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]
    history = []

    remove_element_from_list(list, "0", history)
    assert list == [[0, 0, 0], [8, 5, 9], [10, 10, 9], [2, 8, 6]]

    remove_element_from_list(list, "1", history)
    assert list == [[0, 0, 0], [0, 0, 0], [10, 10, 9], [2, 8, 6]]

    remove_element_from_list(list, "2", history)
    assert list == [[0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 8, 6]]

    remove_element_from_list(list, "3", history)
    assert list == [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_remove_more_elements_by_positions():
    list = [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]
    history = []

    remove_more_elements_by_positions(list, "0 to 1", history)
    assert list == [[0, 0, 0], [0, 0, 0], [10, 10, 9], [2, 8, 6]]

    remove_more_elements_by_positions(list, "2 to 3", history)
    assert list == [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_replace_element_in_list():
    list = [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]
    history = []

    replace_element_in_list(list, "0 p1 with 10", history)
    assert list == [[10, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]

    replace_element_in_list(list, "0 p2 with 10", history)
    assert list == [[10, 10, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]

    replace_element_in_list(list, "0 p3 with 10", history)
    assert list == [[10, 10, 10], [8, 5, 9], [10, 10, 9], [2, 8, 6]]


def test_remove_more_elements_by_rule():
    list = [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]
    history = []
    remove_more_elements_by_rule(list, "< 70", history)
    assert list == [[0, 0, 0], [8, 5, 9], [10, 10, 9], [0, 0, 0]]

    list = [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]
    remove_more_elements_by_rule(list, "> 70", history)
    assert list == [[5, 6, 7], [0, 0, 0], [0, 0, 0], [2, 8, 6]]

    list = [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]
    remove_more_elements_by_rule(list, "= 60", history)
    assert list == [[0, 0, 0], [8, 5, 9], [10, 10, 9], [2, 8, 6]]


def test_undo():
    list = [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]
    history = []

    add_participant_to_list(list, "3 8 8", history)
    assert list == [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6], [3, 8, 8]]
    undo(list, history)
    assert list == [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]

    insert_element_to_position(list, "1 2 3 at 0", history)
    assert list == [[1, 2, 3], [5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]
    undo(list, history)
    assert list == [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]

    remove_element_from_list(list, "0", history)
    assert list == [[0, 0, 0], [8, 5, 9], [10, 10, 9], [2, 8, 6]]
    undo(list, history)
    assert list == [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]

    remove_more_elements_by_positions(list, "0 to 1", history)
    assert list == [[0, 0, 0], [0, 0, 0], [10, 10, 9], [2, 8, 6]]
    undo(list, history)
    assert list == [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]

    replace_element_in_list(list, "0 p1 with 10", history)
    assert list == [[10, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]
    undo(list, history)
    assert list == [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]

    remove_more_elements_by_rule(list, "< 70", history)
    assert list == [[0, 0, 0], [8, 5, 9], [10, 10, 9], [0, 0, 0]]
    undo(list, history)
    assert list == [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]

    remove_more_elements_by_rule(list, "> 70", history)
    assert list == [[5, 6, 7], [0, 0, 0], [0, 0, 0], [2, 8, 6]]
    undo(list, history)
    assert list == [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]

    remove_more_elements_by_rule(list, "= 60", history)
    assert list == [[0, 0, 0], [8, 5, 9], [10, 10, 9], [2, 8, 6]]
    undo(list, history)
    assert list == [[5, 6, 7], [8, 5, 9], [10, 10, 9], [2, 8, 6]]


def run_all_tests():
    test_create_participant()
    test_init_list_of_participants()
    test_average_score()
    test_get_first_problem()
    test_get_second_problem()
    test_get_third_problem()
    test_split_command_params()
    test_create_average_list()
    test_add_participant_to_list()
    test_insert_element_to_position()
    test_remove_element_from_list()
    test_remove_more_elements_by_positions()
    test_replace_element_in_list()
    test_remove_more_elements_by_rule()
    test_undo()
