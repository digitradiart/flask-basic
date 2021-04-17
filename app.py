from flask import Flask, render_template, request
app = Flask(__name__)

# SERVER ROUTING
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<username>')
def show_profile(username):
    return render_template('profile.html', user=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Email kamu adalah ' + request.form['email'] + '\nPassword kamu adalah ' + request.form['password']
    return render_template('login.html')