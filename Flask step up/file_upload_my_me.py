from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app=Flask(__name__)

@app.route('/')
def main():
    return render_template('file_upload_by_me.html')

@app.route('/uploader',methods=['GET','POST'])
def doness():
    if request.method=='POST':
        f=request.files['file']
        f.save(secure_filename(f.filename))
        return 'File saved Successfully'

if __name__ == '__main__':
   app.run(debug = True,port=6115)