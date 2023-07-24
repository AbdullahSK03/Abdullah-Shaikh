import mysql.connector

# Connect to the MySQL database
connection = mysql.connector.connect(
    host="Abdullah",
    user="root",
    password="Adlava#7506",
    database="data"
)

# Read the image file as binary data
def read_image(filename):
    with open(filename, 'rb') as f:
        return f.read()

# Insert image data into the database
def insert_image(title, description, image_data):
    cursor = connection.cursor()
    sql = "INSERT INTO certificates (title, des, image) VALUES (%s, %s, %s)"
    values = (title, description, image_data)
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()

# Example usage
image_data1 = read_image("path/to/your/image1.jpg")
image_data2 = read_image("path/to/your/image2.jpg")
image_data3 = read_image("path/to/your/image3.jpg")

insert_image("Internet Of Things", "Worked and Studied with IoT boards as a field of interest", "static/images/IoT.webp")
insert_image("Web Developer", "I am a certified web developer with good understanding of HTML5, CSS3, JavaScript also learning NodeJs", "static/images/Webdev.webp")
insert_image("Python", "Python Programming language is one of the programming languages which I have an excellent command on. I have also worked with libraries Tkinter, Pandas, Flask, openCV, etc.")
