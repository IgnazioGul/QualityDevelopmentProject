from pytest_mock import MockerFixture
from qd_project import home
from qd_project import HOME_LABEL

def test_home(mocker: MockerFixture) -> None:
 # arrange (empty)
 
 # act
 res = home() 
 # assert
 assert res == HOME_LABEL