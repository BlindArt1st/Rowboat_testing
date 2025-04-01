class Oar:
    def __init__(self, side):
        self.side = side  # Левое или правое весло
        self.position = "idle"
    
    def row(self):
        self.position = "rowing"
    
    def stop(self):
        self.position = "idle"

class Seat:
    def __init__(self, number):
        self.number = number

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
    MAX_SEATS = 3  # Ограничение на количество мест
    
    def __init__(self, seats_count=2):
        if seats_count > self.MAX_SEATS:
            raise ValueError(f"Максимальное количество мест в лодке: {self.MAX_SEATS}")
        
        self.speed = 0  # Скорость лодки
        self.direction = "straight"  # Направление
        self.oars = {
            "left": Oar("left"),
            "right": Oar("right")
        }
        self.seats = [Seat(i + 1) for i in range(seats_count)]
        self.anchor = Anchor()
    
    def row(self):
        """Грести обоими вёслами, увеличивая скорость."""
        if self.anchor.is_dropped:
            print("Нельзя плыть, пока якорь опущен!")
            return
        self.oars["left"].row()
        self.oars["right"].row()
        self.speed += 1
        print(f"Гребем обоими вёслами! Скорость: {self.speed}")
    
    def row_left(self):
        """Грести только левым веслом (поворот вправо)."""
        self.oars["left"].row()
        self.oars["right"].stop()
        self.direction = "right"
        print("Гребем левым веслом! Лодка поворачивает вправо.")
    
    def row_right(self):
        """Грести только правым веслом (поворот влево)."""
        self.oars["right"].row()
        self.oars["left"].stop()
        self.direction = "left"
        print("Гребем правым веслом! Лодка поворачивает влево.")
    
    def stop(self):
        """Остановить движение лодки."""
        self.speed = 0
        self.oars["left"].stop()
        self.oars["right"].stop()
        print("Лодка остановилась.")
    
    def drop_anchor(self):
        """Опустить якорь."""
        self.stop()
        self.anchor.drop()
    
    def lift_anchor(self):
        """Поднять якорь."""
        self.anchor.lift()
    
    def check_status(self):
        """Получить текущее состояние лодки."""
        return {
            "speed": self.speed,
            "direction": self.direction,
            "oars_position": {
                "left": self.oars["left"].position,
                "right": self.oars["right"].position
            },
            "anchor_status": "dropped" if self.anchor.is_dropped else "lifted",
            "seats_count": len(self.seats)
        }

# Пример использования
if __name__ == "__main__":
    boat = Rowboat()
    boat.row()
    print(boat.check_status())
    boat.drop_anchor()
    print(boat.check_status())
    boat.row()
    print(boat.check_status())

    

