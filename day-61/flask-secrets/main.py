from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

EMAIL = 'admin@email.com'
PASSWORD = '12345678'


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email("Invalid email address")])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(8, message="Field must be at least "
                                                                                             "8 characters long")])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = "aze12s54d88z1qsd3215zaez9q5s6d4"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == EMAIL and login_form.password.data == PASSWORD:
            return render_template('success.html')
        return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
