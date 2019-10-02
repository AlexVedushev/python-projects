import psycopg2
from contextlib import closing
from psycopg2.extras import DictCursor

PSQL_CONN = {
    'host': '127.0.0.1',
    'port': '5432',
    'user': 'magnit',
    'password': '3XGGhK28c46E',
    'dbname': 'magnit'
}

# with closing(psycopg2.connect(dbname='magnit', user='magnit', password='3XGGhK28c46E', host='localhost', port=5432)) as conn:
#     with conn.cursor() as cursor:
#         try:
#             selecteQuery = "SELECT * FROM public.user WHERE email = " + "'s1@mail.re'"
#             createRole = """INSERT INTO public.user_role ("created_at","updated_at","id","title","description") VALUES (DEFAULT,DEFAULT,5,'user5','user5')"""
#             cursor.execute(createRole)
#             conn.commit()
#         except psycopg2.Error as e:
#             print(e.diag.message_primary)
#         count = cursor.rowcount
#         print(count)
        # records = cursor.fetchall()

        # if len(records) > 0:
        #     for row in records:
        #         print(row)
def psycopg2_cursor(conn_info):
    
    def wrap(f):
        def wrapper(*args, **kwargs):
            try:
                # Setup postgres connection
                connection = psycopg2.connect(**conn_info)
                cursor = connection.cursor()

                # Call function passing in cursor
                return_val = f(cursor=cursor, *args, **kwargs)

            finally:
                # Close connection
                connection.close()

            return return_val
        return wrapper
    return wrap

class DatabaseManager(object):
    @psycopg2_cursor(PSQL_CONN)
    def truncateTable(self, name, cursor):
        print
        truncateQuery = """ TRUNCATE TABLE public.{}""".format(name)
        cursor.execute(truncateQuery)

databaseManager = DatabaseManager()
databaseManager.truncateTable('user')