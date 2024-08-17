# Frente de Caixa Simples

Este é um projeto de um sistema de frente de caixa simples desenvolvido como uma aplicação web. O objetivo do projeto é demonstrar como implementar um sistema de controle de pedidos e produtos com base em uma planilha que utilizavámos nas feiras.

## Descrição

Este projeto simula um sistema de frente de caixa onde é possível visualizar e atualizar pedidos e quantidades de produtos. A aplicação permite:

- Exibir detalhes de um pedido, incluindo produtos, preços e quantidades.
- Alterar a quantidade dos produtos e visualizar a atualização do total do pedido em tempo real.
- Imprimir o pedido com os detalhes atualizados.

## Tecnologias Utilizadas

- **Backend**: [Flask](https://flask.palletsprojects.com/) (framework web em Python)
- **Frontend**: HTML, CSS, JavaScript
- **Controle de Versão**: Git

## Estrutura do Projeto

- `app.py`: O arquivo principal que define a aplicação Flask, processa os dados e renderiza o template HTML.
- `templates/pedido.html`: O template HTML que exibe os detalhes do pedido e inclui um formulário para atualizar as quantidades dos produtos.

## Como Executar

1. **Clone o Repositório**

   Clone o repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
   cd NOME_DO_REPOSITORIO
