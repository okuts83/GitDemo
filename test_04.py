import pytest

# create a preconditions
# test ermssage

@pytest.fixture() # if we need to execute any preconditions before run test
def setup():
    print("I will be run first as a precondition")
    yield
    print("I will be executed in the end")



# case which will usepreconditions
def test_111(setup):
    print("I will execute fixture method")




