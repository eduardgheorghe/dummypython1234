from flask import Blueprint, jsonify

bp = Blueprint("routes", __name__)

@bp.route("/")
def index():
    return "<h1>Simple Web App</h1><p>Hello from Flask!</p>"

@bp.route("/health")
def health():
    return jsonify({"status": "ok"})

@bp.route("/hello/<name>")
def hello(name):
    return jsonify({"message": f"Hello, {name}!"})

