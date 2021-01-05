import requests
from datetime import datetime
import dateutil.parser as parse_date
import smtplib
import time

MY_LAT = 46.227638
MY_LONG = 2.213749
my_email = "pythontestprojects@gmail.com"
password = "066y068nwMHnZA1b7Og4"  # I changed the password, it's not correct. Don't waste your time trying ;)


def is_iss_close():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    longitude = float(data_iss["iss_position"]["longitude"])
    latitude = float(data_iss["iss_position"]["latitude"])
    iss_position = (longitude, latitude)
    my_position = (MY_LONG, MY_LAT)
    to_return = [pos for pos in zip(iss_position, my_position) if
                 int(pos[1]) in range(int(pos[0] - 5), int(pos[0] + 5))]
    return True if len(to_return) > 1 else False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}


def is_dark_now():
    response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_sun.raise_for_status()
    data_sun = response_sun.json()

    sunrise = parse_date.parse(data_sun["results"]["sunrise"])
    sunset = parse_date.parse(data_sun["results"]["sunset"])
    time_now = datetime.now()
    return False if time_now.hour() in range(sunrise.hour, sunset.hour) else True


while True:
    time.sleep(secs=60)
    if is_iss_close() and is_dark_now():
        with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:ISS is coming  ! \n\n"
                                    f"Look up dude ! ISS is coming ! Clem ;)".encode('utf-8'))



