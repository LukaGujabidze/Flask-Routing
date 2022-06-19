from flask import Flask,render_template,request,url_for,redirect,flash

app = Flask(__name__)

@app.route('/')
def index():
    global name
    global last_nm
    global age

    if request.method == 'POST':
        req = request.form
        name = req.get('name')
        last_nm = req.get('last_nm')
        age = req.get('age')
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html', name=name, last_nm=last_nm, age=age)

if __name__ == '__main__':
    app.run(debug=True)

