from flask import Flask, render_template, request
from departments import department
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    dream = request.form.get('dream')
    recommended_courses = department.get(dream)

    return render_template('result.html', dream=dream, courses=recommended_courses)



app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    port = random.randint(5000, 5100)
    app.run(port=port)
