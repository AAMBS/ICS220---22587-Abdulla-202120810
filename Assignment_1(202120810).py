class Customer:
    def __init__(self, custid, fname, lname, email, mobile_num, location, nationality, dob):
        self.custid = custid
        self.fname = fname
        self.lname = lname
        self.email = email
        self.mobile_num = mobile_num
        self.location = location
        self.nationality = nationality
        self.dob = dob

    def get_custid(self):
        return self.custid

    def set_custid(self, custid):
        self.custid = custid

    def get_fname(self):
        return self.fname

    def set_fname(self, fname):
        self.fname = fname

    def get_lname(self):
        return self.lname

    def set_lname(self, lname):
        self.lname = lname

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_mobile_num(self):
        return self.mobile_num

    def set_mobile_num(self, mobile_num):
        self.mobile_num = mobile_num

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_nationality(self):
        return self.nationality

    def set_nationality(self, nationality):
        self.nationality = nationality

    def get_dob(self):
        return self.dob

    def set_dob(self, dob):
        self.dob = dob

    def new_data(self, updated_custid="N/A", updated_fname="N/A", updated_lname="N/A", updated_email="N/A", updated_mobile_num="N/A", updated_location="N/A", updated_nationality="N/A", updated_dob="N/A"):
        if updated_custid:
            self.set_custid(updated_custid)
        if updated_fname and updated_lname:
            self.set_fname(updated_fname)
            self.set_lname(updated_lname)
        if updated_mobile_num and updated_location:
            self.set_location(updated_location)
            self.set_mobile_num(updated_mobile_num)
        if updated_dob:
            self.set_dob(updated_dob)
        return "\nThe prior data has been updated with new information, thank you!"

    def added_customer(self):
        return f"\nThe customer {self.custid} is currently registered to the Hotel's system with the name {self.fname} {self.lname}"

    def complete_room(self):
        return f"\nThe customer {self.fname} {self.lname} has successfully confirmed their registration for a room"

    def incomplete_room(self):
        return f"\nThe customer {self.fname} {self.lname} could not register for a room, due to that room being occupied"


class Booking:
    def __init__(self, customer, enter_day, exit_day, num_of_rooms, price, description, booking_id, discount):
        self.customer = customer
        self.enter_day = enter_day
        self.exit_day = exit_day
        self.num_of_rooms = num_of_rooms
        self.price = price
        self.description = description
        self.booking_id = booking_id
        self.discount = discount

    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer

    def get_enter_day(self):
        return self.enter_day

    def set_enter_day(self, enter_day):
        self.enter_day = enter_day

    def get_exit_day(self):
        return self.exit_day

    def set_exit_day(self, exit_day):
        self.exit_day = exit_day

    def get_num_of_rooms(self):
        return self.num_of_rooms

    def set_num_of_rooms(self, num_of_rooms):
        self.num_of_rooms = num_of_rooms

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_booking_id(self):
        return self.booking_id

    def set_booking_id(self, booking_id):
        self.booking_id = booking_id

    def get_discount(self):
        return self.discount

    def set_discount(self, discount):
        self.discount = discount

    def state_booking(self):
        return f"\nThe customer {self.customer.fname} {self.customer.lname} has confirmed their booking and will be staying on {self.enter_day} and checking out on {self.exit_day}."

    def state_booking_invalid(self):
        return f"\nThe state of booking is invalid due to the room being unavailable, Please try again."

    def find_price(self, discount=0, days=0, rate_of_room=0, tax_rate=0.5):
        calculated_price = rate_of_room * days * (1 - discount)
        total_amount = calculated_price * tax_rate
        self.price = calculated_price + total_amount
        return f"\nThe total price for your booking is {self.price} AED!"

    def receipt(self):
        return f"\nThe receipt of this booking has been sent to {self.customer.email}! \nThank you for your booking! {self.customer.fname} {self.customer.lname}"

    def receipt_unsuccessful(self):
        return f"\nThe receipt of this booking is unsuccessful, details sent to {self.customer.email}"


class Total_Fees:
    def __init__(self, receipt_id="", total_price="", discount="", date_of_payment="", tax_rate="", booking_id="", transaction_status="", fname="", lname=""):
        self.receipt_id = receipt_id
        self.total_price = total_price
        self.discount = discount
        self.date_of_payment = date_of_payment
        self.tax_rate = tax_rate
        self.booking_id = booking_id
        self.transaction_status = transaction_status
        self.fname = fname
        self.lname = lname

    def get_receipt_id(self):
        return self.receipt_id

    def set_receipt_id(self, receipt_id):
        self.receipt_id = receipt_id

    def get_total_price(self):
        return self.total_price

    def set_total_price(self, total_price):
        self.total_price = total_price

    def get_discount(self):
        return self.discount

    def set_discount(self, discount):
        self.discount = discount

    def get_date_of_payment(self):
        return self.date_of_payment

    def set_date_of_payment(self, date_of_payment):
        self.date_of_payment = date_of_payment

    def get_tax_rate(self):
        return self.tax_rate

    def set_tax_rate(self, tax_rate):
        self.tax_rate = tax_rate

    def get_booking_id(self):
        return self.booking_id

    def set_booking_id(self, booking_id):
        self.booking_id = booking_id

    def get_transaction_status(self):
        return self.transaction_status

    def set_transaction_status(self, transaction_status):
        self.transaction_status = transaction_status

    def payment_received(self):
        return f"\nThe payment has been received, this is your invoice ID: {self.receipt_id}"

    def transaction_date(self):
        return f"\nThe payment has been completed on the date: {self.date_of_payment}"

    def transaction_cancelled(self):
        self.set_transaction_status(
            "Your payment is either cancelled or will be replaced into your account")
        return f"\nReceipt ID: {self.receipt_id} is either cancelled or will be repaid to your account. Thank you!"

    def receipt_status(self):
        return self.transaction_status


