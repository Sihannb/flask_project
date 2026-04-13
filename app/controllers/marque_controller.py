from flask import Blueprint, render_template, request, jsonify
from app.services.marque_service import get_next_marque, get_stats, handle_click

marque_bp = Blueprint("marque", __name__)


@marque_bp.route("/")
def index():
    marque = get_next_marque()
    stats = get_stats()
    return render_template("index.html", marque=marque, stats=stats)


@marque_bp.route("/apropos")
def apropos():
    return render_template("apropos.html")


@marque_bp.route("/click", methods=["POST"])
def click():
    data = request.get_json() or {}

    nom = data.get("marque")
    action = data.get("action")

    if not nom:
        return jsonify({"error": "marque manquante"}), 400

    result = handle_click(nom, action)

    return jsonify(result)