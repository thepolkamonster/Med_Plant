from flask import render_template, Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('index.html')
