import abc
import psycopg2
import metier
import time

class AbstractDatabase(abc.ABC):
    
    @abc.abstractmethod
    def get_body_type(self):
        pass

    @abc.abstractmethod
    def connexion(self):
        pass

    @abc.abstractmethod
    def add_client(self, client: metier.Client):
        pass

    @abc.abstractmethod
    def get_all_clients(self):
        pass

    @abc.abstractmethod
    def get_client(self, id):
        pass


class PostgresDB(AbstractDatabase):

    def __init__(self):
        self.connector = None
        self.dbcursor = None
        self.connexion() #sets up connector and dbcursor
        if(self.connector):
            self.connector.autocommit = True

    def connexion(self):
        try:
            self.connector = psycopg2.connect(
                host="db",
                database="my_company_db",
                user="postgres",
                password="password",
                port="5432"
            )
            self.dbcursor = self.connector.cursor()
            print("connection ok", flush=True)
        except Exception as error:
            print("Oops! An exception has occured:", error, flush=True)

    def add_client(self, newClient: metier.Client):
        self.dbcursor.execute("INSERT INTO clients(firstName, lastName, emailId) values(%s,%s,%s)",(newClient.firstName, newClient.lastName, newClient.emailId))

    def get_all_clients(self):
        self.dbcursor.execute("SELECT * FROM clients")
        try:
            res = self.dbcursor.fetchall()
        except Exception as err:
            print("Oops! An exception has occured:", err)
            res = []
        ret = []
        for row in res:
            new_row = { 'id': row[0], 'firstName': row[1], 'lastName':row[2], 'emailId':row[3]}
            ret.append(new_row)

        return ret

    def get_client(self, id):
        self.dbcursor.execute("SELECT * FROM clients WHERE id=%s", str(id))
        try:
            res = self.dbcursor.fetchall()
        except Exception as err:
            print("Oops! An exception has occured:", err, flush=True)
            res = []
        if(len(res) == 0):
            return None
        return res[0]

    def get_body_type(self):
        return "test"
    
class JsonDB(AbstractDatabase):
    
    def __init__(self):
        pass
        
    def get_body_type(self):
        pass

class DatabaseFactory():
    
    def build_db(plan):
        try:
            if plan == "postgres":
                return PostgresDB()
            elif plan == "json":
                return JsonDB()
            raise AssertionError("Type is not valid.")
        except AssertionError as e:
            print(e)

if(__name__ == "__main__"):
    db = DatabaseFactory.build_db("postgres")
    newone = metier.Client("fn", "ln", "email@email.com")
    db.add_client(newone)
