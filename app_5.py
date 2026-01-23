from flask import Flask, render_template, session, make_response, request, flash

app = Flask(__name__, template_folder='templates')
app.secret_key = "supersecretkey"

@app.route('/')
def index():

    return render_template('index_5.html', message="Index")


@app.route('/set_data')
def set_data():
    session["name"] = "Berkay"
    session["other"] = 40
    return render_template('index_5.html', message="Session Data Set")


@app.route('/get_data')
def get_data():
    if "name" in session.keys() and "other" in session.keys():
        name = session.get("name")
        other = session.get("other")
        return render_template('index_5.html', message=f"Name: {name}, Other: {other}")
    else:
        return render_template('index_5.html', message="No session data found")
   

@app.route('/clear_session')
def clear_session():
    session.clear()
    #session.pop("name")
    return render_template('index_5.html', message="Session Cleared")


@app.route("/set_cookie")
def set_cookie():
    response = make_response(render_template('index_5.html', message="Cookie Set"))
    response.set_cookie("mycookie", "cookievalue")
    return response


@app.route("/get_cookie")
def get_cookie():
    cookie_value = request.cookies.get("mycookie")
    return render_template('index_5.html', message=f"Cookie Value: {cookie_value}")

@app.route("/remove_cookie")
def remove_cookie():
    response = make_response(render_template('index_5.html', message="Cookie Removed"))
    response.set_cookie("mycookie", expires=0)
    return response


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', message="Login Page")
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'beko' and password == '1234':
            flash("Login Successful!")
            return render_template('index_5.html', message="")
        else:
            flash("Login Failed")
            return render_template('login.html', message="")
            

    return render_template('login.html', message="Login Page")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000, debug=True)