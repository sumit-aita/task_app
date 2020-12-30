import mysql_connector as sql

a = sql.start_connection()

b = sql.create_table(a, "task_table")
# print(sql.select(b))
# #sql.insert(a,b, [None, "Hello", 0])
# aa = "task"
# #b.execute(f"INSERT INTO taskDB.task_table (id, task_name, is_check) VALUES ({110}, '{aa}', {1})")

# a.commit()
