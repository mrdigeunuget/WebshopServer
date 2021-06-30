from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, create_refresh_token,
    get_jwt_identity, get_jwt, set_access_cookies
)
from datetime import datetime, timedelta, timezone
import logging

from app import app
from app.utils import init_routing_func, check_request_data
from app.obj_utils import get_objs, get_objs_with_filter, create_obj, get_obj_with_filter, get_obj, change_product, delete_obj, delete_objs_with_filter, get_objs_distinct, get_distinct_producten, get_user_data, check_password
from database.tables import Gebruikers, Product, Winkelwagen, Bestellingen, BestellingItems, Maat, Kleur, Favoriet


login, get, post, put, delete = init_routing_func('login', '/login/')


@get('/gebruikers')
def getGebruikers():
    gebruikers=get_objs(Gebruikers)
    return jsonify(gebruikers),200

@post('/user/create')
def createUser():
    data = request.json
    message, response_code = check_request_data(data,
                                                ["voornaam", "achternaam", "email", "wachtwoord", "straatnaam", "huisnummer", "postcode"])
    if (response_code == 200):
        newProduct = create_obj(Gebruikers, data)
        # optioneel om ook weer het product te zien die aangemaakt wordt
        message = jsonify(newProduct.to_dict())
    return message, response_code


@get('/<string:usr>')
def getUserData(usr):
    user = get_user_data(Gebruikers, email = usr)
    if (user != None):
        return jsonify(user)
    else:
        return jsonify(user),401

@get('/<string:usr>/<string:pwd>')
def checkPassword(usr, pwd):
    check = check_password(Gebruikers, email = usr, wachtwoord = pwd)
    if(check):
        return jsonify(check),200
    else:
        return jsonify(check),401

