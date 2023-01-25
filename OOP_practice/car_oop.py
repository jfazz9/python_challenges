class Car:
    def __init__(self, colour='White', style='SUV', doors = 5, make= 'Volkswagen' , model='Tiguan'): #add 5 arguments to instantiate
        self.colour = colour
        self.style = style
        self.doors = doors
        self.make = make
        self.model = model
        self._acceleration = 0
        self._direction = ''
        self._brake = 0

    def acceleration(self, rate):
        '''add in the speed of acceleration in mph for this method'''
        if not type(rate) is float:           #checking data type
            raise TypeError('Only integers allowed')
        self._acceleration = rate           #applying the 
        
    def check_acceleration(self):
        '''returns the accelration speed'''
        print(f'your {self.make} {self.model} will acclerate from 0-60 in: {self._acceleration} seconds!')

    def brake(self, distance):
        if not type(distance) is int:
            raise TypeError('only numbers allowed')
        self._brake = distance

    def braking_distance(self):
        '''implement the braking distance in metres'''
        print(f'The braking distance of your {self.make} {self.model} is {self._brake} metres')

    def steer(self):
        '''choose a direction in which you want to steer North, East, South, West'''
        directions = ['north', 'east', 'south', 'west']
        print('Please choose a direction in which you want to steer? \n North, East, South or West?')
        
        try:
            direction = str(input()).lower()
            if direction in directions:
                self._direction = direction
        except ValueError('please enter a direction, North, East, South or West...') as ve:
            print(ve)
                
        
    
    def direction_car_facing(self):
        print(f'{self.make} {self.model} is currently facing {self._direction}')
    def park(self):
        pass

class Door(Car):
    def __init__(self, colour, open_style, lock_type, handle):
        super().__init__(colour)
        self.open_style = open_style
        self.lock_type = lock_type
        self.handle = handle

    def open(self):
        pass

    def shut(self):
        pass

    def lock_door(self):
        pass

    def wind_window_down(self):
        pass

class Window(Door):
    def __init__(self, tint, thickness, material, handle):
        self.tint = tint
        self.thickness = thickness
        self.material = material
        super().__init__(handle)
    

