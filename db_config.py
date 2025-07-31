import pyodbc
def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'Server=NITHYA\\SQLEXPRESS;'
        'DATABASE= E commercedb;'
        'Trusted_Connection=yes;'
    )
    return conn
