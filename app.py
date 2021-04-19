from flask import Flask, render_template, request
app = Flask(__name__)

# SERVER ROUTING
@app.route('/')
def index():
    search = request.args.get('search') 
    video = request.args.get('video')
    if not search: #dictionary
        return render_template('index.html')

    return 'hasil search adalah ' + search + ' dan video nomor ' + video

@app.route('/profile/<username>')
def show_profile(username):
    return render_template('profile.html', user=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Email kamu adalah ' + request.form['email'] + '\nPassword kamu adalah ' + request.form['password']
    return render_template('login.html')