# Este é o arquivo app.py, que contém a lógica do servidor Flask para o chatbot.

# Importa as bibliotecas necessárias do Flask e do sistema operacional
from flask import Flask, render_template, request, jsonify
import os
import requests
import json

# Inicializa a aplicação Flask
app = Flask(__name__)

# Configurações da API Gemini
# Deixe a chave da API vazia, o ambiente de execução a fornecerá automaticamente
API_KEY = os.environ.get("GEMINI_API_KEY", "")
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key={API_KEY}"

@app.route("/")
def home():
    """
    Esta rota retorna a página HTML do chatbot.
    """
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """
    Esta rota recebe o histórico da conversa e retorna a resposta da IA.
    """
    # Extrai o histórico da conversa do corpo da requisição JSON
    chat_history = request.json.get("chat_history")

    if not chat_history:
        return jsonify({"response": "Histórico de conversa vazio."}), 400

    try:
        # Prepara o payload para a API Gemini
        payload = {
            "contents": chat_history
        }

        # Chama a API Gemini com o payload
        response = requests.post(API_URL, headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        response.raise_for_status() # Lança um erro para códigos de status HTTP ruins

        result = response.json()

        # Extrai a resposta de texto do resultado da API
        if "candidates" in result and len(result["candidates"]) > 0:
            ai_response = result["candidates"][0]["content"]["parts"][0]["text"]
        else:
            ai_response = "Desculpe, não consegui gerar uma resposta. Tente novamente."

        return jsonify({"response": ai_response})

    except requests.exceptions.RequestException as e:
        print(f"Erro ao chamar a API Gemini: {e}")
        return jsonify({"response": "Desculpe, ocorreu um erro na comunicação com a IA."}), 500
    except (KeyError, IndexError) as e:
        print(f"Erro na estrutura da resposta da API: {e}")
        return jsonify({"response": "Desculpe, ocorreu um erro ao processar a resposta da IA."}), 500


if __name__ == '__main__':
    # Obtém a porta do ambiente do Render ou usa 5000 por padrão
    port = int(os.environ.get("PORT", 5000))
    # Inicia a aplicação Flask, configurada para ser acessível pelo Render
    app.run(host='0.0.0.0', port=port)