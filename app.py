import flask from flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Halo lur!'