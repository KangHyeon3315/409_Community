import traceback
from Backend.Utils.Database import Database


class NoticeDB(Database):
    def create_notice(self, notice_id, notice_title, notice_writer, notice_date, notice_content) -> bool:
        try:
            curs = self.connect.cursor()
            sql = "INSERT INTO user (id, title, writer, date, content) VALUES (%s %s %s %s)"
            val = (notice_id, notice_title, notice_writer, notice_date, notice_content)
            curs.execute(sql, val)
            self.connect.commit()
            return True
        except (Exception,):
            traceback.print_exc()
            return False

    def create_comment(self, comment_id, notice_id, comment_writer, comment_date, parent_id):
        try:
            curs = self.connect.cursor()
            sql = "INSERT INTO user (id, notice_id, writer, date, content) VALUES (%s %s %s %s %s)"
            val = (comment_id, notice_id, comment_writer, comment_date, parent_id)
            curs.execute(sql, val)
            self.connect.commit()
            return True
        except (Exception,):
            traceback.print_exc()
            return False

