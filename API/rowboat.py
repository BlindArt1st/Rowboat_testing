class Oar:
    def __init__(self, side):
        self.side = side  # Левое или правое весло
        self.position = "idle"
    
    def row(self):
        self.position = "rowing"
    
    def stop(self):
        self.position = "idle"

class Anchor:
    def __init__(self):
        self.is_dropped = False
    
    def drop(self):
        self.is_dropped = True
        print("Якорь опущен.")
    
    def lift(self):
        self.is_dropped = False
        print("Якорь поднят.")

class Rowboat:
    MAX_SEATS = 3  
    MAX_SPEED = 4
    def __init__(self, seats_count=3):
        if seats_count > self.MAX_SEATS:
            raise ValueError(f"Максимальное количество мест в лодке: {self.MAX_SEATS}")
        
        self.speed = 0  
        self.direction = "straight"  
        self.oars = {
            "left": Oar("left"),
            "right": Oar("right")
        }
        self.seats = [False] * seats_count  # False - место свободно, True - занято
        self.anchor = Anchor()
        
    #Грести обоими вёслами
    def row(self):
        if self.anchor.is_dropped:
            print("Нельзя грести, пока якорь опущен!")
            return
        if self.seats.count(True) == 0:
            print("Некому управлять лодкой")
            return
        self.oars["left"].row()
        self.oars["right"].row()
        if self.speed < self.MAX_SPEED:
            self.speed += 1
            print(f"Полный вперед! Скорость: {self.speed}")
                
    #Грести только левым веслом (поворот вправо)
    def row_left(self):
        if self.seats.count(True) == 0:
            print("Некому управлять лодкой")
            return
        self.oars["left"].row()
        self.oars["right"].stop()
        self.direction = "right"
        print("Гребем левым веслом. Лодка поворачивает вправо.")
    
    #Грести только правым веслом (поворот влево).
    def row_right(self):
        if self.seats.count(True) == 0:
            print("Некому управлять лодкой")
            return
        self.oars["right"].row()
        self.oars["left"].stop()
        self.direction = "left"
        print("Гребем правым веслом. Лодка поворачивает влево.")
    
    def stop(self):
        if self.seats.count(True) == 0:
            print("Некому управлять лодкой")
            return
        self.speed = 0
        self.oars["left"].stop()
        self.oars["right"].stop()
        print("Он не гребет и огребет.")
    
    def drop_anchor(self):
        if self.seats.count(True) == 0:
            print("Некому управлять лодкой")
            return
        if self.anchor.is_dropped == True:
            return
        self.stop()
        self.anchor.drop()
    
    def lift_anchor(self):
        if self.seats.count(True) == 0:
            print("Некому управлять лодкой")
            return
        if self.anchor.is_dropped == False:
            return
        self.anchor.lift()
        
    #Занять любое свободное место в лодке
    def occupy_seat(self):
        for i in range(len(self.seats)):
            if not self.seats[i]:
                self.seats[i] = True
                print(f"Место занято. Свободных мест осталось: {self.seats.count(False)}")
                return
        print("Все места заняты!")
        
    #Освободить любое занятое место в лодке
    def free_seat(self):
        for i in range(len(self.seats)):
            if self.seats[i]:
                self.seats[i] = False
                print(f"Место освобождено. Свободных мест теперь: {self.seats.count(False)}")
                return
        print("Нет занятых мест для освобождения!")
    
    def check_status(self):
        return {
            "speed": self.speed,
            "direction": self.direction,
            "oars_position": {
                "left": self.oars["left"].position,
                "right": self.oars["right"].position
            },
            "anchor_status": "dropped" if self.anchor.is_dropped else "lifted",
            "available_seats": self.seats.count(False)
        }


   
