from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/test"
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'hello?'

if __name__ == '__main__':
    app.run()