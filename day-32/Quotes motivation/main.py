import smtplib
import datetime as dt
import random as r

my_email = "pythontestprojects@gmail.com"
password = "066y068nwMHnZA1b7Og4"  # I changed the password, it's not correct. Don't waste your time trying ;)

now = dt.datetime.now()
if now.weekday() == 6:
    with open("quotes.txt", "r", encoding="utf8") as f:
        file_content = f.read().splitlines()

    quote_choice = r.choice(file_content)
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Sunday motivation\n\n"
                                f"{quote_choice}".encode('utf-8'))



