import psycopg2 # For work PGAdmin and SQL
from psycopg2 import sql # For request
from config import DB_CONFIG # Config

class Database:
    def __init__(self, db_config):
        self.dbname = db_config['dbname']
        self.user = db_config['user']
        self.password = db_config['password']
        self.host = db_config['host']
        self.port = db_config['port']
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname, 
                user=self.user,  
                password=self.password,  
                host=self.host,          
                port=self.port
            )
            self.cur = self.conn.cursor()
        except Exception as e:
            print(f'Error with DB! {e}')

    def execute_queryOne(self, query, *params):
        try:
            self.cur.execute(query, params)
            return self.cur.fetchone()[0]
        except Exception as e:
            print(f'Error executing the query: {e}')

    def executeAndPrint_queryMany(self, query, *params):
        self.cur.execute(query, (params))
        records = self.cur.fetchall()
        header = ["ID", "City", "Temperature", "Description", "Time of Request", "Nickname"]
        print("{:<5} {:<15} {:<15} {:<20} {:<25} {:<15}".format(*header))
        print("=" * 100) 

        for record in records:
            print("{:<5} {:<15} {:<15} {:<20} {:<25} {:<15}".format(*record))

    def saveRequest(self, nick, city, temperature, description, timerequest):
        insert_query = sql.SQL("""
            INSERT INTO UsersRequests (UsersRequests_cityAtRequest, UsersRequests_temperature, UsersRequests_description, UsersRequests_timeOfRequest, users_nickname)
            VALUES (%s, %s, %s, %s, %s);
        """)
        self.cur.execute(insert_query, (city, temperature, description, timerequest, nick))
        self.conn.commit()

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()