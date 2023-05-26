from flask import Flask
from config import Config
from flask_cors import CORS



yala = Flask(__name__)
CORS(yala, supports_credentials=True)

yala.config.from_object(Config)

