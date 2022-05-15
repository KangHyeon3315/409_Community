import traceback
import json
from flask import Flask, Blueprint, request , session
import Backend.Utils.Database as DB

login_bp = Blueprint('Data', __name__, url_prefix='/api/data')




def ID_CHECK(check):
    return True
def PASSWORD_CHECK(check):
    return True

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
            rq_js = request.json(silent=True)

            id = rq_js['id']
            pw = rq_js['pw']

            if ID_CHECK(id) and PASSWORD_CHECK(pw):  # 아이디 , 비밀번호 체크후 넘기기

                if DB.Database.id_check(id):  # 데이터베이스에 아이디가 있는지 확인

                    if DB.Database.is_user(id,pw):  # 유저가 입력한 비밀번호와 데이터베이스의 비밀번호 비교하기

                        session['userid'] = id

                        return json.dumps({
                            "Result": True,
                            "id": id,
                            "name": TestName[id]
                        })
                    else:
                        return json.dumps({  # 비밀번호 틀림
                            "Result": False,
                            "error": "3",
                            "msg": "wrong password"
                        })
                else:
                    return json.dumps({  # 입력한 아이디가 존재하지 않음
                        "Result": False,
                        "error": "2",
                        "msg": "The id entered does not exist"
                    })
            else:
                return json.dumps({  # 아이디 비번 조건틀림
                    "Result": False,
                    "error": "1",
                    "msg": "Id or password condition is wrong"
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

            rq_js = request.json(silent=True)

            id = rq_js['id']
            pw = rq_js['pw']
            name = rq_js['name']  # 유저 닉네임

            # 아이디 체크
            if ID_CHECK(id) and PASSWORD_CHECK(pw):  # 아이디, 비밀번호 체크후 넘어가기

                if not DB.Database.id_check(id):  # 아이디 중복 여부

                    TestName[id] = id  # 유저 이름,유저 아이디 추가
                    TestPassword[id] = pw  # 유저 아이디에 비밀번호 추가



                    return json.dumps({  # 회원가입 성공
                        "Result": True,
                        "id" : id,
                        "name": name
                    })
                else:
                    return json.dumps({  # 이미 존재하는 아이디
                        "Result": False,
                        "msg": "The id that already exists"
                    })
            else:
                return json.dumps({  # 아이디 비밀번호 조건 틀림
                    "Result": False,
                    "msg": "Id or password condition is wrong"
                })
        else:
            return json.dumps({  # request is Not POST
                "Result": False,
                "msg": "Request is not POST"
            })
    except:
        traceback.print_exc()
        return json.dumps({"result": False, "error": 0, "msg": traceback.format_exc()})


@login_bp.route("/logout", methods=['POST',])
def logout():
    try:
        session.pop('userid',None)
        return json.dumps({"result" : True,})


    except:
        traceback.print_exc()
        return json.dumps({"result": False, "error": 0, "msg": traceback.format_exc()})
