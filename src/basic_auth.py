from functools import wraps

from flask import Flask, jsonify, request

app = Flask(__name__)

USERS = {
    "user1": "password1",
}


def check_auth(username, password) -> bool:
    """Check authorization data of user"""

    return username in USERS and USERS.get(username) == password


def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization

        if not (auth) or not check_auth(auth.username, auth.password):
            return (
                "Unauthorized",
                401,
                {"WWW-Authenticate": 'Basic realm="Login Required"'},
            )

        return f(*args, **kwargs)

    return decorated


@app.route("/api/data", methods=["GET"])
@require_auth
def get_data():
    return jsonify({"message": "Protected data"})


if __name__ == "__main__":
    app.run(debug=True)
