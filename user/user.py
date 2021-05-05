from DataBase.db import Db
from datetime import datetime
from uuid import uuid4
from flask import request, json
from pandas import pandas as pd


class User(Db):

    def create_user(self):
        dict_values =json.loads(request.data.decode("utf-8"))
        try:
            self.cursor.execute(f"""INSERT INTO user VALUES('{str(uuid4())[0:8]}', '{dict_values['name']}', 
                                '{dict_values['cpf'].replace(".","").replace("-","")}', 
                                '{dict_values['email']}','{dict_values['phone_number']}', 
                                '{datetime.strftime(datetime.now(), '%H:%M:%S  %d/%m/%Y')}', '{'Never'}')""")
            return "Cadastro registrado !!", 200
        except:
            return "Algo deu errado ...", 400

    def delete_user(self):
        dict_values = json.loads(request.data.decode("utf-8"))
        try:
            print("aaaa")
            self.cursor.execute(f"DELETE FROM user WHERE id = '{dict_values['id']}'")
            return "Usuário deletado !!", 200
        except:
            return "Algo deu errado ...", 400

    def select_users(self):
        try:
            self.cursor.execute("SELECT * FROM user")
            columns = [i[0] for i in self.cursor.description]
            df = pd.DataFrame(self.cursor.fetchall(), columns=columns)
            return df.to_json(orient="records")
        except:
            return "Algo deu errado ...", 400

    def update_user(self):
        dict_values = json.loads(request.data.decode("utf-8"))
        set_sql_list = []

        for key, value in dict_values['set'].items():
            set_sql_list.append(f"{key} = '{value}'")

        try:
            self.cursor.execute(f"UPDATE user SET {', '.join(set_sql_list)}, "
                                f"updated_at = '{datetime.strftime(datetime.now(), '%H:%M:%S  %d/%m/%Y')}' "
                                f"WHERE id = '{dict_values['id']}'")
            return "Dados Alterados !!", 200
        except:
            return "Algo deu errado ...", 400