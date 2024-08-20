from flask import Flask, render_template, request

app = Flask(__name__)

# Dados do pedido inicial
pedido = {
    "numero": 1,
    "produtos": [
        {"nome": "CORN DOG", "preco": 18, "quantidade": 0},
        {"nome": "HAND ROLL", "preco": 28, "quantidade": 0},
        {"nome": "TONKATSU", "preco": 22, "quantidade": 0},
        {"nome": "ONIGIRI", "preco": 12, "quantidade": 0},
        {"nome": "TAKOYAKI", "preco": 28, "quantidade": 0},
        {"nome": "MOCHI", "preco": 12, "quantidade": 0},
        {"nome": "CHIFFON CAKE", "preco": 22, "quantidade": 0},
        {"nome": "CHÁ GELADO", "preco": 10, "quantidade": 0},
        {"nome": "ADIC.TARÊ", "preco": 5, "quantidade": 0},
        {"nome": "REFRI", "preco": 6, "quantidade": 0},
        {"nome": "ÁGUA", "preco": 5, "quantidade": 0}
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
