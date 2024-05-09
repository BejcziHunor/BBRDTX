# Bejczi Hunor Bence
# Mérnökinformatika
# BBRDTX

from datetime import datetime, timedelta

class HotelBookingSystem:
    def __init__(self, hotel_name):
        self.hotel_name = hotel_name
        self.rooms = {'101': 'Egy ágyas', '102': 'Két ágyas', '103': 'Egy ágyas'}  
        self.bookings = {}

    def make_booking(self, room_number, check_in_date, check_out_date, customer_name, customer_email):
        if room_number not in self.rooms:
            print("Nincs ilyen szoba az adott szállodában.")
            return False
        
        
        for booking_info in self.bookings.values():
            existing_room_number = booking_info[0]
            existing_check_in = booking_info[1]
            existing_check_out = booking_info[2]
            if room_number == existing_room_number and (check_in_date < existing_check_out and check_out_date > existing_check_in):
                print("A szoba már foglalt ezen az időponton.")
                return False
        
        
        booking_duration = (check_out_date - check_in_date).days
        room_type = self.rooms[room_number]
        if isinstance(room_type, tuple):
            room_type = room_type[2]  
        if room_type == 'Egy ágyas':
            booking_price = booking_duration * 5000
        elif room_type == 'Két ágyas':
            booking_price = booking_duration * 10000
        else:
            print("Ismeretlen szoba típus.")
            return False
        
        self.rooms[room_number] = (check_in_date, check_out_date, room_type, booking_price) 
        self.bookings[(room_number, check_in_date)] = (room_number, check_in_date, check_out_date, booking_price, customer_name, customer_email)  
        print(f"Foglalás sikeresen létrehozva. A kivánt időre a foglalás ára: {booking_price} Ft")
        return True



    def cancel_booking(self, room_number, check_in_date):
        if (room_number, check_in_date) not in self.bookings:
            print("Nincs ilyen foglalás.")
            return False
        
        del self.bookings[(room_number, check_in_date)]
        self.rooms[room_number] = None
        print("Foglalás sikeresen törölve.")
        return True

    def list_bookings(self):
        if not self.bookings:
            print("Nincs aktív foglalás.")
            return
        print("Aktív foglalások:")
        for booking in self.bookings.values():
            room_number = booking[0]
            room_type = self.rooms[room_number][2]  
            check_in_date = booking[1].strftime("%Y-%m-%d")
            check_out_date = booking[2].strftime("%Y-%m-%d")
            customer_name = booking[4]
            customer_email = booking[5]
            print(f"Szoba: {room_number}, Típus: {room_type}, Check-in: {check_in_date}, Check-out: {check_out_date}, Ügyfél név: {customer_name}, Ügyfél email: {customer_email}")

    def list_available_rooms_and_dates(self):
        print("Elérhető szobák és időpontok:")
        for room_number, room_type in self.rooms.items():  
            if room_type is None:
                print(f"Szoba: {room_number}")
            else:
                if isinstance(room_type, tuple):  
                    print(f"Szoba: {room_number}, Típus: {room_type[2]}")  
                else:
                    print(f"Szoba: {room_number}, Típus: {room_type}")


def main():
    print("Válassz szállodát:")
    print("1. Hotel Visegrád")
    hotel_choice = input("Szálloda kiválasztása: ")

    if hotel_choice == '1':
        hotel_name = "Hotel Visegrád"
    else:
        print("Érvénytelen választás.")
        return

    hotel_system = HotelBookingSystem(hotel_name)
    
    
    bookings = [
        {'room_number': '101', 'check_in_date': datetime(2024, 5, 15), 'check_out_date': datetime(2024, 5, 17), 'customer_name': 'Kovács Géza', 'customer_email': 'geza1982@gmail.com'},
        {'room_number': '102', 'check_in_date': datetime(2024, 5, 18), 'check_out_date': datetime(2024, 5, 20), 'customer_name': 'Kis Alíz', 'customer_email': 'kis.aliz2000@example.com'},
        {'room_number': '103', 'check_in_date': datetime(2024, 5, 21), 'check_out_date': datetime(2024, 5, 23), 'customer_name': 'Buják József', 'customer_email': 'bujak.joci12@hotmail.com'},
        {'room_number': '101', 'check_in_date': datetime(2024, 5, 24), 'check_out_date': datetime(2024, 5, 26), 'customer_name': 'Szabados Erika', 'customer_email': 'szabados.erika@example.com'},
        {'room_number': '102', 'check_in_date': datetime(2024, 5, 27), 'check_out_date': datetime(2024, 5, 29), 'customer_name': 'Tóth Piroska', 'customer_email': 'toth.piroska1@example.com'}
    ]

    
    for booking in bookings:
        room_number = booking['room_number']
        check_in_date = booking['check_in_date']
        check_out_date = booking['check_out_date']
        customer_name = booking['customer_name']
        customer_email = booking['customer_email']
        hotel_system.make_booking(room_number, check_in_date, check_out_date, customer_name, customer_email)

    
    while True:
        print("\nVálassz műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        choice = input("Választott művelet: ")

        if choice == '1':
            hotel_system.list_available_rooms_and_dates()
            room_number = input("Kérlek, add meg a szoba számát: ")
            check_in_date = datetime.strptime(input("Kérlek, add meg a bejelentkezés dátumát (YYYY-MM-DD): "), "%Y-%m-%d")
            check_out_date = datetime.strptime(input("Kérlek, add meg a kijelentkezés dátumát (YYYY-MM-DD): "), "%Y-%m-%d")
            customer_name = input("Kérlek, add meg az ügyfél nevét: ")
            customer_email = input("Kérlek, add meg az ügyfél email címét: ")
            hotel_system.make_booking(room_number, check_in_date, check_out_date, customer_name, customer_email)
        elif choice == '2':
            room_number = input("Kérlek, add meg a szoba számát: ")
            check_in_date = datetime.strptime(input("Kérlek, add meg a bejelentkezés dátumát (YYYY-MM-DD): "), "%Y-%m-%d")
            hotel_system.cancel_booking(room_number, check_in_date)
        elif choice == '3':
            hotel_system.list_bookings()
        elif choice == '4':
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()
