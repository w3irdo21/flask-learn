from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///mytodo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


class ToDo(db.Model):
        
    SNo=db.Column(db.Integer,primary_key=True)
    Title=db.Column(db.String(50),nullable=False)
    Desc=db.Column(db.String(250),nullable=False)
    dc=db.Column(db.DateTime,default=datetime.utcnow)
    def __repr__(self) -> str:
        return f"{self.SNo}- {self.title}"


@app.route('/world')
def hello_world() :
    return "Hello There, We learning Flask here"

@app.route('/')
def renderfunc():
    return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True, port=6115)