
#designig a matatu class
class Matatu:
    def __init__(self, route, capacity, registration_number):
        self.route = route
        self.capacity = capacity
        self.current_passengers = 0  # Initially, no passengers
        self.registration_number = registration_number

    def pick_up_passenger(self):
        if self.current_passengers < self.capacity:
            self.current_passengers += 1
            print(f"Passenger picked up. Current passengers: {self.current_passengers}")
        else:
            print("Matatu is full!")

    def drop_off_passenger(self):
        if self.current_passengers > 0:
            self.current_passengers -= 1
            print(f"Passenger dropped off. Current passengers: {self.current_passengers}")
        else:
            print("No passengers to drop off.")

    def is_full(self):
        return self.current_passengers == self.capacity

    def display_info(self):
        print(f"Route: {self.route}")
        print(f"Capacity: {self.capacity}")
        print(f"Current Passengers: {self.current_passengers}")
        print(f"Registration Number: {self.registration_number}")

    #Creating Objects (Instances) of the Matatu Class

matatu_one = Matatu("Ruiru-Nairobi", 14, "KDA 123B")
matatu_two = Matatu("Kamakis-Thika", 18, "KCB 456C")

matatu_one.display_info()
matatu_one.pick_up_passenger()
matatu_one.pick_up_passenger()
matatu_one.display_info()

matatu_two.display_info()

#inheritance

class ExpressMatatu(Matatu):  # ExpressMatatu inherits from Matatu
    def __init__(self, route, capacity, registration_number, has_music_system):
        super().__init__(route, capacity, registration_number)  # Call the parent's constructor
        self.has_music_system = has_music_system

    def play_music(self):
        if self.has_music_system:
            print("Playing some tunes!")
        else:
            print("No music system in this one.")

    def display_info(self):  # Overriding the parent's method
        super().display_info()
        print(f"Has Music System: {self.has_music_system}")

express_matatu = ExpressMatatu("Nairobi-Thika Highway", 11, "KDE 789D", True)
express_matatu.display_info()
express_matatu.pick_up_passenger()
express_matatu.play_music()