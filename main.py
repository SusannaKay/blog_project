from flask import Flask, render_template
import requests


app = Flask(__name__)

blog_url ='https://api.npoint.io/c790b4d5cab58020d391'
response = requests.get(blog_url)
response.raise_for_status()
all_posts = response.json()
print(all_posts)

@app.route('/')
def home():
    
    return render_template("index.html", all_posts=all_posts)

@app.route('/post/<int:id>')
def get_post(id):
    for post in all_posts:
        if post['id'] == id:
            title = post['title']
            subtitle = post['subtitle']
            body = post['body']


    return render_template('post.html', title=title, subtitle=subtitle,body=body)

if __name__ == "__main__":
    app.run(debug=True)
