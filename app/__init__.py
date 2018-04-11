from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from threading import Lock
import numpy as np
import math
from config import *

from models import DM, Tiler, RadiusTiler, AngleTiler

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

mike = DM(name="mike")
