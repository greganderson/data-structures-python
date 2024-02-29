import pytest
from train import TrainCar, Train


@pytest.fixture
def test_train() -> Train:
    result_test_train = Train()

    trains = [TrainCar(f"Contents {i}") for i in range(10)]
    for train in trains:
        result_test_train.add_back(train)
    
    return result_test_train

def test_add_front():
    test_train = Train()

    test_car_1_contents = "Harry Potter and friends"
    test_car_1 = TrainCar(test_car_1_contents)

    test_train.add_front(test_car_1)

    assert test_train.head_car != None
    assert test_train.head_car.contents == test_car_1_contents
    assert test_train.size == 1

    # Test second car
    test_car_2_contents = "Prefects"
    test_car_2 = TrainCar(test_car_2_contents)

    test_train.add_front(test_car_2)

    assert test_train.head_car != None
    assert test_train.head_car.contents == test_car_2_contents
    assert test_train.head_car.next_car == test_car_1
    assert test_train.size == 2

def test_add_front(test_train: Train):
    assert test_train.size == 10
    test_train.add_front(TrainCar("Alan"))
    assert test_train.size == 11

def test_add_back():
    test_train = Train()

    # Test first car
    test_car_1_contents = "Harry Potter and friends"
    test_car_1 = TrainCar(test_car_1_contents)
    test_train.add_back(test_car_1)

    assert test_train.head_car != None
    assert test_train.head_car.contents == test_car_1_contents
    assert test_train.size == 1

    # Test second car
    test_car_2_contents = "Prefects"
    test_car_2 = TrainCar(test_car_2_contents)
    test_train.add_back(test_car_2)

    assert test_train.head_car.next_car != None
    assert test_train.head_car.next_car.contents == test_car_2_contents
    assert test_train.size == 2

def test_insert(test_train: Train):
    c = test_train.head_car
    while c.next_car != None and c.contents != "Contents 5":
        c = c.next_car

    assert test_train.head_car.next_car.next_car.next_car.next_car.next_car.contents == "Contents 5"

    new_car = TrainCar("New car")
    test_train.insert(c, new_car)
    assert test_train.size == 11

    assert c.next_car == new_car

def test_search(test_train: Train):
    expected_car_contents = "Contents 7"
    
    actual_car = test_train.search(expected_car_contents)
    assert actual_car.contents == expected_car_contents

    actual_car = test_train.search("Nonexistent car")
    assert actual_car == None

def test_remove_front(test_train: Train):
    assert test_train.remove_front() == True
    assert test_train.head_car.contents == "Contents 1"
    assert test_train.size == 9

def test_remove_front_empty_train():
    empty_train = Train()
    assert empty_train.remove_front() == False
    assert empty_train.size == 0

def test_remove_back(test_train: Train):
    assert test_train.remove_back() == True

    current_car = test_train.head_car
    while current_car.next_car != None:
        current_car = current_car.next_car

    expected_car_contents = "Contents 8"
    assert current_car.contents == expected_car_contents

    assert test_train.size == 9

def test_remove_back_empty_train():
    empty_train = Train()
    assert empty_train.remove_back() == False
    assert empty_train.size == 0

def test_remove(test_train: Train):
    car_to_remove = test_train.search("Contents 3")

    test_train.remove(car_to_remove)
    assert test_train.size == 9

def test_remove_single_car_train():
    test_train = Train()
    car = TrainCar("Chris")
    test_train.add_back(car)

    assert test_train.size == 1
    test_train.remove(car)
    assert test_train.size == 0

def test_remove_front_car_with_cars_behind_and_such(test_train: Train):
    test_train.remove(test_train.head_car)
    assert test_train.size == 9
    assert test_train.head_car is not None