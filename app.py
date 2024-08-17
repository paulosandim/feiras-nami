from flask import Flask, render_template, request

app = Flask(__name__)

# Dados do pedido inicial
pedido = {
    "numero": 1,
    "produtos": [
        {"nome": "corn_dog", "preco": 18, "quantidade": 0},
        {"nome": "hand_roll", "preco": 28, "quantidade": 0},
        {"nome": "tonkatsu", "preco": 22, "quantidade": 0},
        {"nome": "onigiri", "preco": 12, "quantidade": 0},
        {"nome": "takoyaki", "preco": 28, "quantidade": 0},
        {"nome": "mochi", "preco": 12, "quantidade": 0},
        {"nome": "chiffon_cake", "preco": 22, "quantidade": 0},
        {"nome": "cha_gelado", "preco": 10, "quantidade": 0},
        {"nome": "adicional_tare", "preco": 5, "quantidade": 0},
        {"nome": "refri", "preco": 6, "quantidade": 0},
        {"nome": "agua", "preco": 5, "quantidade": 0}
    ]
}

def calcular_total_pedido():
    return sum(produto["preco"] * produto["quantidade"] for produto in pedido["produtos"])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Atualiza o número do pedido
        pedido["numero"] = int(request.form.get('numero_pedido', pedido["numero"]))

        # Processa as quantidades atualizadas do formulário
        for produto in pedido["produtos"]:
            nome_produto = produto["nome"]
            nova_quantidade = request.form.get(f"quantidade_{nome_produto}")
            if nova_quantidade is not None:
                produto["quantidade"] = int(nova_quantidade)

    total_pedido = calcular_total_pedido()
    return render_template('index.html', pedido=pedido, total_pedido=total_pedido)

if __name__ == '__main__':
    app.run(debug=True)
