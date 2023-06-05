from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json
from flask_csp.csp import csp_header

csp = {
    'default-src': 
        "'self'",
    'img-src': 
        '\'self\' data:',
    'style-src': 
        '\'self\' \'unsafe-inline\' https://fonts.googleapis.com/ https://unpkg.com/ https://cdn.jsdelivr.net/',
    'script-src': '\'self\' \'unsafe-inline\' https://code.jquery.com/ https://cdn.jsdelivr.net/ https://cdnjs.cloudflare.com/',
    'font-src': '\'self\' https://fonts.googleapis.com/ https://cdn.jsdelivr.net/ https://unpkg.com/' ,
    'connect-src': '\'self\''
}


views = Blueprint('views', __name__)

@views.route('/')
@csp_header(csp)
@login_required
def home():

    return render_template("template.html", user=current_user)
