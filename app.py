from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Trading Intelligence Engine Online"

@app.route("/radar")
def radar():
    return jsonify({
        "WIN": {
            "sinal": random.choice(["COMPRA","VENDA","AGUARDAR"]),
            "probabilidade": random.randint(60,90),
            "fluxo_institucional": random.choice(["Comprador","Vendedor"])
        },
        "FOREX": {
            "sinal": random.choice(["COMPRA","VENDA","AGUARDAR"]),
            "probabilidade": random.randint(60,90),
            "tendencia": random.choice(["Alta","Baixa"])
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
