from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello 5 World!'

@app.route('/home', methods=['POST','GET'], defaults={'name':'Default'})
@app.route('/home/<string:name>', methods=['GET', 'POST'])
def home(name):
    return 'Hello {}. You are coming home'.format(name)

@app.route('/app')
def json():
    return jsonify({'key': ' value', 'listkey': [1, 2, 3]})

@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi {}/. You are on the {} page</h1>'.format(name, location)

@app.route('/submit', methods =['GET','POST'])
def submit():
    if request.method == 'GET':
        return '''<form method ="POST" action ="/finish">
           <input type = "text" name = "name">
           <input type = "text" name = "location">
           <input type = "submit" value = "Submit">
           </form>'''
    else:
        name = request.form['name']
        location = request.form['location']
        return '<h1>hello{} . You are from {} </h1>'.format(name, location)

    @app.route('/finish', methods = ['POST'])
    def finish():
        name = request.form['name']
        location = request.form['location']
    return '<h1>hello{} . You are from {} </h1>'.format(name, location)

@app.route('/jsonSubmit',methods =['POST'])
def jsonsubmit():
    data = request.get_json()
    name = data['name']
    location = data['location']
    randomlist = data['randomlist']
    return jsonify({'result': 'Success','name' : name,'location':location,'randomkeylist':randomlist})

if __name__ == '__main__':
    app.run(debug=True)
