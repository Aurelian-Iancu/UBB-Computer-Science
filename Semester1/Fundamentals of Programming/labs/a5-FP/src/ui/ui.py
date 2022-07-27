from src.services.services import Services
from src.domain.domain import Expense
from src.tests.test import test_add_expense
from copy import deepcopy


class UI:
    def __init__(self, service):
        self. _service = service
        self._history = [Expense.sample_expenses()]

    @staticmethod
    def print_menu():
        print("        The menu is:")
        print("1. Add an expense. Expense data is read from the console.")
        print("2. Display the list of expenses.")
        print("3. Filter the list so that it contains only expenses above a certain value read from the console.")
        print("4. Undo the last operation that modified program data. This step can be repeated.")
        print("5. Exit.")

    def ui_add_expense(self):
        day = input("Enter the day in which you want to insert an expense:")
        try:
            day = int(day)
        except ValueError:
            print("Invalid day")
            return
        if day < 1 or day > 30:
            print("Day must be greater than 1 or less than 30!")
            return
        amount = input("Enter the amount you spent that day:")
        try:
            amount = int(amount)
        except ValueError:
            print("Invalid amount")

        if amount < 0:
            print("Amount has to be positive!")
            return
        type = input("Enter the type of expense:")
        try:
            self._service.add_expense(Expense(day, amount, type))
            self._history.append(self._service.expenses)
        except Exception as e:
            print(e)

    def ui_list_expenses(self):
        for expense in self._service.expenses:
            print(expense)

    def ui_filter_expenses(self):
        value = input("Enter the desired value:")
        try:
            value = int(value)
        except ValueError:
            print("Invalid value")
        self._service.filter_expense(value)
        self._history.append(self._service.expenses)

    def start_menu(self):
        UI.print_menu()
        while True:
            Input = input("The command you want to chose from the menu is:")
            self._service.expenses = deepcopy(self._history[-1])
            if Input == "1":
                self.ui_add_expense()
            elif Input == "2":
                self.ui_list_expenses()
            elif Input == "3":
                self.ui_filter_expenses()
            elif Input == "4":
                if len(self._history) == 1:
                    print("You cannot undo anymore")
                else:
                    self._history.pop()
            elif Input == "5":
                return
            else:
                print("Invalid command")

serv = Services()
test_add_expense(serv)
ui = UI(serv)
ui.start_menu()
