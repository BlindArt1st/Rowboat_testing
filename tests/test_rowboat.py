import pytest
from API.rowboat import Oar, Anchor, Rowboat  


@pytest.mark.unit
def test_oar_initial_state():
    """Тест-кейс U-1"""
    left_oar = Oar("left")
    right_oar = Oar("right")
    
    assert left_oar.position == "idle", "Initial state of left oar is incorrect"
    assert right_oar.position == "idle", "Initial state of right oar is incorrect"


@pytest.mark.unit
def test_oar_row():
    """Тест-кейс U-2"""
    oar = Oar("left")
    oar.row()
    assert oar.position == "rowing", "Oar should be in 'rowing' state after calling row()"


@pytest.mark.unit
def test_oar_stop():
    """Тест-кейс U-3"""
    oar = Oar("right")
    oar.row()  
    oar.stop()   
    assert oar.position == "idle", "Oar should be in 'idle' state after calling stop()"    


@pytest.mark.unit
def test_anchor_initial_state():
    """Тест-кейс U-4"""
    anchor = Anchor()
    assert anchor.is_dropped == False, "Anchor should be initially lifted"


@pytest.mark.unit
def test_anchor_drop():
    """Тест-кейс U-5"""
    anchor = Anchor()
    anchor.drop()
    assert anchor.is_dropped == True, "Anchor should be dropped after calling drop()"


@pytest.mark.unit
def test_anchor_lift():
    """Тест-кейс U-6"""
    anchor = Anchor()
    anchor.drop()  
    anchor.lift()
    assert anchor.is_dropped == False, "Anchor should be lifted after calling lift()"


@pytest.mark.unit
def test_seat_can_be_occupied():
    """Тест-кейс U-7"""
    boat = Rowboat()
    initial_free_seats = boat.seats.count(False)
    
    boat.occupy_seat()
    
    assert boat.seats.count(False) == initial_free_seats - 1, "The number of available seats had to decrease"


@pytest.mark.unit
def test_seat_can_be_freed():
    """Тест-кейс U-8"""
    boat = Rowboat()
    boat.occupy_seat()  
    initial_free_seats = boat.seats.count(False)
    
    boat.free_seat()
    
    assert boat.seats.count(False) == initial_free_seats + 1, "The number of available seats had to increase"


@pytest.mark.unit
def test_maximum_seats():
    """Тест-кейс U-9"""
    boat = Rowboat()
    for _ in range(3):
        boat.occupy_seat()
    
    boat.occupy_seat()
    free_seats = boat.seats.count(False)
    
    assert free_seats == 0, "All seats should be occupied"    


@pytest.mark.unit
def test_maximum_speed():
    """Тест-кейс U-10"""
    boat = Rowboat()
    boat.occupy_seat()

    for _ in range(boat.MAX_SPEED + 1): 
        boat.row()

    assert boat.speed == boat.MAX_SPEED, "Speed should not exceed MAX_SPEED"


@pytest.mark.integration
def test_rowing(prerequisites):
    '''Тест-кейс I-1'''
    boat = prerequisites
    
    initial_speed = boat.speed
    boat.row()
    assert boat.speed > initial_speed, "Boat speed has not increased"
    assert boat.oars["left"].position == "rowing", "Left oar status is incorrect"
    assert boat.oars["right"].position == "rowing", "Right oar status is incorrect"


@pytest.mark.integration
def test_stop_rowing(prerequisites):
    '''Тест-кейс I-2'''
    boat = prerequisites
    
    boat.row()
    boat.stop()
    assert boat.speed == 0, "Boat speed is not null"
    assert boat.oars["left"].position == "idle", "Left oar status is incorrect"
    assert boat.oars["right"].position == "idle", "Right oar status is incorrect"
    

@pytest.mark.integration
def test_turning(prerequisites):
    '''Тест-кейс I-3'''
    boat = prerequisites
    
    boat.row_left()
    assert (
        boat.oars["left"].position == "rowing"
        and boat.oars["right"].position == "idle"
    ), "Left oar status is incorrect"
    assert boat.direction == "right", "Direction is not 'right'"
    
    boat.row_right()
    assert (
        boat.oars["right"].position == "rowing" 
        and boat.oars["left"].position == "idle"
    ), "Right oar status is incorrect"
    assert boat.direction == "left", "Direction is not 'left'"
    

@pytest.mark.integration   
def test_rowing_while_anchor_is_dropped(prerequisites):
    '''Тест-кейс I-4'''
    boat = prerequisites
    
    boat.drop_anchor()
    boat.row()
    assert boat.speed == 0, "Boat should not move when the anchor is dropped"


@pytest.mark.integration
def test_rowing_while_anchor_is_lifted(prerequisites):
    '''Тест-кейс I-5'''
    boat = prerequisites
    
    boat.drop_anchor()
    boat.lift_anchor()
    boat.row()
    assert boat.speed > 0, "Boat should be able to move after anchor is raised"


@pytest.mark.integration
def test_steer_empty_boat(prerequisites):
    '''Тест-кейс I-6'''
    boat = prerequisites
    
    boat.free_seat()
    boat.row()
    assert boat.speed == 0, "Boat should not move without occupied seats"
    boat.row_left()
    assert boat.oars["left"].position == "idle", "Left oar status is incorrect"
    assert boat.oars["right"].position == "idle", "Right oar status is incorrect"
    

@pytest.mark.integration   
def test_use_anchor_while_boat_is_empty(prerequisites):
    '''Тест-кейс I-7'''
    boat = prerequisites
    boat.free_seat()
    
    boat.drop_anchor()
    assert not boat.anchor.is_dropped, "The anchor should not have been dropped"
    
    boat.occupy_seat()
    boat.drop_anchor()
    boat.free_seat()
    
    boat.lift_anchor()
    assert boat.anchor.is_dropped, "The anchor should not have been lifted"  
    

@pytest.mark.integration    
def test_lifting_lifted_anchor(prerequisites):
    '''Тест-кейс I-8'''
    boat = prerequisites
    
    boat.lift_anchor()
    assert not boat.anchor.is_dropped
    
    boat.row()
    assert boat.speed != 0, "The boat had to speed up"


@pytest.mark.integration    
def test_dropping_dropped_anchor(prerequisites):
    '''Тест-кейс I-9'''
    boat = prerequisites
    
    boat.drop_anchor()
    boat.drop_anchor()
    assert boat.anchor.is_dropped
    
    boat.row()
    assert boat.speed == 0, "The boat should not have to speed up"
    


    
    