# 1. Any pytest file should start with "tets_" or end with "_test", this is a rule
####
# 2. pytest method should start with test

# 3. Any code should be wrapped in method only

# >>> How to run PYTESTS >>>
# 1. Copy full path to py package (C:\Users\okuts\PycharmProjects\UdemyPython\pytests>)
# 2. Open CMD
# 3. cd ***our full path to TC's***
# 4. add >>> py.test -v -s >>> (-v-s  -details)
# 5. to run special case >>> -k NameOfCase (py.test -k Creditcard -v -s)
# 6. to run "mark" group of tests >>> -m "name of group" (py.test -m smoke -v -s)
# 7. to skip case >>> add mark @pytest.mark.skip
# 8. to run case and not displayed failed >> @pytest.mark.xfail

import pytest  # to switch marks

def test_FirsttTest():
    print("hello")

@pytest.mark.smoke
def test_SecondTest():
    msg = "hi"
    print(msg)
    assert msg == "Hello", "It is not match"

@pytest.mark.smoke
@pytest.mark.skip # if we want to skip cases
def test_Second2Test():
    msg = "hi"
    print(msg)
    assert msg == "Hello", "It is not match"

@pytest.mark.smoke
@pytest.mark.xfail # if we want to run case but do not display failed
def test_Second3Test():
    msg = "hi"
    print(msg)
    assert msg == "Hello", "It is not match"

@pytest.mark.smoke
def test_ThirdTest_CreditCard():
    a = 20
    b = 15
    assert a > b, "Card is correct"

def test_FortTest_CreditCard():
    a = 2
    b = 3
    assert a == b, "Card is incorrect"

