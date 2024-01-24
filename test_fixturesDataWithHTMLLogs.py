import pytest

from pytestdemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass): # connect / import parent class


# if we need to load data, we need to add parametr (dataload)
    def test_editProfile1(self,dataLoad):
        log = self.getlogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        print(dataLoad)

    def test_editProfile2(self,dataLoad):
        print(dataLoad[0])

    def test_editProfile3(self,dataLoad):
        print(dataLoad[2])