import psycopg2 # For work PGAdmin and SQL
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

    def execute_query(self, query, *params):
        try:
            self.cur.execute(query, params)
            return self.cur.fetchall()
        except Exception as e:
            print(f'Error executing the query: {e}')

    # ip/nick, city, temperature, description, timeofrequest, API
    def saveRequest(nick, city, temperature, description, timerequest):
        print('q')

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()