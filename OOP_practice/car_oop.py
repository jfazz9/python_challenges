class Car:
    def __init__(self, make= 'Volkswagen',  model='Tiguan', colour='White', style='SUV', doors = 5): #add 5 arguments to instantiate
        self.colour = colour
        self.style = style
        self.doors = doors
        self.make = make
        self.model = model
        self._acceleration = 0
        self._direction = '' # single underscore to say it is private 
        self.__brake = 0 #add in the double underscore so you can't edit by variable
        self.status = ''

    def acceleration(self, rate):
        '''add in the speed of acceleration in mph for this method'''
        if not type(rate) is float:           #checking data type
            raise TypeError('Only integers allowed')
        self._acceleration = rate           #applying the 

    def check_acceleration(self):
        '''returns the acceleration speed'''
        print(f'your {self.make} {self.model} will acclerate from 0-60 in: {self._acceleration} seconds!')

    def brake(self, distance):
        if not type(distance) is int:
            raise TypeError('only numbers allowed')
        self.__brake = distance
        

    def braking_distance(self):
        '''implement the braking distance in metres'''
        print(f'The braking distance of your {self.make} {self.model} is {self.__brake} metres')

    def steer(self):
        '''choose a direction in which you want to steer North, East, South, West'''
        self.status = 'driving'
        directions = ['north', 'east', 'south', 'west']
        print('Please choose a direction in which you want to steer? \n North, East, South or West?')
        check_direct = True
        while check_direct:
            try:
                direction = str(input()).lower()
                if direction in directions:
                    self._direction = direction
                    check_direct = False
                else:
                    print('please enter North, East, South or West')
            except ValueError as ve:
                print(ve)
            
    
    def direction_car_facing(self):
        print(f'{self.make} {self.model} is currently facing {self._direction} and is {self.status}')

    def park(self):
        self.status = 'parked'


class Door(Car):
    def __init__(self, colour = 'Dark', open_style = 'Regular Doors', lock_type='automatic lock with key', handle= 'trigger'):

        super().__init__(colour)
        self.open_style = open_style
        self.lock_type = lock_type
        self.handle = handle
        self.__status = ''

    def open(self):
        self.__status = 'open'

    def shut(self):
        self.__status = 'closed'

    def lock_door(self):
        self.__status = 'locked'

    def wind_window_down(self):
        self.__window_status = 'window is winded down'
    
    def window_status(self):
        self.__

class Window(Door):
    def __init__(self, tint, thickness, material, handle):
        self.__tint = tint
        self.__thickness = thickness
        self.__material = material
        super().__init__(handle)

    
    

