from flask import Flask, request, make_response  

app = Flask(__name__)

@app.route('/')

def index():
    return "<h1>Hello, World!</h1>"

@app.route('/hello')   #@app.route('/hello', methods=['GET', 'POST'])
def hello():
    response = make_response("hello  bro")
    response.status_code = 202
    response.headers["content-type"] = "text/plain"
    return response



@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"the sum is: {num1 + num2}"


@app.route('/handle_url_params')
def handle_params():
    if "greeting" in request.args.keys() and "name" in request.args.keys():
        greeting = request.args["greeting"]
        name = request.args["name"]
        return f"{greeting}, {name}!"
    else:
        return "Some paramaters are missing"





if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

