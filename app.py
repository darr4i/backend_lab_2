from flask import Flask
from flask_restful import Api

from models.models import User, Category, Record

from flask import Flask
from flask_restful import Api
from routes.routes import init_routes

app = Flask(__name__)
api = Api(app)

init_routes(app)

if __name__ == "__main__":
    app.run(debug=True)


app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return {"message": "API is running!"}

if __name__ == "__main__":
    app.run(debug=True)
