# Import Dependencies
import datetime as dt
import numpy as np
import pandas as pd

# Dependencies needed for sqlalchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Flask Dependencies
from flask import Flask, jsonify

# Setting Up Database
## Retrieving access and query database files
engine = create_engine('sqlite:///hawaii.sqlite')

## Reflecting database into our classes
Base = automap_base()

Base.prepare(engine, reflect = True)

## References to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

## Session link
session = Session(engine)

## Defining and setting up flask app
app = Flask(__name__)

import app

# Defining the route
@app.route('/')
# Creating route function
def welcome():
    return ('''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end''')
