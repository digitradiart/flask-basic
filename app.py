from flask import Flask
app = Flask(__name__)

# SERVER ROUTING
# halaman statis
@app.route('/')
def index():
    return 'Halo lur!'

@app.route('/setting')
def show_setting():
    return 'Ini halaman berikutnya: setting'