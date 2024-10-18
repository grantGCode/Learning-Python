# Classes:
    # Classes are like blueprints for things I would like to create like objects.
    # You can pass in methods and property in to a class.

# Generic class
class Vehicle:
    def __init__(self, make, model): # Initializer function
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along..')
    
    def get_make_model(self): # Getter method
        print(f"I'm a {self.make} {self.model}.")

my_car = Vehicle('Honda', 'Civic') # my_car is an object I created from the Vehicle class.

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()


# inheritances

# All 3 classes will inherit everything from the Vehicle class. 
class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model) 
        # super() allows me to inherit make and model from the parent class Vehicle.
        self.faa_id = faa_id

    def moves(self):
        print('Flies along..')
    
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model} FAA-ID#: {self.faa_id}.")
        
class Truck(Vehicle):
    def moves(self):
        print('Rumbles along..')

class GolfCart(Vehicle):
    pass # Class will inherit ever thing from Vehicle as is.

cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()

print('\n\n')

# Polymerism:
    # The ability to behave differently in response to the same inputs messages.


for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()