from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Trading Engine Online"

@app.route("/signal")
def signal():
    signals = ["COMPRA", "VENDA", "AGUARDAR"]
    return jsonify({
        "ativo": "WIN",
        "sinal": random.choice(signals),
        "probabilidade": random.randint(60, 85)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
