import psycopg2

class Age_Dijkstra:

    def __init__(self):
        self.connection = None
        self.graph_name = None

    def get_pg_version(self):
        crsr = self.connection.cursor()
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        crsr.close()
        return db_version


    def connect(self,host="172.17.0.2", port="5432", dbname="postgres", user="postgres", password="agens", printMessage = False):
        try: 
            self.connection = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
            if (printMessage):
                print(self.get_pg_version())
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def close_connection(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

__name__ = "apache-age-dijkstra"