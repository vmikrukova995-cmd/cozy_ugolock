from flask import Flask, request, jsonify
from flask_cors import CORS
lumieria_server = Flask(__name__)
CORS(lumieria_server)
polzovateli = {}
@lumieria_server.route('/register', methods=['POST'])
def registracia():
    dannie = request.get_json()
    login = dannie.get('login')
    parol = dannie.get('parol')

    if len(login) < 8:
        return jsonify({"uspeh": False, "soobshenie": "Логин должен быть не короче 8 символов"})
    if len(parol) < 8:
        return jsonify({"uspeh": False, "soobshenie": "Пароль должен быть не короче 8 символов"})
    if login in polzovateli:
        return jsonify({"uspeh": False, "soobshenie": "Такой пользователь уже есть"})
    
    polzovateli[login] = parol
    return jsonify({"uspeh": True, "soobshenie": "Ура! Теперь ты часть этой Вселенной!"})
if __name__ == '__main__':
    lumieria_server.run(debug=True)