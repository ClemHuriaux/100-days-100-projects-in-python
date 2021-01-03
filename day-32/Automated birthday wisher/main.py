##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import smtplib
import random as r
import glob
import os
WORD_TO_REPLACE = "[NAME]"
my_email = "pythontestprojects@gmail.com"
password = "066y068nwMHnZA1b7Og4"  # I changed the password, it's not correct. Don't waste your time trying ;)
# 1. Update the birthdays.csv
df_birthday = pd.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now().date()
today_birthday = df_birthday[(df_birthday.month == today.month) & (df_birthday.day == today.day)]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv

all_letters = [os.path.basename(x) for x in glob.glob('letter_templates/*.txt')]
for index, row in today_birthday.iterrows():
    letter_sample = r.choice(all_letters)
    with open(f"letter_templates/{letter_sample}", "r") as letter:
        letter_content = letter.read()
    letter_content = letter_content.replace(WORD_TO_REPLACE, row['name'])

# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=row["email"],
                            msg=f"Subject:Happy Birthday ! \n\n"
                                f"{letter_content}".encode('utf-8'))






