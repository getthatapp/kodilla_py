class Car:
    def __init__(self, make, model_name, top_speed, color):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color

mustang = Car(make='Ford', model_name='Mustang', top_speed=300, color='black')
print(mustang)
print(mustang.top_speed)