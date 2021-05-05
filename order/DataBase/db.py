import MySQLdb


class Db:

    def __init__(self):
        self.conn = MySQLdb.connect(db="microsservices_exercise", host="localhost", port=33069, user="root")
        self.conn.autocommit(True)
        self.cursor = self.conn.cursor()
