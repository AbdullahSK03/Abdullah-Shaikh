import pypyodbc as odbc

DRIVER_NAME = 'SQL Server'
SERVER_NAME = 'Abdullah\SQLEXPRESS'

DB_NAME = 'qualification'

# uid=<username>;
# pwd=<password>;

conn = f""" 
DRIVER={{{DRIVER_NAME}}};
SERVER={SERVER_NAME};
DATABASE={DB_NAME};
Trustt_Connection=yes;
"""

odbc_conn = odbc.connect(conn)

print(odbc_conn)