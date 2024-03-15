from flask import Flask , render_template, request, redirect, session, flash
import secrets
import sqlite3
app = Flask(__name__)
app.secret_key="123"

sqlconnection =sqlite3.connect("admin.db")
sqlconnection.execute("create table if not exists users(username text,password integer, email text)")
sqlconnection.close()

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/chatai.html')
def chatai():
    return render_template("chatai.html")

@app.route('/features.html')
def features():
    return render_template("features.html")

@app.route('/feature1.html')
def feature1():
    return render_template("feature1.html")

@app.route('/feature2.html')
def feature2():
    return render_template("feature2.html")

@app.route('/feature3.html')
def feature3():
    return render_template("feature3.html")

@app.route('/categories.html')
def categories():
    return render_template("categories.html")

@app.route('/Vegetables.html')
def Vegetables():
    return render_template("Vegetables.html")

@app.route('/Fruits.html')
def Fruits():
    return render_template("Fruits.html")

@app.route('/Millets.html')
def Millets():
    return render_template("Millets.html")

@app.route('/Spices.html')
def Spices():
    return render_template("Spices.html")

@app.route('/Others.html')
def Others():
    return render_template("Others.html")

@app.route('/Pulses.html')
def Pulses():
    return render_template("Pulses.html")

@app.route('/products.html')
def products():
    return render_template("products.html")

@app.route('/Aboutus.html')
def Aboutus():
    return render_template("Aboutus.html")

@app.route('/salesacc.html')
def salesacc():
    return render_template("salesacc.html")

@app.route('/cartform.html')
def cartform():
    return render_template("cartform.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        sqlconnection = sqlite3.connect('admin.db')
        sqlconnection.row_factory = sqlite3.Row
        cur = sqlconnection.cursor()

        cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        data = cur.fetchone()
        if( data):
            session['username'] = data["username"]
            session['password'] = data["password"]
            return redirect("/")
        else:
            flash("Invalid Username and Password", "danger")
            return redirect('/login')
    return render_template('login.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        try:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            
            sqlconnection = sqlite3.connect('admin.db')

            cur = sqlconnection.cursor()
            cur.execute("INSERT INTO users(username, email, password) VALUES (?, ?, ?)", (username, email, password))
            
            sqlconnection.commit()
           
        except:
            flash("Error in Insert Operation", "danger")
        finally:
            sqlconnection.close()
            return redirect('/login')

    return render_template('signup.html')



if __name__ == '__main__':
    app.run(debug=True)
