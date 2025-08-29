import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/myField14")
def get_field14():
    open_id = request.args.get("open_id")
    if not open_id:
        return jsonify({"error": "open_id eksik"}), 400

    url = f"https://ffbd-v2.vercel.app/field14_bySamiul?open_id={open_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        field_14 = data.get("field_14", "")
        
        # Sadece okunabilir karakterleri al
        readable = ''.join(c for c in field_14 if c.isprintable())
        return readable  # JSON değil, direkt string döndür
    except Exception as e:
        return jsonify({"error": str(e)}), 500
