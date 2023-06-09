from flask import Flask, session
#import keycloak
from keycloak.extensions.flask import keycloak
#from keycloak.extensions.flask import AuthenticationMiddleware


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret0123456789"
#app.wsgi_app = AuthenticationMiddleware(
app.wsgi_app = keycloak(
    app.wsgi_app,
    app.config,
    app.session_interface,
    callback_url="http://localhost:5000/kc/callback",
    login_redirect_uri="/home",
    logout_redirect_uri="/logout",
)


@app.route("/home")
def home():
    user = session["user"]
    return f"Howdy {user}"


@app.route("/logout")
def logout():
    return "User logged out successfully"


if __name__ == "__main__":
    app.run()