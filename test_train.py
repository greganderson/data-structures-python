import pytest

from train import TrainCar, Train


def test_add_front(setup_train):
    test_train = Train()

    test_car_1_contents = "Harry Potter and friends"
    test_car_1 = TrainCar(test_car_1_contents)

    test_train.add_front(test_car_1)

    assert test_train.head_car != None
    assert test_train.head_car.contents == test_car_1_contents

    # Test second car
    test_car_2_contents = "Prefects"
    test_car_2 = TrainCar(test_car_2_contents)

    test_train.add_front(test_car_2)

    assert test_train.head_car != None
    assert test_train.head_car.contents == test_car_2_contents

def test_add_back():
    test_train = Train()

    # Test first car
    test_car_1_contents = "Harry Potter and friends"
    test_car_1 = TrainCar(test_car_1_contents)
    test_train.add_back(test_car_1)

    assert test_train.head_car != None
    assert test_train.head_car.contents == test_car_1_contents

    # Test second car
    test_car_2_contents = "Prefects"
    test_car_2 = TrainCar(test_car_2_contents)
    test_train.add_back(test_car_2)

    assert test_train.head_car.next_car != None
    assert test_train.head_car.next_car.contents == test_car_2_contents

def test_insert():
    test_train = Train()

    test_cars = [TrainCar(f"Contents {i}") for i in range(10)]

    for car in test_cars:
        test_train.add_back(car)
    
    c = test_train.head_car
    while c.next_car != None and c.contents != "Contents 5":
        c = c.next_car
    
    new_car = TrainCar("New car")
    test_train.insert(c, new_car)

    assert test_train.size == 11
    assert test_train.head_car.next_car.next_car.next_car.next_car.contents == "Content 5"
    assert test_train.head_car.next_car.next_car.next_car.next_car.contents == "New car"