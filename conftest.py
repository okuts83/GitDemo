

# create a special iniversal file with a name conftest.py with preconditions
# we can call preconditions by names
# one file conftest.py for all cases in the folder
import pytest


@pytest.fixture(scope="class") # if we need to execute any preconditions before run test
# scope="class" >>> for class if we need to run at the beginning and at the end
def setup_02():
    print("I will be run first as a precondition from conftest") # precondition
    yield
    print("I will be executed in the end from congtest") # postcondition

@pytest.fixture()
def dataLoad():
    print("User profile data has been created")
    return ["Name", "Surname","rahulacademy@email.com"]       # if we need to pass some data

@pytest.fixture(scope="class")
def dataLoad_2(scope="class"):
    print("User data is:")
    return ["Lesha", "Last_Name", "super.email@email.com"]       # if we need to pass some data


# Fixture will run 3 times as we have 3 parameters
@pytest.fixture(params=["Name", "Surname", "email"])
def crossBrowser(request):
    return request.param

# Fixture will run 3 times as we have 3 group of parameters
@pytest.fixture(params=[("Name", "Lesha", "Pasha"), ("Surname","Petrov","Petrenko"), ("email","email@email.com")])
def crossBrowser2(request):
    return request.param

