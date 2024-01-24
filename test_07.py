import pytest


@pytest.mark.usefixtures("dataLoad_2")
class TestExample3:


# if we need to load data, we need to add parametr (dataload)
    def test_data(self,dataLoad_2):
        print(dataLoad_2[0:3])


    def test_data2(self, dataLoad_2):
         print(dataLoad_2[1])


    def test_data3(self,dataLoad_2):
        print(dataLoad_2[2])
