class Car:
    def __init__(self, make, model_name, top_speed, color):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color
    ###str###
    def __str__(self):
        return f'{self.color} {self.make} {self.model_name} '
    ###repr###
    def __repr__(self):
        return f"Car(make={self.make} {self.model_name} {self.top_speed})"
    ###eq###
    def __eq__(self, other):
        return (
            self.make == other.make and
            self.model_name == other.model_name and
            self.top_speed == other.top_speed and
            self.color == other.color
        )
    def __eq__(self, other):
        return all(
            (self.make == other.make,
            self.model_name == other.model_name,
            self.top_speed == other.top_speed,
            self.color == other.color)
        )
    def __gt__(self, other):
        return self.top_speed > other.top_speed

car_one = Car(make='Ford', model_name='Mustang', top_speed=300, color='Black')
car_two = Car(make="Ford", model_name="Mustang", top_speed=300, color="Black")
car_three = Car(make="Ford", model_name="Mustang", top_speed=250, color="Yellow")

car_1 = Car(make='Ford', model_name='Mustang', top_speed=250, color='Red')
car_2 = Car(make='Ford', model_name='Fiesta', top_speed=200, color='Blue')
car_3 = Car(make='Ferrari', model_name='Testarossa', top_speed=350, color='Black')
cars = [car_1, car_2, car_3]
by_speed = sorted(cars, key=lambda car: car.top_speed)
by_make = sorted(cars, key=lambda car: car.make)
print(by_speed)
print(by_make)

print(car_one)
print(car_two)
print(car_one == car_two) #eq
print(car_one == car_three) #eq all
print(car_one > car_three)