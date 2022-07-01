
from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dropdown.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/", methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template ("index.html")

@app.route('/go', methods=['GET', 'POST'])
def update():
    if request.method=='POST':
        go = request.form['go']
        
        return redirect("/")
    return render_template('go.html')  

@app.route("/daa", methods=['GET', 'POST'])
def daa():
    data = request.form
    print(data)
    return render_template ("daa.html")

@app.route("/dtp", methods=['GET', 'POST'])
def dtp():
    data = request.form
    print(data)
    return render_template ("dtp.html")            
    

   
if __name__ == '__main__':
    app.debug = True
    app.run()