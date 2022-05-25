import pymysql
import traceback

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

    def insert_user(self, user_id, user_pw, user_nickname, dept_id) -> bool:
        try:
            curs = self.connect.cursor()
            sql = "INSERT INTO user (id, pw, nickname, dept_id, sid) VALUES (%s, %s, %s, %s, '')"
            val = (user_id, user_pw, user_nickname, dept_id)
            curs.execute(sql, val)
            self.connect.commit()
            return True
        except Exception:
            traceback.print_exc()
            return False

    def find_dept_id(self, user_univ, user_dept) -> str:
        curs = self.connect.cursor()
        curs.execute('SELECT dept_id FROM dept WHERE univ = %s AND dept = %s', (user_univ, user_dept))
        self.connect.commit()
        dep_id = curs.fetchone()
        if dep_id is None:
            return ""
        else:
            return str(dep_id[0])