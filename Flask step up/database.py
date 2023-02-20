# from flask import Flask,render_template,request,flash
# import sqlite3

# app=Flask(__name__)
# # db=sqlite3.connect('database.db')
# # print('Database Connected Successfully')

# # db.execute('CREATE TABLE Students (Name TEXT, Addr TEXT, PhoneNumber TEXT, Course TEXT)')
# # print('''Table's Row and Columns Created''')
# # db.close()

# @app.route('/')
# def home():
#     return render_template('database.html')

# @app.route('/done',methods=('POST','GET'))
# def details():
#     try:
#         if request.method=='POST':
#             myname=request.form('myname')
#             addr=request.form('addr')
#             phn=request.form('phone')
#             crse=request.form('course')
#             with sqlite3.connect('database.db') as con:
#                 cur=con.cursor()
#                 cur.execute('INSERT INTO Students (Name,Addr,PhoneNumber Course) Values (?,?,?,?)',(myname,addr,phn,crse))
#                 con.commit()
#                 msg = "Record successfully added"

#     except:
#         con.rollback()
#         msg = "error in insert operation"
#     finally:
#         return "Your details have been saved, Thank You for your Time"

# if __name__ =="__main__":
#     app.run(debug=True,port=6115)
from flask import Flask,render_template,request,flash
import sqlite3

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('database.html')

@app.route('/done',methods=('POST','GET'))
def details():
    try:
        if request.method=='POST':
            myname=request.form['myname']
            addr=request.form['addr']
            phn=request.form['phone']
            crse=request.form['course']
            with sqlite3.connect('database.db') as con:
                cur=con.cursor()
                cur.execute('INSERT INTO Students (Name,Addr,PhoneNumber,Course) Values (?,?,?,?)',(myname,addr,phn,crse))
                con.commit()
                msg = "Record successfully added"

    except:
        con.rollback()
        msg = "error in insert operation"
    finally:
        return "Your details have been saved, Thank You for your Time"

if __name__ =="__main__":
    app.run(debug=True,port=6115)
