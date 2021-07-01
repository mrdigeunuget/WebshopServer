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
from database.tables import Product, Bestellingen, BestellingItems


bestellen, get, post, put, delete = init_routing_func('bestellen', '/bestellen/')


@post('/items')
def postItems():
    data = request.json
    message, response_code = check_request_data(data, ["bestelling_id", "product_id", "hoeveelheid"])
    if (response_code == 200):
        newItem = create_obj(BestellingItems, data)
        message = jsonify(newItem.to_dict())
    return message, response_code

@post('/open')
def openOrder():
    data = request.json
    message, response_code = check_request_data(data, ["gebruikers_id"])
    if (response_code == 200):
        order = create_obj(Bestellingen, data)
        message = jsonify(order.to_dict())
    return message, response_code




