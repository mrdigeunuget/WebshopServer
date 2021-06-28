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


home, get, post, put, delete = init_routing_func('home', '/home/')

@get('/gebruikers')
def getGebruikers():
    gebruikers=get_objs(Gebruikers)
    return jsonify(gebruikers),200

@get('/product')
def getProducts():
    product=get_objs(Product)
    return jsonify(product),200

@get('/product/<string:name_id>')
def getProductsByName(name_id):
    product=get_objs_with_filter(Product, naam=name_id)
    return jsonify(product),200

@get('/product/<int:product_id>')
def getProductById(product_id):
    product=get_obj_with_filter(Product, id=product_id)
    return jsonify(product),200

@get('/allProduct')
def getDistinctProducten():
    product = get_distinct_producten(Product)
    return jsonify(product),200

@delete('/delete/<int:product_id>')
def deleteProduct(product_id):
    obj = delete_objs_with_filter(Product, id=product_id)
    return jsonify(obj),200

@get('/product/<string:product_categorie>/<string:product_naam>')
def getProductByCategorieAndName(product_naam, product_categorie):
    product=get_objs_with_filter(Product, naam=product_naam, categorie=product_categorie)
    return jsonify(product),200

@get('/product/<string:product_categorie>/<string:product_naam>/<string:product_kleur>/<string:product_maat>')
def getFirstProduct(product_naam, product_categorie, product_kleur, product_maat):
    product=get_obj_with_filter(Product, naam=product_naam, categorie=product_categorie, kleur=product_kleur, maat=product_maat)
    return jsonify(product),200

@get('/products/<string:product_categorie>')
def getProductsByCategorie(product_categorie):
    product=get_objs_with_filter(Product, categorie = product_categorie)
    return jsonify(product),200


@get('/product/kleuren')
def getKleuren():
    kleuren = get_objs_distinct(Kleur.kleur)
    return jsonify(kleuren), 200

@get('/product/maten')
def getMaten():
    maten = get_objs_distinct(Maat.maat)
    return jsonify(maten), 200

@post('/product/create')
def createProduct():
    data = request.json
    message, response_code = check_request_data(data, ["naam", "categorie", "maat", "kleur", "prijs", "voorraad", "body", "imagePath", "manufacturer", "model"])
    if (response_code == 200):
        newProduct = create_obj(Product, data)
        #optioneel om ook weer het product te zien die aangemaakt wordt
        message = jsonify(newProduct.to_dict())
    return message, response_code

@put('/product/update')
def updateProduct():
    data = request.json
    message, response_code = check_request_data(data,
                                                ["id", "naam", "categorie", "maat", "kleur", "prijs", "voorraad", "body",
                                                 "imagePath", "manufacturer", "model"])
    if (response_code == 200):
        newProduct = change_product(Product, data)
        # optioneel om ook weer het product te zien die aangemaakt wordt
        message = jsonify(newProduct.to_dict())
    return message, response_code


@post('/login')
def parse_request():
    data = request.json
    message, response_code = check_request_data(data,
                                                ["email" , "wachtwoord"])
    logging.warning(data)
    if(response_code == 200):
        checkUser = get_obj_with_filter(Gebruikers, data)
        logging.warning(checkUser)
        access_token = create_access_token(identity=checkUser['id'])
        resp = jsonify({'login':True})
        logging.warning(access_token)
        set_access_cookies(resp,access_token)
        return resp,200
    else:
        return jsonify({'error':'incorrect credentials'}), 401

@get('/userdata/<string:usr>')
def getUserData(usr):
    user = get_user_data(Gebruikers, email = usr)
    if (user != None):
        return jsonify(user)
    else:
        return jsonify(user),401

@get('/login/<string:usr>/<string:pwd>')
def checkPassword(usr, pwd):
    check = check_password(Gebruikers, email = usr, wachtwoord = pwd)
    if(check):
        return jsonify(check),200
    else:
        return jsonify(check),401





