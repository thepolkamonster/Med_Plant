import os
from werkzeug.utils import secure_filename
from models import LeafModel
from db import db
import tensorflow
from predict import predict
from label_mapping import label_mapping

#Schemas
#from schema import LeafOutputSchema


#flask 
from flask_smorest import Blueprint
from flask import render_template, redirect, url_for, request
from forms import ImageForm

#blueprints
blp = Blueprint("views", __name__, description = "Views Blueprint")

#load model
model = tensorflow.keras.models.load_model("plant_identification_model2.keras")


@blp.route('/', methods = ['GET'])
def index():
    return render_template('index.html')



@blp.route('/predict', methods=['GET', 'POST'])
#@blp.response(LeafOutputSchema)
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        pred = int(predict(file_path, model))
        #maybe the diffrence between numpy.int64 and int caused an error(correct)
        leaf_obj = LeafModel.query.get_or_404(pred+1)
        leaf = leaf_obj.name
        return leaf
    
    return None

