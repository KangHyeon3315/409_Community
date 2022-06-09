import traceback
from Backend.Utils.Database import Database

class Login_DB(Database):

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