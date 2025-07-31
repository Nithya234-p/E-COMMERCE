import pyodbc

server = 'localhost'
database = 'ecommerce'
username = 'sa'   # or your SQL username
password = 'YourPasswordHere'  # replace with your real password

try:
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes'
    )
    print("Connection successful!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)
