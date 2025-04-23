import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello from Flask on Heroku!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT",500))
    # app.run(debug=True)
    app.run(host='0.0.0.0',port=port)
