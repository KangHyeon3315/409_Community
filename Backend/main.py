from flask import Flask ,request
from Router.Login import login_bp


app = Flask(__name__)

if __name__ == "__main__":

    app.register_blueprint(login_bp)

    app.run(port=7209, debug=False)
