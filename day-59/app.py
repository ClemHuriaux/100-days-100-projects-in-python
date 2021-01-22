from flask import Flask, render_template
import requests

posts = requests.get('https://api.npoint.io/43644ec4f0013682fc0d').json()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
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
