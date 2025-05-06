import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='.')

@app.route("/", methods=['GET', 'POST'])
def web():
    price = None
    error_message = None

    if request.method == 'POST':
        pair = request.form['pair'].upper()
        url = f'https://api.binance.com/api/v3/ticker/price?symbol={pair}'
        try:
            response = requests.get(url)
            data = response.json()

            if 'price' in data:
                price = data['price']
            else:
                error_message = "Не удалось получить цену для указанной пары. Проверьте правильность ввода."
        except requests.exceptions.RequestException as e:
            error_message = f"Ошибка подключения к Binance API: {e}"


    return render_template('index.html', price=price, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port='80')
