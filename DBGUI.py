from tkinter import *
import sqlite3
import pymysql
from tkinter.filedialog import askopenfilename

root = Tk()
filename=""
root.bind('<Escape>', lambda e: root.quit())
root.attributes('-fullscreen', True)
root.configure(background='black')


def draw_Schema():
    DBtype = Database_kind.get()
    print(DBtype)
    if DBtype == 'sql':
        tables_name = load_table_name_sql()
    elif DBtype == 'sqlite':
        tables_name = load_table_name_sqlite()
    columns_name = {}
    for t in tables_name:
        if DBtype == 'sql':
            columns_name[t] = load_column_name_sql(t)
        elif DBtype == 'sqlite':
            columns_name[t] = load_column_name_sqlite(t)
    print(tables_name)
    print(columns_name)
    x = 200
    y = 300
    c = 0
    for t in tables_name:
        createTabel(DBName,t,columns_name[t],len(columns_name[t]),x,y)
        x += 600
        c += 1
        if c%3 == 0:
            x = 200
            y += 500


def load_table_name_sqlite():
    conn = sqlite3.connect(DBFullName)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = cur.fetchall()
    conn.close()
    tables_name = []
    for r in rows:
        tables_name.append(r[0])
    return tables_name

def load_column_name_sqlite(t):
    conn = sqlite3.connect(DBFullName)
    cur = conn.cursor()
    cur.execute("PRAGMA table_info("+t+");")
    rows = cur.fetchall()
    conn.close()
    columns_name = []
    for r in rows:
        columns_name.append(r[1])
    return columns_name

def load_table_name_sql():
    db = pymysql.connect(host='localhost',user='gely',passwd='123456789',db=DBName)
    cur = db.cursor()
    cur.execute("SELECT table_name From information_schema.tables WHERE table_schema='"+DBName+"'")
    rows = cur.fetchall()
    tables_name = []
    for r in rows:
        tables_name.append(r[0])
    return tables_name

def load_column_name_sql(t):
    db = pymysql.connect(host='localhost',user='gely',passwd='123456789',db=DBName)
    cur = db.cursor()
    cur.execute("SELECT column_name From information_schema.columns WHERE table_name='"+t+"'")
    rows = cur.fetchall()
    columns_name = []
    for r in rows:
        columns_name.append(r[0])
    return columns_name
flag = False
DBName = ''
DBFullName = ''

def choose_file():
    global DBNameLbl,flag,DBName,DBFullName,tablesfields
    for tablefields in tablesfields:
        for tableElement in tablefields:
            tableElement.destroy()
    for tableTitle in TableNameTitle:
        tableTitle.destroy()
    flag = False
    Tk().withdraw()
    filename = askopenfilename()
    print(filename)
    DBName = getDbName(filename)
    DBFullName = getDbFullName(filename)
    DBNameQuestion = "Is your DB Name: '"+DBFullName+"'"
    DBNameLbl.config(text=DBNameQuestion)
    DBNameLbl.text = DBNameQuestion
    flag = True

def getDbName(path):
    name = ''
    fianl_name = ''
    for i in range(len(path)-1,-1,-1):
        if path[i] == '/':
            break
        else:
            name += path[i]
    for i in range(len(name)-1,-1,-1):
        if name[i] == '.':
            break
        fianl_name += name[i]
    return fianl_name

def getDbFullName(path):
    name = ''
    fianl_name = ''
    for i in range(len(path)-1,-1,-1):
        if path[i] == '/':
            break
        else:
            name += path[i]
    for i in range(len(name)-1,-1,-1):
        # if name[i] == '.':
        #     break
        fianl_name += name[i]
    return fianl_name
tablesfields = []
TableNameTitle = []
def createTabel(dataBasename,tableName,column_names,numOfFields,locationX,locationY):
    global tablesfields,TableNameTitle
    TableNamelbl = Label(root,width=20,text=tableName,bg='yellow',fg='black',font='Calibri 20')
    TableNamelbl.place(x=locationX,y=locationY-60)
    tablefields = []
    for i in range(numOfFields):
        tablefield = Label(root,width=16,text=column_names[i],bg='blue',fg='black',font='Calibri 14')
        tablefields.append(tablefield)
    for tableElement in tablefields:
        tableElement.place(x=locationX,y=locationY)
        locationY += 35
    tablesfields.append(tablefields)
    TableNameTitle.append(TableNamelbl)


choose_file_btn = Button(root,bg='red',width=8,fg='black',text='Load\nDataBase',font='Calibri 20',command=choose_file)
choose_file_btn.place(x=100,y=50)

DBNameLbl = Label(root,text='',bg='black',fg='red',font='Calibri 20')
DBNameLbl.place(x=700,y=50)

Draw_Schema_btn = Button(root,bg='red',width=8,fg='black',text="Draw\nSchema",font='Calibri 20',command=draw_Schema)
Draw_Schema_btn.place(x=1600,y=50)
check_DBName = IntVar()
yes_Radio = Radiobutton(root,text="Yes",bg='black',fg='green',variable=check_DBName,value=1,font='Calibri 12')
no_Radio = Radiobutton(root,text="No",bg='black',fg='red',variable=check_DBName,value=0,font='Calibri 12')
if flag:
    yes_Radio.place(x=600,y=100)
    no_Radio.place(x=700,y=100)

Database_kind_lbl = Label(root,text="What Is the Kind of DB",bg='black',fg='blue',font='Calibri 20')
Database_kind_lbl.place(x=300,y=40)
Database_kind = StringVar(root)
Database_kind.set("sql")

choose_DB_Kind = OptionMenu(root,Database_kind,"sql","sqlite","csv","xml")
choose_DB_Kind.config(fg='black')
choose_DB_Kind.config(bg='blue')
choose_DB_Kind.config(width=10)
choose_DB_Kind.config(font='Calibri 20')
choose_DB_Kind.place(x=330,y=90)

root.mainloop()
