<<<<<<< Updated upstream
from flask import Flask 
=======
from flask import Flask
>>>>>>> Stashed changes

app = Flask(__name__)

@app.route('/')
def head():
<<<<<<< Updated upstream
    return 'Hello world Oktay'


@app.route('/second')
def second():
    return 'This is second page'

@app.route('/third')
def third():
    return 'This is third page'

=======
    return 'Hello world Demir'
@app.route('/second')
def second():
    return 'This is second page'
@app.route('/third')
def third():
    return 'This is third page'
>>>>>>> Stashed changes
@app.route('/forth/<string:id>')
def forth(id):
    return f'Id of this page is {id}'

<<<<<<< Updated upstream

if __name__ == '__main__':

    # app.run(debug=True)
    app.run(host= '0.0.0.0', port=80)
=======
if __name__ == '__main__':
    
    
    #app.run(debug=True)
    app.run(host= '0.0.0.0', port=80) 
>>>>>>> Stashed changes
