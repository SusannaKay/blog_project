from flask import Flask, render_template
import requests
app = Flask(__name__)

blog_url = 'https://api.npoint.io/956b4a7d6e53ce9f7f44'
response = requests.get(blog_url)
response.raise_for_status()
all_posts = response.json()

@app.route('/')
def home():
    return render_template('index.html', posts = all_posts)

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:id>')
def post(id):
    for post in all_posts:
        if post['id'] == id:
            title = post['title']
            subtitle = post['subtitle']
            body = post['body']
            img = post['image_url']
            date = post['date']
            return render_template('post.html', title=title, subtitle=subtitle, body=body,img=img, date=date)



if __name__ == '__main__':
    app.run(debug=True)