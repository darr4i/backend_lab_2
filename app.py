from flask import Flask
from flask_restful import Api
from routes.routes import init_routes 
from utils.utils import format_response, error_response  

app = Flask(__name__)
api = Api(app)

init_routes(app)

@app.route('/')
def index():
    return {"message": "API is running!"}

if __name__ == "__main__":
    app.run(debug=True)
