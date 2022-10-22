# 1. Створіть клас Vehicle з атрибутами екземпляра max_speed і mileage та методами increase_speed, break_speed,
# mileage_info
import time

print("Task 1\n")


class Vehicle:
    max_speed: int
    speed: int
    mileage: str

    def __init__(self, speed, max_speed, mileage):
        self.speed = speed
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self):
        if self.speed + 1 < self.max_speed:
            self.speed = self.speed + 1
            print(f"Speed increased to: {self.speed}")
        else:
            print(f"Maximum speed limit reached: {self.max_speed}")

    def break_speed(self):
        print("Breaking in action...\n")
        while self.speed > 0:
            self.speed = self.speed - 1
            if self.speed > 0:
                print(f"Slowing down to {self.speed}")
            else:
                print(f"Breaking finished. Vehicle stopped.")
            time.sleep(1)

    def mileage_info(self):
        print(f"Mileage is: {self.mileage}")


auto = Vehicle(10, 20, 2)
auto.increase_speed()
auto.increase_speed()
auto.increase_speed()
auto.break_speed()
auto.mileage_info()

# 2. Створіть дочірній клас Bus, який успадкує всі змінні та методи класу Vehicle і матиме власний метод
# seating_capacity

print("Task 2\n")


class Bus(Vehicle):
    seating_capacity: int

    def __init__(self, speed, max_speed, mileage, seating_capacity):
        super().__init__(speed, max_speed, mileage)
        self.seating_capacity = seating_capacity

    def show_seating_capacity(self):
        print(f"Seating capacity of the bus is: {self.seating_capacity}")


bus = Bus(20, 60, 20, 18)
bus.increase_speed()
bus.increase_speed()
bus.increase_speed()
bus.break_speed()
bus.mileage_info()
bus.show_seating_capacity()

# 3. Визначте, від якого класу успадковується клас Bus (перевірте issubclass)

# 4. Створіть екземпляр Bus під назвою school_bus і визначте, чи є school_bus об'єктом класу Vehicle/Bus
# 5. Створіть новий клас School з атрибутами екземпляра get_school_id і number_of_students та методами school_address,
# main_subject
