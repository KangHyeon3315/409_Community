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
        "result": false,
        "error": Error Code
        "msg": failure message
    }

### success
    {
        "result" true,
        "name": user name
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

### success
    {
        "result" true,
        "name": user name
        향후 필요한 정보 추가
    }