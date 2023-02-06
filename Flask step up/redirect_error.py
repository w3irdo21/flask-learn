from os import rename
from pydoc import render_doc
from flask import Flask,redirect, render_template,request,url_for,abort

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=="POST":
        if request.form['userid']=='18':
            return '<h2>Login Successfully Admin</h2>'
        abort(402)
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True,port=6115)