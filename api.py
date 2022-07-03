import os
from flask import Flask
from src.blueprints.code import code_bp

SECRET_KEY = os.environ['SECRET_KEY']

app = Flask(__name__)

app.url_map.strict_slashes = False

app.register_blueprint(code_bp)

if __name__ == '__main__':
    app.run(debug=True)
