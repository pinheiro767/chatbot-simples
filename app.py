# Importa as bibliotecas necessárias do Flask e do sistema operacional
from flask import Flask, render_template, request, jsonify
import os

# Inicializa a aplicação Flask
app = Flask(__name__)

# Este é um exemplo simples para ilustrar o funcionamento.
# Em um projeto real, você faria a chamada a uma API de IA aqui.
def get_ai_response(user_message):
    """
    Função para obter a resposta da IA.
    Substitua esta lógica pela chamada à API de IA real (ex: Gemini, GPT).
    """
    if "olá" in user_message.lower():
        return "Olá! Em que posso te ajudar hoje?"
    elif "canva" in user_message.lower():
        return "O Canva é uma ótima ferramenta para design gráfico. Quer saber mais sobre ele?"
    else:
        return "Não entendi. Poderia reformular a pergunta?"

@app.route("/")
def home():
    """
    Esta rota retorna a página HTML do chatbot.
    """
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """
    Esta rota recebe a mensagem do usuário e retorna a resposta da IA.
    """
    # Extrai a mensagem do usuário do corpo da requisição JSON
    user_message = request.json.get("user_message")

    if not user_message:
        return jsonify({"response": "Mensagem vazia."}), 400

    # Obtém a resposta da IA com base na mensagem do usuário
    ai_response = get_ai_response(user_message)
    return jsonify({"response": ai_response})

if __name__ == '__main__':
    # Obtém a porta do ambiente do Render ou usa 5000 por padrão
    port = int(os.environ.get("PORT", 5000))
    # Inicia a aplicação Flask, configurada para ser acessível pelo Render
    app.run(host='0.0.0.0', port=port)

