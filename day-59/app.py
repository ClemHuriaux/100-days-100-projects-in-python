from flask import Flask, render_template, request
import requests
import smtplib
import os

posts = requests.get('https://api.npoint.io/43644ec4f0013682fc0d').json()
app = Flask(__name__)

MY_EMAIL = os.environ.get('email')
MY_PASSWORD = os.environ.get('password')


@app.route('/')
def home():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:New message from your website! \n\n"
                                    f"Name: {request.form['name']} \n"
                                    f"Email: {request.form['email']} \n"
                                    f"Phone Number: {request.form['phoneNumber']} \n"
                                    f"Message: {request.form['message']}".encode('utf-8'))

        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html')


@app.route('/post/<int:index>')
def post(index):
    post_to_send = None
    for single_post in posts:
        if single_post['id'] == index:
            post_to_send = single_post
    return render_template('post.html', post=post_to_send)


if __name__ == '__main__':
    app.run(debug=True)
