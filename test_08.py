
# If we have a lot of cases which use the same preconditions
# we can cover them in to the class and call one time


# All tests use preconditions from conftest.py

def test_12(setup_02):  # case will run preconditions from conftest.py file
    print("I will execute fixture method")

def test_13(setup_02):  # case will run preconditions from conftest.py file
    print("I will execute fixture method")

def test_14(setup_02):  # case will run preconditions from conftest.py file
    print("I will execute fixture method")

def test_15(setup_02):  # case will run preconditions from conftest.py file
    print("I will execute fixture method")

def test_16(setup_02):  # case will run preconditions from conftest.py file
    print("I will execute fixture method")
