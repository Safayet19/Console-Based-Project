class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0
    
    def available_seats(self):
        return self.total_seats - self.booked_seats
    
    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            print("Seat Booked Successfully.")
            return True
        else:
            print("No seats available")
            return False


class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus

class Admin:
    def __init__(self):
        self.__username = "safayet"
        self.__password = "safayet"
        self.logged_in = False
    
    def login(self, user, pas):
        if (self.__username == user) and (self.__password == pas):
            self.logged_in = True
            print("Successfully Logged in")
            return True
        else:
            print("Invalid username or password.")
            return False
        
    def admin_menu(self, system):
        while self.logged_in:
            print("\n--- Admin Menu ---")
            print("1. Add Bus")
            print("2. View All Buses")
            print("3. View Booked Tickets for a Bus")
            print("4. Logout")
            choice = input("Enter choice: ")
            if choice == '1':
                number = input("Enter bus number: ")
                route = input("Enter route: ")
                seats = int(input("Enter total seats: "))
                system._add_bus(number, route, seats)
            elif choice == '2':
                system.show_buses()
            elif choice == '3':
                bus_number = input("Enter bus number to view booked tickets: ")
                system.view_booked_tickets(bus_number)
            elif choice == '4':
                self.logged_in = False
                print("Logged out successfully.")
            else:
                print("Invalid choice. Try again.")

class BusSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []
        self.admin = Admin()
    
    def _add_bus(self, number, route, seats):
        new_bus = Bus(number, route, seats)
        self.buses.append(new_bus)
        print("Bus Added Successfully")
    
    def find_bus(self, number):
        for bus in self.buses:
            if bus.number == number:
                return bus
        print("Bus not found")
        return None
    
    def book_ticket(self, bus_number, name, phone):
        bus = self.find_bus(bus_number)
        if bus and bus.book_seat():
            passenger = Passenger(name, phone, bus)
            self.passengers.append(passenger)
            print(f"Ticket booked for {name}. Fare: 500")
    
    def show_buses(self):
        if not self.buses:
            print("No buses available.")
        else:
            print("\nAvailable Buses:")
            for bus in self.buses:
                print(f"Bus Number: {bus.number}, Route: {bus.route}, Available Seats: {bus.available_seats()}")
    
    def view_booked_tickets(self, bus_number):
        bus = self.find_bus(bus_number)
        if bus:
            print(f"Booked tickets for Bus {bus_number}:")
            for passenger in self.passengers:
                if passenger.bus == bus:
                    print(f"Name: {passenger.name}, Phone: {passenger.phone}")
        else:
            print("Bus not found.")
    
    def cancel_ticket(self, bus_number, name, phone):
        bus = self.find_bus(bus_number)
        if bus:
            for passenger in self.passengers:
                if passenger.bus == bus and passenger.name == name and passenger.phone == phone:
                    self.passengers.remove(passenger)
                    bus.booked_seats -= 1
                    print(f"Ticket cancelled for {name}.")
                    return
            print("Passenger not found.")
        else:
            print("Bus not found.")

LalSobuj = BusSystem()

while True:
    print("\n--- Main Menu ---")
    print("1. Admin Login")
    print("2. Book Ticket")
    print("3. View Buses")
    print("4. Cancel Ticket")
    choice = input("Enter choice: ")
    
    if choice == '1':
        user = input("Enter username: ")
        pwd = input("Enter password: ")
        if LalSobuj.admin.login(user, pwd):
            LalSobuj.admin.admin_menu(LalSobuj)
    
    elif choice == '2':
        bus_number = input("Enter bus number: ")
        name = input("Enter your name: ")
        phone = input("Enter phone number: ")
        LalSobuj.book_ticket(bus_number, name, phone)
   
    elif choice == '3':
        LalSobuj.show_buses()

    elif choice == '4':
        bus_number = input("Enter bus number: ")
        name = input("Enter your name: ")
        phone = input("Enter phone number: ")
        LalSobuj.cancel_ticket(bus_number, name, phone)
    
    else:
        print("Invalid choice. Try again.")
