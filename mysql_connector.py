import mysql.connector as mydb


q = {"id":None,"task_name":None,"is_check":None}
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
        """
        CREATE TABLE IF NOT EXISTS `%s` (
        `id` int auto_increment primary key,
        `task_name` varchar(50) not null,
        `is_check` int(11) not null
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
        """, table)
    
    return cur

def select(cur):
    data = []
    rows = cur.fetchall()
    for i,t,c in rows:
        q["id"] = i
        q["task_name"] = t
        q["is_check"] = c
        data.append(q)

    return data

def insert(cur,value):
    #a = cur.execute("SELECT id FROM task_table ORDER BY id")
    cur.execute("INSERT INTO task_table VALUES  (%(id)s, %(task_name)s, %(is_check)s)",{"id":2,"task_name":value[1],"is_check":value[2]
})


def delete(cur,id):
    cur.execute(f'DELETE FROM test_table WHERE id = {id}')