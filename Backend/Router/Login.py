import traceback
import json
from flask import Flask, Blueprint, request , session
from Backend.Utils.Database import Database
from Backend.Utils.validation import Validation


login_bp = Blueprint('User', __name__, url_prefix='/api/user')

CHECK_DB = Database()
CHECK_ID = Validation()

'''
@login_bp.route('/' ,methods =('POST',))
def home():
    if 'userid' in session:
        userid = session['userid']
'''


@login_bp.route('/login', methods=('POST',))
def login():
    try:
        if request.method == 'POST':
            rq_js = request.args.get()

            id = rq_js['id']
            pw = rq_js['pw']

                                      # 아이디 , 비밀번호 체크후 넘기기
            if not (CHECK_ID.id_validation(id) and CHECK_ID.pw_validation(pw)):
                # 아이디 , 비밀번호 체크후 넘기기
                return json.dumps({  # 아이디 비번 조건틀림
                    "Result": False,
                    "error": "1",
                    "msg": "Id or password condition is wrong"
                })

            if not CHECK_DB.is_user(id, pw):
                return json.dumps({  # 비밀번호 틀림
                    "Result": False,
                    "error": "3",
                    "msg": "wrong password"
                })    # 유저가 입력한 비밀번호와 데이터베이스의 비밀번호 비교하기

            session['userid'] = id

            return json.dumps({
                    "Result": True,
                    "id": id,
            })

        else:
            return json.dumps({  # request is Not POST
                "Result": False,
                "error": "0",
                "msg": "Request is not POST"
            })
    except:
        traceback.print_exc()
        return json.dumps({"result": False, "error": 0, "msg": traceback.format_exc()})


@login_bp.route("/register", methods=['POST',])
def register():
    try:
        if request.method == 'POST':

            rq_js = request.args.get()

            id = rq_js['id']
            pw = rq_js['pw']
            nickname = rq_js['name']  # 유저 닉네임

            # 아이디 체크
            if not (CHECK_ID.id_validation(id) and CHECK_ID.pw_validation(pw)):  # 아이디, 비밀번호 체크후 넘어가기
                return json.dumps({  # 아이디 비밀번호 조건 틀림
                    "Result": False,
                    "error": "1",
                    "msg": "Id or password condition is wrong"
                })

            if not CHECK_DB.id_check(id):
                return json.dumps({  # 이미 존재하는 아이디
                    "Result": False,
                    "error": "4",
                    "msg": "The id that already exists"
                })
                # 아이디 중복 여부
            if not CHECK_DB.insert_user(id, pw, nickname, 0):  # 회원가입 성공여부
                return json.dumps({
                    "Result": False,
                    "error": "5",
                    "msg": "Failed to sign up for membership"
                })



            return json.dumps({  # 회원가입 성공
                "Result": True,
                "id": id,
                "name": nickname
            })

        else:
            return json.dumps({  # request is Not POST
                "Result": False,
                "error" : "0",
                "msg": "Request is not POST"
            })

    except:
        traceback.print_exc()
        return json.dumps({"result": False, "error": 0, "msg": traceback.format_exc()})


@login_bp.route("/logout", methods=['POST',])
def logout():
    try:
        session.pop('userid', None)
        return json.dumps({"result" : True,})


    except:
        traceback.print_exc()
        return json.dumps({"result": False, "error": 0, "msg": traceback.format_exc()})
