from train import TrainCar, Train


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
    assert test_train.size == 2

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

def test_insert():
    test_train = Train()

    test_cars = [TrainCar(f"Contents {i}") for i in range(10)]

    for car in test_cars:
        test_train.add_back(car)
    
    c = test_train.head_car
    while c.next_car != None and c.contents != "Contents 5":
        c = c.next_car
    

    assert test_train.size == 10
    # head - 1 - 2 - 3 - 4 - 5
    assert test_train.head_car.next_car.next_car.next_car.next_car.next_car.contents == "Contents 5"

    c = test_train.head_car
    while c.next_car != None:
        c = c.next_car

    new_car = TrainCar("New car")
    # Same as add_back
    test_train.insert(c, new_car)
    assert c.next_car == new_car
    assert test_train.size == 11

def test_search():
    test_train = Train()

    test_cars = [TrainCar(f"Contents {i}") for i in range(10)]

    for car in test_cars:
        test_train.add_back(car)

    target_car = test_cars[5]

    actual_car = test_train.search(target_car.contents)

    assert target_car == actual_car

def test_remove_back():
    test_train = Train()

    assert test_train.remove_back() == False

    test_cars = [TrainCar(f"Contents {i}") for i in range(10)]
    for car in test_cars:
        test_train.add_back(car)

    assert test_train.size == 10
    assert test_train.remove_back() == True
    assert test_train.size == 9

    expected_back_car = test_cars[8]
    actual_back_car = test_train.head_car
    while actual_back_car.next_car != None:
        actual_back_car = actual_back_car.next_car

    assert expected_back_car == actual_back_car