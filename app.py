from databases import *
from flask import Flask, request, redirect, render_template
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def home():
    return render_template('home.html')
    

@app.route('/login', methods=['POST'])
def login():
    user = get_user(request.form['username'])
    if user != None and user.verify_password(request.form["password"]):
        login_session['name'] = user.username
        login_session['logged_in'] = True
        return logged_in()
    else:
        return home()


@app.route('/signup', methods=['POST'])
def signup():
    #check that username isn't already taken
    user = get_user(request.form['username'])
    if user == None:
        add_user(request.form['username'],request.form['password'])
    return home()


@app.route('/logged-in', methods=['POST',"GET"])
def logged_in():
    
    if request.method == "POST":
        try:        

            fav_food = request.form['fav_food']
            add_food(login_session['name'], fav_food)
            return render_template('logged.html',fav_food=fav_food)
        except KeyError:
            return render_template('logged.html', get_user())
    else:
        return render_template('logged.html'


@app.route('/logout')
def logout():
    login_session.clear()
    return home()



if __name__ == '__main__':
    app.run(debug=True)
