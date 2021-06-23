from flask import Flask,render_template, request,json,jsonify,make_response,redirect
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, create_refresh_token,
    get_jwt_identity, set_access_cookies, set_refresh_cookies,
    get_jwt,unset_jwt_cookies,unset_access_cookies
)
from datetime import timedelta
import json

from app import app
from app.utils import init_routing_func, check_request_data
from app.obj_utils import get_objs, get_objs_with_filter, create_obj, get_obj_with_filter, get_obj, change_product, delete_obj, delete_objs_with_filter
from database.tables import Gebruikers, Product, Winkelwagen, Bestellingen, BestellingItems, Maat, Kleur, Favoriet


from data import *



app = Flask(__name__)
app.config['BASE_URL'] = 'http://127.0.0.1:8081'  #Running on localhost
app.config['JWT_SECRET_KEY'] = 'ICTVT20WMS'  # Change this!
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=3600)

app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
jwt = JWTManager(app)

def check_if_token_is_revoked(jwt_header,jwt_payload):
    jti = decrypted_token['jti']
    return get_blacklist_token(jti)

@app.route('/', methods=['get'])
def index():
    return render_template("index.html")

@app.route('/geheim', methods=['get'])
@jwt_required()
def geheim():
    return render_template('geheim.html')


@app.route('/login', methods=['get'])
def login_form():
    return render_template('login_form.html')

# @app.route('/login', methods=['post'])




@app.route('/logout', methods=['get'])
@jwt_required()
def logout():
    resp = make_response(redirect(app.config['BASE_URL']+'/',302))
    unset_jwt_cookies(resp)
    return resp