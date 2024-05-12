from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    sport = request.form.get('sport')
    # You can save the user data to a database or perform any other actions here
    return f"Thank you, {name}! You've chosen {sport}."

if __name__ == '__main__':
    app.run(debug=True)
