from flask import Flask
from flask_restful import Api

from models.models import User, Category, Record

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return {"message": "API is running!"}

if __name__ == "__main__":
    app.run(debug=True)
