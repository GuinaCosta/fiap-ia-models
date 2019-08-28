# import das dependencias do Flask
from flask import Flask, request, make_response, jsonify

# inicializa a app do flask
app = Flask(__name__)

# rota default
@app.route('/')
def index():
   return 'hello world!'

# funcao de respostas
def results():
    # constroi o objeto de respostas
    req = request.get_json(force=True)

    # pega a acao do json
    action = req.get('queryResult').get('action')

    # retorna o fulfillment do response
    return {'fulfillmentText': 'This is a response from webhook'}

#cria uma rota para o webhook
@app.route('/webhook', methods=['GET','POST'])
def webhook():
    # retorno da resposta
    return make_response(jsonify(results()))

# executa a aplicação
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)