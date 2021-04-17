from flask import Flask, render_template
app = Flask(__name__)

# SERVER ROUTING
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<username>')
def show_profile(username):
    # return 'Kamu berada di halaman profile user: %s' % username
    return render_template('profile.html', user=username)