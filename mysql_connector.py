import mysql.connector as mydb



def start_connection():
    # コネクションの作成
    conn = mydb.connect(
        host='127.0.0.1',
        port='3306',
        user='',
        password='',
        database=''
    )
    return conn

def create_table(conn,table_name):
    print(1)
    # DB操作用にカーソルを作成
    cur = conn.cursor()

    # id, name, priceを持つテーブルを（すでにあればいったん消してから）作成
    table = table_name
    #cur.execute("DROP TABLE IF EXISTS `%s`;", table)
    cur.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
        `id` int primary key,
        `task_name` varchar(50) not null,
        `is_check` boolean not null
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
        """)
    
    return cur

def select(cur):
    data = []
    cur.execute("SELECT * FROM task_table")
    rows = cur.fetchall()
    print(rows)
    for i,t,c in rows:
        q = {"id":None,"task_name":None,"is_check":None}
        q["id"] = i
        q["task_name"] = t
        q["is_check"] = c
        data.append(q)

    return data

def insert(con,cur,value):
    cur.execute("SELECT max(id) FROM task_table")
    max_id = cur.fetchone()[0]
    if max_id == None:
        max_id = 0
    
    #cur.execute("INSERT INTO taskDB.task_table VALUES  (%(id)s, %(task_name)s, %(is_check)s)",{"id":max_id + 1,"task_name":value[1],"is_check":value[2]})
    cur.execute(f"INSERT INTO taskDB.task_table (id, task_name, is_check) VALUES ('{max_id+1}', '{value[1]}', '{value[2]}')")
    #print(f'INSERT INTO taskDB.task_table (id, task_name, is_check) VALUES ({max_id+1}, "{value[1]}", {value[2]})')
    con.commit()
def delete(cur,id):
    cur.execute(f'DELETE FROM test_table WHERE id = {id}')
