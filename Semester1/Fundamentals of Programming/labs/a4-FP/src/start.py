"""
  Start the program by running this module
"""
from ui import *
from functions import *
from test import *


def start():
    list_of_participants = init_list_of_participants()
    run_all_tests()
    run_menu()

start()