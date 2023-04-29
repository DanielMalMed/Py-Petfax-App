from flask import Blueprint, render_template
import json 

factbp = Blueprint('fact', __name__, url_prefix="/facts")

@factbp.route('/')
def index(): 
    return render_template('facts.html')


