import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO article (title, content) VALUES (?,?)", ('Bottlender-prototype', 'This is mobile app code and hardware code + circuit for automatic air cannon. It was made during Sporthack 2020 to deliver small packages that would fall down from air using parachutes. The mechanical part is not included. This cannon is built like a turret and can be made to shoot at certain locations using formulas and right calculations.'))
cur.execute("INSERT INTO article (title, content) VALUES (?,?)", ('ESP-Console', 'Epic snake'))
cur.execute("INSERT INTO article (title, content) VALUES (?,?)", ('RoboArm', 'Hardware and mobile app code for Robotic Arm that is controlled by Arduino Nano. There are two main function that arm can do. One is manual control, where you can control all arm movements via app. Second function is auto, where has been programmed to take ball from bottom and put it on top of roller coaster, so the ball could roll back and be picked up again. There is no mechanical part description in this documentation. Bluetooth 4.0 module will be needed to receive data from app.'))
cur.execute("INSERT INTO article (title, content) VALUES (?,?)", ('Attiny-Led', 'Attiny13a register code examples.'))
cur.execute("INSERT INTO article (title, content) VALUES (?,?)", ('BtClassic.h', 'Arduino library for receiving Serial data on Rx/Tx pins and processing it. Using custom made protocol, you can send up to 10 commands and parameters with them.'))

cur.execute("INSERT INTO images (list_id, imageName, articleImages) VALUES (?, ?, ?)",
            (1, 'Image 1', 'https://www.somagnews.com/wp-content/uploads/2020/09/1599647767_244123_1599647831_noticia_normal.jpg')
            )

cur.execute("INSERT INTO images (list_id, imageName, articleImages) VALUES (?, ?, ?)",
            (2, 'Image 2', 'https://www.somagnews.com/wp-content/uploads/2020/09/1599647767_244123_1599647831_noticia_normal.jpg')
            )

cur.execute("INSERT INTO images (list_id, imageName, articleImages) VALUES (?, ?, ?)",
            (2, 'Image 3', 'https://www.somagnews.com/wp-content/uploads/2020/09/1599647767_244123_1599647831_noticia_normal.jpg')
            )

cur.execute("INSERT INTO images (list_id, imageName, articleImages) VALUES (?, ?, ?)",
            (3, 'Image 4', 'https://www.somagnews.com/wp-content/uploads/2020/09/1599647767_244123_1599647831_noticia_normal.jpg')
            )

cur.execute("INSERT INTO images (list_id, imageName, articleImages) VALUES (?, ?, ?)",
            (3, 'Image 5', 'https://www.somagnews.com/wp-content/uploads/2020/09/1599647767_244123_1599647831_noticia_normal.jpg')
            )

cur.execute("INSERT INTO images (list_id, imageName, articleImages) VALUES (?, ?, ?)",
            (4, 'Image 6', 'https://www.somagnews.com/wp-content/uploads/2020/09/1599647767_244123_1599647831_noticia_normal.jpg')
            )

connection.commit()
connection.close()