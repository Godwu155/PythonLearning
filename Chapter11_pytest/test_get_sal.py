import pytest
from company import Employee

staff = Employee('John', 'Doe', '2000')
staff.address = '1000'
money = staff.get_salary()
    # print(money)


# @pytest.fixture
def test_employee():

    # print(money)
    assert money >= 1000