from flask import Flask, render_template
app = Flask(__name__)

# SERVER ROUTING
# halaman statis
@app.route('/')
def index():
    # return 'Halo lur!'

@app.route('/setting')
def show_setting():
    return 'Ini halaman berikutnya: setting'

# halaman dinamis, misal profil dari user
@app.route('/profile/<username>')
def show_profile(username):
    return 'Kamu berada di halaman profile user: %s' % username

# halaman dinamis, blog ID
@app.route('/blog/<int:blog_id>')
def show_blog(blog_id):
    return 'Kamu berada di blog nomor-%d' %blog_id