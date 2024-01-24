import pytest

# How to pass parameters in fixtures

# this tes will run three times according to conftest file, we pass 3 parameters one by one

def test_crossBroser(crossBrowser):
    print(crossBrowser)

def test_crossBroser2(crossBrowser2):
    print(crossBrowser2)

# we can pass 2 parameter from the group
def test_crossBroser2(crossBrowser2):
    print(crossBrowser2[1])
