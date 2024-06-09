from flask import Flask, render_template, request
from departments import department

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    dream = request.form.get('dream')
    recommended_courses = department.get(dream)

    return render_template('result.html', dream=dream, courses=recommended_courses)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
