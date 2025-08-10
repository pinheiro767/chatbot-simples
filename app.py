from flask import Flask, request, jsonify

app = Flask(__name__)

# Este é um exemplo simples para ilustrar o funcionamento.
# Em um projeto real, você faria a chamada a uma API de IA aqui.
def get_ai_response(user_message):
    # **IMPORTANTE**: Substitua esta lógica pela chamada à API de IA real (ex: Gemini, GPT).
    # Exemplo:
    # from google.generativeai import GenerativeModel
    # model = GenerativeModel('gemini-pro')
    # response = model.generate_content(user_message)
    # return response.text

    # Resposta simulada para este exemplo:
    if "olá" in user_message.lower():
        return "Olá! Em que posso te ajudar hoje?"
    elif "canva" in user_message.lower():
        return "O Canva é uma ótima ferramenta para design gráfico. Quer saber mais sobre ele?"
    else:
        return "Não entendi. Poderia reformular a pergunta?"

@app.route("/")
def home():
    return "O servidor está rodando. Abra o arquivo 'index.html' no seu navegador."

@app.route("/chat", methods=["POST"])
def chat():
    user_data = request.json
    user_message = user_data.get("message")
    
    if not user_message:
        return jsonify({"response": "Mensagem vazia."}), 400
    
    ai_response = get_ai_response(user_message)
    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(debug=True)