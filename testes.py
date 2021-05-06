import MySQLdb


conn = MySQLdb.connect(db="microsservices_exercise", host="localhost", port=33069, user="root")
conn.autocommit(True)
cursor = conn.cursor()

cursor.execute("SELECT * FROM orders")
table = cursor.fetchall()
set_value = set()
for tuple in table:
    set_value.add(f'"{tuple[1]}"')

# print(set_value)

print(", ".join(list(set_value)))