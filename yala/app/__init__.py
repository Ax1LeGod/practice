from flask import Flask
from config import Config

yala = Flask(__name__)
yala.config.from_object(Config)
