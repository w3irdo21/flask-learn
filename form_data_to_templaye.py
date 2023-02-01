from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method=='POST':
        result=request.form
        return render_template('home_result.html',result=result)
    
if __name__ == "__main__":
    app.run(debug=True,port=7777)