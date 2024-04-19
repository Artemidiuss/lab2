from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Додаємо CORS до нашого додатку Flask

# Функція, яка повертає дані про каву
def get_coffee_data():
    coffee_data = [
        {"name": "Americano", "image": "svg/barista-icons_americano.svg", "price": "$2.50"},
        {"name": "Espresso", "image": "svg/barista-icons_espresso.svg", "price": "$1.80"},
        {"name": "Cafe-Latte", "image": "svg/barista-icons_cafe-latte.svg", "price": "$3.00"},
        {"name": "Cappuccino", "image": "svg/barista-icons_cappuccino.svg", "price": "$3.20"},
        {"name": "Flat-White", "image": "svg/barista-icons_flat-white.svg", "price": "$3.00"},
        {"name": "Latte-Macchiato", "image": "svg/barista-icons_latte-macchiato.svg", "price": "$3.20"},
        {"name": "Moccacino", "image": "svg/barista-icons_moccacino.svg", "price": "$3.50"},
        {"name": "Frappuccino-Milk-Shake", "image": "svg/barista-icons_frappuccino-milk-shake.svg", "price": "$4.00"}
    ]
    return coffee_data

# Функція, яка повертає дані про зерна
def get_beans_data():
    beans_data = [
        {"name": "Brazil, Santos", "image": "Brasil_Santos.png", "price": "$13.00"},
        {"name": "Brazil, Mogiana", "image": "Brasil_Mogiana_2502.png", "price": "$18.00"},
        {"name": "Ethiopia, Sidamo Grade", "image": "ethiopia_sidamo_gr2.png", "price": "$27.00"},
        {"name": "Brazil, Sul de Minas", "image": "brasil.sui-de-minas-0.2.png", "price": "$28.00"}
    ]
    return beans_data

# Роут для отримання даних про каву
@app.route('/coffee', methods=['GET'])
def get_coffee():
    return jsonify(get_coffee_data())

# Роут для отримання даних про зерна
@app.route('/beans', methods=['GET'])
def get_beans():
    return jsonify(get_beans_data())

@app.route('/order', methods=['POST'])
def order():
    if request.method == 'POST':
        phone_number = request.json.get('phone')
        if phone_number:
            print("Отриманий номер телефону:", phone_number)
            return "Замовлення на номер: " + phone_number + " отримано"
        else:
            return "Введіть номер!"

if __name__ == '__main__':
    app.run(debug=True)
