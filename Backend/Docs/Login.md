# Login

## request
    {
        "req": "login",
        "id": user id,
        "pw": user pw
    }

## response
### error or failure
    {
        "result": False,
        "error" : error code,
        "msg": failure message
    }
### error code and msg
    {
        # 요청이 POST 가 아닌경우
        code : 0
        msg: "Request is not POST"
    }
    {
        # 아이디 비밀번호 조건이 틀린경우
        code : 1
        msg : "Id or password condition is wrong"
    }
    {
        # 입력한 아이디가 존재하지 않을경우 
        code : 2
        msg : "The id entered does not exist"
    }
    {
        # 비밀번호가 틀린경우
        code : 3
        msg : "wrong password"
    }

### success
    {
        "result": True,
        "name": user name,
        "id": user id
        향후 필요한 정보 추가
    }

# Register

## request
    {
        "req": "regist",
        "id": user id,
        "pw": user pw,
        "pw_check": pw check,
        "name": user name,
    }

## response
### error or failure
    {
        "result": false,
        "error": Error Code
        "msg": failure message
    }

### error code and msg
    {
        # 요청이 POST 가 아닌경우
        code : 0
        msg: "Request is not POST"
    }
    {
        # 아이디 비밀번호 조건이 틀린경우
        code : 1
        msg : "Id or password condition is wrong"
    }
    {
        # 이미 아이디가 존재할경우
        code : 4
        msg : "The id that already exists"
    }


### success
    {
        "result" true,
        "name": user name
        향후 필요한 정보 추가
    }