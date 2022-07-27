import random

class Expense:
    def __init__(self, day, amount, type):
        """
        We create an object Expense of the class Expense with the following properties:
        :param day: The day the expense happened. It has to be an integer.
        :param amount: The amount of the expense. It has to be an integer
        :param type: The type of the expense. It has to be a string
        """
        if day < 1 or day > 30:
            raise ValueError("Invalid day")
        if amount < 1:
            raise ValueError("Invalid amount")
        self._day = day
        self._amount = amount
        self._type = type

    def __str__(self):
        """

        :return: The form in which we want to print the objects
        """
        return "On day " + str(self._day) + " you spent " + str(self._amount) + " on " + self._type

    @property
    def day(self):
        return self._day

    @property
    def amount(self):
        return self._amount

    @property
    def type(self):
        return self._type

    @day.setter
    def day(self, value):
        self._day = value

    @amount.setter
    def amount(self, value):
        self._amount = value

    @type.setter
    def type(self, value):
        self._type = value

    @staticmethod
    def sample_expenses():
        types =["Food", "VideoGames", "Clothes", "Transportation", "Phone Bill", "Utilities",
                            "Books", "UniversityFee", "Gas"]
        expenses =[]

        for i in range(0,10):
            expenses.append(Expense(random.randint(1, 30), random.randint(1, 500), random.choice(types)))

        return expenses

