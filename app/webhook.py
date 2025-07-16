from flask import Blueprint, request, abort
import os

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route("/webhook", methods=["POST"])
def flutterwave_webhook():
    # Validate secret hash here
    secret_hash = os.getenv("FLUTTERWAVE_WEBHOOK_HASH")
    signature = request.headers.get("verif-hash")
    if secret_hash and signature != secret_hash:
        abort(403)
    data = request.get_json()
    # Process Flutterwave event here
    return "OK", 200
