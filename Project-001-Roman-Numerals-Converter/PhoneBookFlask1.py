from flask import Flask, render_template, request

app = Flask(__name__)
phonebook = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST', 'GET'])
def add():
    try:
        name = request.form['name']
        phone_number = request.form['phone_number']
        phonebook[name] = phone_number
    except KeyError:
        return render_template('index.html', message='Invalid input format, cancelling operation ...')
    else:
        return render_template('add.html', message=f'Phone number of {name} is inserted into the phonebook')

@app.route('/find', methods=['POST'])
def find():
    try:
        name = request.form['name']
        phone_number = phonebook[name]
    except KeyError:
        return render_template('index.html', message=f"Couldn't find phone number of {name}")
    else:
        return render_template('find.html', message=f'Phone number of {name} is {phone_number}')

@app.route('/delete', methods=['POST'])
def delete():
    try:
        name = request.form['name']
        del phonebook[name]
    except KeyError:
        return render_template('index.html', message=f'{name} is not in the phonebook')
    else:
        return render_template('delete.html', message=f'{name} is deleted from the phonebook')

if __name__ == '__main__':
    app.run()
