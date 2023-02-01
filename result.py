from flask import render_template,Flask

app=Flask(__name__)

@app.route("/result/<int:score>")
def myresult(score):
    report={'Physics':score/3,'Chemistry':score/2,'Maths':score - score/3 - score/2}
    return render_template('result.html',marks=score,result=report)

if __name__=="__main__":
    app.run(debug=True)