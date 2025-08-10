from flask import Flask, render_template, request, jsonify

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
def @app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    # ... (rest of your code)
    
    if not user_message:
        return jsonify({"response": "Mensagem vazia."}), 400
    
    ai_response = get_ai_response(user_message)
    return jsonify({"response": ai_response})

if __name__ == "__main__":
    import os
# ... (rest of your code)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)