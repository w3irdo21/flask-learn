from flask import Flask, redirect,render_template, url_for,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///mytodo.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db=SQLAlchemy(app)


# class ToDo(db.Model):
        
#     SNo=db.Column(db.Integer,primary_key=True)
#     Title=db.Column(db.String(50),nullable=False)
#     Desc=db.Column(db.String(250),nullable=False)
#     dcj=db.Column(db.DateTime,default=datetime.utcnow)
    # with app.app_context():
    #     db.create_all()
    # def __repr__(self) -> str:
    #     return f"{self.SNo}- {self.Title}"


@app.route('/world')
def hello_world() :
    return "Hello There, We learning Flask here"

@app.route('/')
def renderfunc():
    # todo=ToDo(Title="Here No.1",Desc="Got this Here")
    # db.session.add(todo)
    # db.session.commit()
    return render_template('index.html')

@app.route('/guest/<user>')
def guest(user):
        return "Hello %s" %user

@app.route('/admin')
def admin():
        return "Hello Admin, w3irdo_21"

@app.route('/user/<name>')
def nameing(name):
    if name=='admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest',user=name))
        
# @app.route('/',methods=['POST','GETS'])
# def login():
#     if request.method=='POST':
#         me=request.form('title')
#         return redirect(url_for('guest',user=me))
#     else:
#         me = request.args.get('title')
#         return redirect(url_for('guest',user=me))

if __name__=="__main__":
    app.run(debug=True, port=6115)