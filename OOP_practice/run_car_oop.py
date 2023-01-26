from car_oop import Car, Door


def create_car(name= 'BMW', *args):
    car = Car(name, *args)
    car.acceleration(5.9)
    car.brake(40)
    return car

def create_toyota_hatchback():
    toyota = Car('Red', 'Hatchback', 3, 'Toyota', 'Celica')
    toyota.acceleration(4.1)
    toyota.brake(40)
    toyota.__brake = 32 # this will stop the variable from being changed as protected with '__'
    toyota.steer()
    
def return_information(obj):
    obj.braking_distance()
    obj.check_acceleration()
    obj.direction_car_facing()


if __name__ == '__main__':
    gary_the_car = create_car() # creating the car gary, which is an object
    sheila_the_car = create_car('Ford', 'Mustang', 'Red', 'Sports Car', 5) # using *args
    sheila_the_car.acceleration(3.1)
    print(gary_the_car.make)
    print(gary_the_car.model) 
    print(sheila_the_car) #returns the object info
    toyota_the_first = create_toyota_hatchback()
    toyota_the_second = create_toyota_hatchback()
    toyota_the_third = create_toyota_hatchback()
    print(toyota_the_first, ': first toyota')
    print(toyota_the_second, ': second toyota')
    print(toyota_the_third, ': third toyota')
    return_information(sheila_the_car)
    return_information(gary_the_car)

    '''instantiate the door'''
    gary_the_car = Door()