from unicodedata import name
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      name = result.get('Name')
      last_nm = result.get('last-nm')
      age = result.get('num')
      return render_template("result.html",name = name, last_name = last_nm, age=age)


if __name__ == '__main__':
   app.run(debug = True)