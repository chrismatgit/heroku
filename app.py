from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'ok ! my first change'

if __name__ == "__main__":
    app.run() 
