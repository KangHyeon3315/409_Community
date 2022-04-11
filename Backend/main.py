from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    # TODO app에 Router 추가하기

    app.run(port=7209, debug=False)
