from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def home():
    return "Hello, aarti"

@app.route('/hellos')
def test():
    return "Hello, aarti!!!!!!!"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
