from DataBase.db import Db
from flask import json, request
from datetime import datetime
from uuid import uuid4
from pandas import pandas as pd

class Order(Db):

    def create_order(self):
        dict_values = json.loads(request.data.decode("utf-8"))

        sql = f"""INSERT INTO orders VALUES(
        "{str(uuid4())[0:8]}", 
        "{dict_values['user_id']}", 
        "{dict_values['item_description']}", 
        {dict_values['item_quantity']}, 
        {dict_values['item_price']}, 
        {dict_values['item_price']*dict_values['item_quantity']}, 
        "{datetime.strftime(datetime.now(), '%d/%m/%Y  %H:%M:%S')}", 
        "Never")"""

        try:
            self.cursor.execute(sql)
            return "cadastro efetuado !!", 200
        except:
            return "Algo deu errado ...", 400

    def update_order(self):
        dict_values = json.loads(request.data.decode("utf-8"))
        set_sql_list = []

        for key, value in dict_values['set'].items():
            set_sql_list.append(f"{key} = '{value}'")

        try:
            self.cursor.execute(f"UPDATE orders SET {', '.join(set_sql_list)}, "
                                f"updated_at = '{datetime.strftime(datetime.now(), '%d/%m/%Y  %H:%M:%S')}' "
                                f"WHERE id = '{dict_values['id']}'")
            return "Dados Alterados !!", 200
        except:
            return "Algo deu errado ...", 400

    def delete_order(self):
        dict_values = json.loads(request.data.decode("utf-8"))
        try:
            self.cursor.execute(f"DELETE FROM orders WHERE id = '{dict_values['id']}'")
            return "Pedido deletado !!", 200
        except:
            return "Algo deu errado ...", 400

    def select_orders(self):
        try:
            self.cursor.execute("SELECT * FROM orders")
            columns = [i[0] for i in self.cursor.description]
            df = pd.DataFrame(self.cursor.fetchall(), columns=columns)
            return df.to_json(orient="records").replace("\/","/")
        except:
            return "Algo deu errado ...", 400

    def select_users_with_orders(self):
        try:
            self.cursor.execute("SELECT * FROM orders")
            table = self.cursor.fetchall()
            set_value = set()
            for tuple in table:
                set_value.add(f'"{tuple[1]}"')
            self.cursor.execute((f'SELECT * FROM user WHERE id IN ({", ".join(list(set_value))})'))
            columns = [i[0] for i in self.cursor.description]
            df = pd.DataFrame(self.cursor.fetchall(), columns=columns)
            return df.to_json(orient="records").replace("\/", "/")
        except:
            return "Algo deu errado ...", 400