from flask import Flask, session, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_session import Session
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'


Session(app)

# Set up database
engine = create_engine("postgresql://postgres:MDMD2121@localhost/test")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    ##test = request.form.get("test") 
    return render_template("search.html", methods=["POST"])
    

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == "POST":   
        username = request.form.get("username")
        password = request.form.get("password")
        db.execute("INSERT INTO users (username, password) VALUES (:username, :password)",
        {"username": username, "password" : password})
        db.commit()
        session['user'] = username
        
        return redirect(url_for('success'))
    
    return render_template("signup.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST": 
        username = request.form.get("username")
        passwordform = request.form.get("password")
        result = db.execute("SELECT * FROM users WHERE username = :username",
        {"username": username}).fetchone()
        
        try: 
            password = result[1]
            
            if password == passwordform:
                session['logged_in'] = True
                session['user'] = username
                return redirect(url_for('index'))
            else: 
                error = "not matched"
                return render_template("login.html", error=error)
        except:
            error = "This Username doesn't exist"
            return render_template("login.html", error=error)


    return render_template("login.html")



@app.route("/success")
def success():
    return render_template("success.html", user=session['user'])


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == "__main__":
    

    app.debug = True
    app.run()