from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    from Router.Login import login_bp
    app.register_blueprint(login_bp)

    app.run(port=7209, debug=False)
