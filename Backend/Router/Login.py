import traceback
import json

from flask import Blueprint, request

login_bp = Blueprint('Data', __name__, url_prefix='/api/data')


@data_bp.route('/login', methods=('POST',))
def login():
    try:


        return json.dumps({"result": True})
    except:
        traceback.print_exc()
        return json.dumps({"result": False, "error": 0, "msg": traceback.format_exc()})
