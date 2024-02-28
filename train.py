class TrainCar:
    """ A train car with contents and a pointer to the car attached behind it (None if there are no cars behind it) """

    def __init__(self, contents: str):
        self.contents = contents
        self.next_car = None

class Train:
    """ A train, consisting of train cars attached to each other """

    def __init__(self):
        self.head_car = None
        self.size = 0
    
    def add_front(self, car: TrainCar):
        """ Adds the train car at the front of the train """
        if self.head_car != None:
            car.next_car = self.head_car
        self.head_car = car

        self.size += 1

    def add_back(self, car: TrainCar) -> None:
        """ Adds the train car at the end of the train """
        if self.head_car == None:
            self.head_car = car
            self.size += 1
            return

        # Find last car
        current_car = self.head_car
        while current_car != None:
            if current_car.next_car == None:
                current_car.next_car = car
                break
            current_car = current_car.next_car

        self.size += 1

    def insert(self, front_car: TrainCar, new_car: TrainCar) -> None:
        """ Attaches the new car to the 'front_car', replacing the car that used to be attached to 'front_car'. That will now
        be attached to the new car. """
        current_car = self.head_car

        while current_car != None:
            if current_car == front_car:
                temp_car = front_car.next_car
                new_car.next_car = temp_car
                current_car.next_car = new_car
                break
            current_car = current_car.next_car

        self.size += 1

    def search(self, contents: str) -> TrainCar:
        """ Returns the train car that has the provided contents, or None if it doesn't exist """
        current_car = self.head_car
        while current_car != None:
            if current_car.contents == contents:
                return current_car
            current_car = current_car.next_car
        return None

    def remove_front(self) -> bool:
        """ Removes the front train car from the train """
        pass

    def remove_back(self) -> bool:
        """ Removes the back train car from the train """
        if self.size == 0:
            return False

        current_car = self.head_car

        while current_car.next_car != None:
            if current_car.next_car.next_car == None:
                # Found second to last car
                current_car.next_car = None
                self.size -= 1
                return True
            current_car = current_car.next_car

    def remove(self, car: TrainCar) -> bool:
        """ Removes the target train car from the train, attaching the car behind it to the car in front of it """
        pass