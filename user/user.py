from DataBase.db import Db
from datetime import datetime
from uuid import uuid4
from flask import request, json


class User(Db):

    def create_user(self):
        dict_values =json.loads(request.data.decode("utf-8"))
        try:
            self.cursor.execute(f"""INSERT INTO user VALUES('{str(uuid4())[0:8]}', '{dict_values['name']}',  
                                '{dict_values['cpf']}', '{dict_values['email']}', '`{dict_values['phone_number']}', 
                                '{datetime.strftime(datetime.now(), '%H:%M:%S  %d/%m/%Y')}', '{'Never'}')""")
            return "Dale manin, cadastro registrado !!"
        except:
            return "Tentamos mas não funfou :(  ...", 777
