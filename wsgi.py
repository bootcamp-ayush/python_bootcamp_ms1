from flask import Flask

app = Flask(__name__)


@app.route('/bootcamp')
def handler():
    return 'hello from bootcamp';


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