class Available_Rooms:
    def __init__(self, rate_of_room, days, view, free_room, internet, room_rank, rooms_number, items_in_room):
        self.rate_of_room = rate_of_room
        self.days = days
        self.view = view
        self.free_room = free_room
        self.internet = internet
        self.room_rank = room_rank
        self.rooms_number = rooms_number
        self.items_in_room = items_in_room

    def get_rate_of_room(self):
        return self.rate_of_room

    def set_rate_of_room(self, rate_of_room):
        self.rate_of_room = rate_of_room

    def get_days(self):
        return self.days

    def set_days(self, days):
        self.days = days

    def get_view(self):
        return self.view

    def set_view(self, view):
        self.view = view

    def is_free_room(self):
        return self.free_room

    def set_free_room(self, free_room):
        self.free_room = free_room

    def has_internet(self):
        return self.internet

    def set_internet(self, internet):
        self.internet = internet

    def get_room_rank(self):
        return self.room_rank

    def set_room_rank(self, room_rank):
        self.room_rank = room_rank

    def get_rooms_number(self):
        return self.rooms_number

    def set_rooms_number(self, rooms_number):
        self.rooms_number = rooms_number

    def get_items_in_room(self):
        return self.items_in_room

    def set_items_in_room(self, items_in_room):
        self.items_in_room = items_in_room

    def check_if_room_empty(self):
        return f"\nThe room {self.rooms_number} is currently available!"

    def occupied_room(self):
        return f"\nThe room with the number {self.rooms_number} is now occupied!"

    def taking_inputs_from_user(self):
        # This is supposed to be a function that takes inputs from user to then implement it into the code
        pass


print("--~~Booking Information~~--")

customer1 = Customer(custid=99, fname="Abdulla", lname="Bin Safwan", email="202120810@zu.ac.ae",
                     mobile_num="0509977450", location="Abu Dhabi", nationality="United Arab Emirates", dob="5-7-2004")

booking1 = Booking(customer=customer1, enter_day="20-9-2024", exit_day="25-9-2024", num_of_rooms=1,
                   price=1500, description="This room is a Penthouse Suite!", booking_id=1111, discount=0.1)

room1 = Available_Rooms(rate_of_room=1500, days=5, view="The view is overlooking the Ocean!", free_room=True, internet=True,
                        room_rank="Pent House", rooms_number=186, items_in_room=["TV", "Mini-Kitchen", "Internet", "Espresso Machine"])


total_fees1 = Total_Fees(receipt_id="A0909211234", total_price=450, discount=0.1, date_of_payment="29-9-2024",
                         tax_rate=0.05, booking_id=booking1.booking_id, transaction_status="Paid",
                         fname=customer1.fname, lname=customer1.lname)


print(customer1.added_customer())
print(room1.check_if_room_empty())
print(customer1.new_data(updated_fname="Abdulla Ahmed", updated_lname="Bin Safwan", updated_dob="5-7-2003",
                         updated_custid="109"))
print(customer1.complete_room())
print(booking1.state_booking())
print(booking1.find_price(rate_of_room=150, days=5, discount=0.1, tax_rate=0.05))
print(total_fees1.transaction_date())
print(total_fees1.payment_received())
print(booking1.receipt())

print("---------------~~~~~~~~~~~~~~~~~~~~~~-----------------------")

customer2 = Customer(custid=100, fname="Mohammed", lname="Bin Safwan", email="abs25149@gmail.com",
                     mobile_num="054241661", location="Abu Dhabi", nationality="United States Of America", dob="25-5-2005")

booking2 = Booking(customer=customer2, enter_day="30-9-2024", exit_day="2-10-2024", num_of_rooms=1,
                   price=150, description="This room is a Standard Suite!", booking_id=1131, discount=0.1)

room2 = Available_Rooms(rate_of_room=150, days=3, view="The view is overlooking our swimming pool!", free_room=True, internet=True,
                        room_rank="Pent House", rooms_number=201, items_in_room=["TV", "Mini-Kitchen", "Internet", "Espresso Machine"])


total_fees2 = Total_Fees(receipt_id="A0909211245", total_price=250, discount=0.3, date_of_payment="29-9-2024",
                         tax_rate=0.05, booking_id=booking2.booking_id, transaction_status="Cancelled, refunded payment",
                         fname=customer2.fname, lname=customer2.lname)


print(customer2.added_customer())
print(customer2.new_data(updated_fname="Mohamed Ahmed", updated_lname="Bin Safwan", updated_dob="25-4-2005",
                         updated_custid="132"))
print(room2.occupied_room())
print(customer2.incomplete_room())
print(booking2.state_booking_invalid())
print(total_fees2.transaction_date())
print(total_fees2.transaction_cancelled())
print(booking2.receipt_unsuccessful())

print("---------------~~~~~~~~~~~~~~~~~~~~~~-----------------------")
