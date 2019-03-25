import sqlite3

file_list = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

def getTextExtension():
    extension_list = []
    for i in file_list:
        if '.txt' in i:
            extension_list.append(i)  
    
    return extension_list
               
def createTable():
    conn = sqlite3.connect('database_python_drill.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_txt_extension( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT)")
        conn.commit()
    conn.close()
    createRows(getTextExtension())

def createRows(extension_list):
    conn = sqlite3.connect('database_python_drill.db')
    
    with conn:
        for i in extension_list:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_txt_extension (col_fname) VALUES (?)", \
                (i,) )
            print(i)
            conn.commit()
    conn.close()

createTable()
