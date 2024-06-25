from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/1278f8eb1c73bfc2906f"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    author = 'Nolan Brand'
    dates = datetime.today().strftime('%Y-%m-%d')

    return render_template("index.html", posts=all_posts, author=author, dates=dates)


@app.route('/about')
def get_about():
    return render_template("about.html")


@app.route('/contact')
def get_contact():
    return render_template("contact.html")


@app.route('/post/<post_num>')
def get_blog(post_num):
    blog_url = "https://api.npoint.io/1278f8eb1c73bfc2906f"
    response = requests.get(url=blog_url)
    all_posts = response.json()

    blog = all_posts[(int(post_num) - 1)]

    title = blog['title']
    subtitle = blog['subtitle']
    body = blog['body']
    author = 'Nolan Brand'
    dates = datetime.today().strftime('%Y-%m-%d')

    return render_template("post.html", posts=all_posts, title=title, subtitle=subtitle, author=author, dates=dates, body=body)


if __name__ == "__main__":
    app.run(debug=True)
