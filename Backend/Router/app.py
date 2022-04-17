
from flask import Flask, jsonify, request
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

TestName = {}
TestPassword = {}


def ID_CHECK(check):
    return True
def PASSWORD_CHECK(check):
    return True


@app.route("/user/login",methods = ['POST','GET'])
def USER_LOGIN():
    if request.method == 'POST':
        USER_ID = request.form['USER_ID']
        USER_PASSWORD = request.form['USER_PASSWORD']
        
        if ID_CHECK(USER_ID) and PASSWORD_CHECK(USER_PASSWORD):  #아이디 , 비밀번호 체크후 넘기기
        
            if USER_ID in TestPassword.keys():  # 데이터베이스에 아이디가 있는지 확인
            
                if TestPassword[USER_ID] == USER_PASSWORD: #  유저가 입력한 비밀번호와 데이터베이스의 비밀번호 비교하기
                    
                    return jsonify({
                        "Result" : "True",
                        "USER_ID" : USER_ID,
                        "USER_NAME" : TestName[USER_ID]
                    })
                else:
                    return jsonify({   #비밀번호 틀림
                        "Result" : "False",
                        "msg" : "wrong password"
                    })
            else:
                return jsonify({  # 입력한 아이디가 존재하지 않음
                    "Result" : "False",
                    "msg" : "The id entered does not exist"
                    }) 
        else:
            return jsonify({   # 아이디 비번 조건틀림 
                "Result" : "False",
                "msg" : "Id or password condition is wrong"
                }) 
    else:
        return jsonify({ # request is Not POST
            "Result" : "False",
            "msg" : "Request is not POST"
            }) 
                
        

@app.route("/user/register",methods = ['POST','GET'])
def USER_REGISTER():
    if request.method == 'POST':
        USER_NAME = request.form['USER_NAME']  #유저 닉네임 
        USER_ID = request.form['USER_ID']
        USER_PASSWORD = request.form['USER_PASSWORD']
        
        # 아이디 체크
        if ID_CHECK(USER_ID) and PASSWORD_CHECK(USER_PASSWORD):  # 아이디, 비밀번호 체크후 넘어가기
            
            if USER_ID not in TestPassword.keys():    #아이디 중복 여부
                
                
                TestName[USER_ID] = USER_NAME   # 유저 이름,유저 아이디 추가 
                TestPassword[USER_ID] = USER_PASSWORD  #유저 아이디에 비밀번호 추가
                    
                return  jsonify({ # 회원가입 성공
                    "Result" : "True"
                })
            else:
                return jsonify({   # 이미 존재하는 아이디
                    "Result" : "False",
                    "msg" : "The id that already exists"
                })
        else:
            return jsonify({  # 아이디 비밀번호 조건 틀림
                "Result" : "False",
                "msg" : "Id or password condition is wrong"
            }) 
    else:
        return jsonify({   # request is Not POST
            "Result" : "False",
            "msg" : "Request is not POST"
        })



if __name__ == '__main__':
    app.run()