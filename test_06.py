
# If we have a lot of cases which use the same preconditions
# we can cover them in to the class and call one time

import pytest


@pytest.mark.usefixtures("setup_02")
class CaseWithTheSamePreconditions:

    def test_fixtureDemo(self):  # case will run preconditions from conftest.py file
        print("I will execute fixture method")

    def test_fixtureDemo1(self):  # case will run preconditions from conftest.py file
        print("I will execute fixture method")

    def test_fixtureDemo2(self):  # case will run preconditions from conftest.py file
        print("I will execute fixture method")

    def test_fixtureDemo3(self):  # case will run preconditions from conftest.py file
        print("I will execute fixture method")

    def test_fixtureDemo4(self):  # case will run preconditions from conftest.py file
        print("I will execute fixture method")
