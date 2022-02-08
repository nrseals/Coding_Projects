# import cursor to interact w/database
import pymysql.cursors

# create class that gives instance of a connection to db
class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'euphman91',
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor,
            autocommit = True
        )
        self.connection = connection
    #method to query db
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try: 
                query = cursor.mogrify(query, data)
                print("*"*50)
                print("Running Query:", query)

                executable = cursor.excecute(query, data)
                # INSERT will return ID of row inserted
                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                #SELECT will return data as a LIST OF DICTONARIES
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result
                else: 
                    #UPDATE/DELETE return nothing
                    self.connection.commit()
            except Exception as e:
                # If the query fails the method returns False
                print("*"*50)
                print("Something went wrong", e)
                return False
            finally:
                #close connection
                self.connection.close()
#this function recieves db and uses it to create an instance of the MySQL connection
def connectToMySQL(db):
    return MySQLConnection(db)
