# Import Module(s)
import sqlite3

# Create database and add table
conn = sqlite3.connect('myDatabase.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFiles \
    (ID INTEGER PRIMARY KEY AUTOINCREMENT, col_txtFile TEXT)")
    conn.commit()
conn.close()

conn = sqlite3.connect('myDatabase.db')

# Add all '.txt' files to database and print
print("Text files in database:\n")

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

for i in fileList:
    if i.endswith('.txt'):
        print(i)
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_txtFiles(col_txtFile) VALUES (?)", (i,))
        conn.commit()
conn.close()



