from flask import Flask, render_template
import requests
from post import Post

posts_blog = requests.get('https://api.npoint.io/5abcca6f4e39b4955965').json()
all_posts = [Post(post['id'], post['title'], post['subtitle'], post['body']) for post in posts_blog]

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:id>')
def post(id):
    for post_blog in all_posts:
        if post_blog.id == id:
            post = post_blog
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
