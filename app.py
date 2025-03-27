from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Функция для получения цитаты с обработкой ошибок
def get_quote():
    try:
        response = requests.get('https://api.quotable.io/random', timeout=5)
        response.raise_for_status()  # Проверяем на ошибки HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_quote')
def api_get_quote():
    quote = get_quote()
    if quote:
        return jsonify({
            'content': quote['content'],
            'author': quote['author']
        })
    else:
        return jsonify({
            'error': 'Не удалось получить цитату'
        }), 500

if __name__ == '__main__':
    app.run(debug=True)