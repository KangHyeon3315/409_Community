import pymysql

class Database:

    def __init__(self):
        self.connect = pymysql.connect(host="115.23.220.188", user="labs409", password="#@!labs409", db="409Community",
                                       charset="utf8")

    def is_user(self, user_id, user_pw) -> bool:
        curs = self.connect.cursor()
        curs.execute('SELECT * FROM user WHERE id = %s AND pw = %s', (user_id, user_pw,))
        account = curs.fetchone()
        if account is None:
            return False
        else:
            return True

    def id_check(self, user_id) -> bool:
        curs = self.connect.cursor()
        curs.execute('SELECT * FROM user WHERE id = %s', (user_id,))
        account = curs.fetchone()
        if account is None:
            return True
        else:
            return False