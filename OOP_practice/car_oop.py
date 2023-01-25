class Car:
    def __init__(self, colour, style, doors, make):
        self.colour = colour
        self.style = style
        self.doors = doors
        self.make = make

    def acceleration(self):
        pass

    def brake(self):
        pass

    def steer(self):
        pass

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
    
    