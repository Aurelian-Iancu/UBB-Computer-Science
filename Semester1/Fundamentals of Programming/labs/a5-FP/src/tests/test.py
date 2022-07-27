from src.services.services import Services
from src.domain.domain import Expense


def test_add_expense(serv=Services()):
    serv.expenses = []
    serv.add_expense(Expense(10, 20, "Phone bill"))
    assert len(serv.expenses) == 1
    serv.add_expense(Expense(30, 50, "Food"))
    assert len(serv.expenses) == 2


test_add_expense()


