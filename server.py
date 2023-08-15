import base64
import pyodbc

class db_item:
    def __init__(self):
        self.conn = pyodbc.connect('''
            DRIVER={SQL Server};
            SERVER=Abdullah\SQLEXPRESS;
            DATABASE=Certification;  
            Trust_connection=yes                    
        ''')
        self.cursor = self.conn.cursor()

    def get_data(self):




# conn = pyodbc.connect('''
#     DRIVER={SQL Server};
#     SERVER=Abdullah\SQLEXPRESS;
#     DATABASE=Certification;  
#     Trust_connection=yes                    
# ''')


# cursor = conn.cursor()
# cursor.execute('SELECT id, course, C_Desc FROM certificate')
# for row in cursor.fetchall():
#     print(row)


# cursor.execute('SELECT IMG FROM certificate')
# for row in cursor.fetchall():
#     with open (row, 'rb') as image:
#         data = image.read()
    
#     data = base64.b64encode(data)

#     data.decode("UTF-8")


# print("successful")