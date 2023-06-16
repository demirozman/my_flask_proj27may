from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_password(full_name):
    # Remove any spaces from the full name
    full_name = full_name.replace(" ", "")
    
    # Select three random letters from the full name
    letters = random.sample(full_name.lower(), 3)
    
    # Generate a random four-digit number
    number = random.randint(1000, 9999)
    
    # Combine the letters and number to form the password
    password = "".join(letters) + str(number)
    
    return password

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        full_name = request.form["full_name"]
        password = generate_password(full_name)
        return render_template("result.html", password=password)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=95000)
    #app.run(host= '0.0.0.0', port=80)