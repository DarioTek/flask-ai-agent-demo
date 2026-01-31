from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)

# templates/home.html
"""
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Flask App</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>
    <div class="container mt-5">
      <div class="card shadow-sm">
        <div class="card-body">
          <h1 class="card-title text-center mb-4">Hello World</h1>
        </div>
      </div>
    </div>
  </body>
</html>
"""

# tests/test_routes.py
import pytest
from app import app

def test_health_route():
    with app.test_client() as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.is_json
        assert response.get_json() == {"status": "ok"}