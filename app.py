from flask import Flask, jsonify

app = Flask(__name__)

# Route for root path "/"
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the URL Shortener App!"})

# Optional: health check
@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
