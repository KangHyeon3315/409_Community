import re

class Validation:
    def __init__(self):
        self.id_rg = r'^[a-z]+[a-z0-9]{5,15}$'
        self.pw_rg = r'^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[@!?$]).{8,16}$'

    def id_validation(self, id):
        if ' ' in id:
            print("blank")
            return False
        if re.search(self.id_rg, id):
            return True
        return False

    def pw_validation(self, pw):
        if ' ' in pw:
            print("blank")
            return False
        if re.search(self.pw_rg, pw):
            return True
        return False