from car_oop import Car


def create_car(name):
    car = Car(name)
    return car


toyota = Car('Red', 'Hatchback', 3, 'Toyota', 'Celica')
toyota.acceleration(4.1)
toyota.check_acceleration()
toyota.brake(40)
toyota.braking_distance()
toyota.steer()
toyota.direction_car_facing()

if __name__ == '__main__':
    vw = create_car('gary')
    print(vw.model)