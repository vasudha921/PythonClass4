from typing import Pattern


class Cars:
    def __init__(self,engine, tires, carwheel, clutch, accelartor, model, color, speedlimit, brakes):
        self.engine = engine
        self.tires = tires
        self.carwheel = carwheel
        self.clutch = clutch
        self.accelarator = accelartor
        self.model = model
        self.color = color
        self.speedlimit = speedlimit
        self.brakes = brakes
    
    def start(self,engine, tires, carwheel):
        print("car has started")
    
    def stop(self, brakes):
        
       print(self.brakes)
        

    def accelarate(self, accelarator):
        print("car has increased its speed")

    def changegear(self, color):
        print("car color has changed", color)

RollsRoyceBoatTail= Cars("started", 4, "turn left", "clutch", "Increased speed", "Boat Tail", "blue", 100, "car has stopped at red light")
Kia= Cars("started", 4, "turn left", "clutch", "Increased speed", "Seltos", "Red", 80, "car has stopped in the parking lot")

print(Kia.accelarate(""))
print(Kia.changegear("blue"))
RollsRoyceBoatTail.stop("")
Kia.stop("")



        