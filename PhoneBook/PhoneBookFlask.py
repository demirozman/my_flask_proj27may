from flask import Flask, render_template, request

app = Flask(__name__)
phonebook = {}

def find_contact(name):
    return phonebook.get(name, f"Couldn't find phone number of {name}")

def add_contact(name, phone_number):
        phonebook[name] = phone_number
        return name, phone_number
    

def delete_contact(name):
        return phonebook.pop(name)
        # del phonebook[name]
        #return name
    
@app.route('/', methods='GET')
def index():
    return render_template('index.html', methods='POST')

@app.route('/find', methods=['GET', 'POST'])
def find():
    try:
        name = request.form['name']
        result = find_contact(name)
    except KeyError as err:
        return render_template('index.html', f'{err} is not in the phonebook')   
    else:
        return render_template('find.html', resulty=result)

@app.route('/add', methods=['GET', 'POST'])
def add():
    try:
        name = request.form['name']
        phone_number = request.form['phone_number']
        result=add_contact(name, phone_number)
    #return f'Phone number of {name} is inserted into the phonebook'
    except KeyError as err:
        return render_template('index.html', f'{err} Invalid input format, cancelling operation ...')   
    else:
        return render_template('add.html', resulty=result)
    
@app.route('/delete', methods=['POST'])
def delete():
    try:
        name = request.form['name']
        result = delete_contact(name)
        
    except KeyError as err:
        return render_template('index.html', f'{err} is not in the phonebook')
    else:
        return render_template('delete.html', resulty=result)
@app.route('/exit')
def exit():
    return render_template('exit.html')

if __name__ == '__main__':
    app.run(debug=True)
