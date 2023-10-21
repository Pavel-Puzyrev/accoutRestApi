import psycopg2

import schemas

db_name = "localDb"
db_user = "user"
conn = psycopg2.connect(f"dbname={db_name} user={db_user} password=psw")
cur = conn.cursor()


# def getUser(login: schemas.User.login):
def get_user(login):

    # Execute a query
    cur.execute(f"SELECT * FROM account WHERE login='{login}'")

    # Retrieve query results
    records = cur.fetchall()
    print(records)
    return {'result': records[0]}
