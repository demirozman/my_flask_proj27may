from flask import Flask, render_template, request, url_for

app = Flask(__name__)
phonebook = {}

def finding(keyword):
    return phonebook.get(keyword, f"Couldn't find phone number of {keyword}")

def addition(name, phone_number):
    
    phone_number = request.form['phone_number']
    phonebook[name] = phone_number
    

def deletion(name):
    try:
        phonebook.pop(name)
    except KeyError as err:
        return f'{err} is not in the phonebook'
    else:
        return f'{name} is deleted from the phonebook'
    
@app.route('/')
def index():
    return render_template('index.html', methods='GET')

@app.route('/add', methods=['GET', 'POST'])
def add():
    try:
        name = request.form['name']
        return f'Phone number of {name} is inserted into the phonebook'
    except KeyError:
        return render_template('index.html', message='Invalid input format, cancelling operation ...')
    else:
        return render_template('add.html', message=f'Phone number of {name} is inserted into the phonebook')

@app.route('/find', methods=['GET', 'POST'])
def find():
    try:
        name = request.form['name']
        phone_number = phonebook[name]
    except KeyError:
        return render_template('index.html', message=f"Couldn't find phone number of {name}")
    else:
        return render_template('find.html', message=f'Phone number of {name} is {phone_number}')

@app.route('/delete', methods=['GET'])
def delete():
    try:
        name = request.form['name']
        del phonebook[name]
    except KeyError:
        return render_template('index.html', message=f'{name} is not in the phonebook')
    else:
        return render_template('delete.html', message=f'{name} is deleted from the phonebook')

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=80)
