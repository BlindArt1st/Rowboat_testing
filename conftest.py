import pytest
from API.rowboat import Rowboat

@pytest.fixture()
def prerequisites():
    boat = Rowboat()
    boat.occupy_seat()
    return boat

    

