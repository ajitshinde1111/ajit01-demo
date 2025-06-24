from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client['portfolio_db']
collection = db['contacts']

@app.route('/')
def index():
    return render_template('index.html')  # वापर render_template

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    subject = request.form.get('subject', '')
    message = request.form['message']

    collection.insert_one({
        'name': name,
        'email': email,
        'subject': subject,
        'message': message
    })

    return "✅ Thank you! Your message has been received."

if __name__ == '__main__':
    app.run(debug=True)
