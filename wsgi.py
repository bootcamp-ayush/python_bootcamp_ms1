from flask import Flask

app = Flask(__name__)


@app.route('/')
def handler():
    return 'hello from bootcamp'


if __name__ == "__main__":
    app.run(debug=True)
