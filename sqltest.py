import pyodbc
server = 'exexdaserver.database.windows.net'
database = '<database>'
username = '<username>'
password = '<password>'   
driver= '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
        row = cursor.fetchone()
        while row:
            print (str(row[20]) + " " + str(row[20]))
            row = cursor.fetchone()