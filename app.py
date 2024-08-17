from flask import Flask, render_template, request

app = Flask(__name__)

# Dados do pedido
pedido = {
    "numero": 0,
    "produtos": [
        {"nome": "produto_1", "preco": 15, "quantidade": 0},
        {"nome": "produto_2", "preco": 25, "quantidade": 0},
        {"nome": "produto_3", "preco": 12, "quantidade": 0},
        {"nome": "produto_4", "preco": 15, "quantidade": 0},
        {"nome": "produto_5", "preco": 18, "quantidade": 0},
        {"nome": "produto_6", "preco": 6, "quantidade": 0},
        {"nome": "produto_7", "preco": 5, "quantidade": 0},
        {"nome": "produto_8", "preco": 10, "quantidade": 0}
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
    return render_template('pedido.html', pedido=pedido, total_pedido=total_pedido)

if __name__ == '__main__':
    app.run(debug=True)
