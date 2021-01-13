from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

data = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

data_list = data.get_data_from_api()
for destination in data_list:
    if not destination['iataCode']:
        destination['iataCode'] = FlightSearch().search(destination["city"])
        data.fill_iata_code(destination)

today = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(6 * 30)

for destination in data_list:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=today,
        to_time=six_month_from_today,
    )
    if not flight:
        continue

    if flight.price <= destination['lowestPrice']:
        users = data.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        notification_manager.send_emails(emails, message, link)


def get_user_info():
    user = {"first name": input("What is your first name?\n"),
            "last name": input("What is your last name?\n"),
            "email": input("What is your email?\n")}
    confirm_email = input("Confirm your email: \n")
    if user["email"] == confirm_email:
        return user
    else:
        raise ValueError("Email doesn't match! Try again !")


#  user_info = get_user_info()
#  data.fill_users_doc(user_info)
