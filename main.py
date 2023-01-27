from flask import Flask,render_template
app=Flask(__name__)
@app.route('/world')
def hello_world() :
    return "Hello There, We learning Flask here"

@app.route('/')
def renderfunc():
    return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True, port=6115)