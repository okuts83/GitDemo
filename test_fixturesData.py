import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:


# if we need to load data, we need to add parametr (dataload)
    def test_editProfile1(self,dataLoad):
        print(dataLoad)

    def test_editProfile2(self,dataLoad):
        print(dataLoad[0])

    def test_editProfile3(self,dataLoad):
        print(dataLoad[2])