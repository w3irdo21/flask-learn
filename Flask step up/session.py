from flask import session,Flask,request,redirect,url_for

# Set the secret key to some random bytes. Keep this really secret!
app=Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__== '__main__':
    app.run(debug=True,port=6115)

    
# from flask import Flask,redirect,render_template,request,session

# app=Flask(__name__)

# @app.route("/")
# def main():
#     return render_template('session.html')

# @app.route('/session',methods=['POST','GET'])
# def login():
#     if request.method=="POST":
#         session['username']=request.form(userid)
    
# if __name__== '__main__':
#     app.run(debug=True,port=6115)