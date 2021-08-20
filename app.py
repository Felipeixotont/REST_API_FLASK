from flask import Flask, request, jsonify
import json

app = Flask(__name__)

taskList = list()
'''
[
    {
        'id': '',
        'responsavel': '',
        'tarefa': '',
        'status': ''
    }
]
'''


# Exibir uma tarefa específica, alterar o status de uma tarefa especifica ou deletar uma tarefa especifica.
@app.route('/exibir/<int:id>', methods=['GET', 'POST', 'DELETE'])
def tarefa(id):
    if request.method == 'GET':
        response = taskList[id]
        return jsonify(response)

    elif request.method == 'POST':
        dados = json.loads(request.data)
        att = str(dados['status'])
        taskList[id]['status'] = att
        return jsonify(taskList[id]['status'])

    elif request.method == 'DELETE':
        del taskList[id]

    else:
        print("Erro!")


# cadastrar uma tarefa ou imprimir toda a lista de tarefas.
@app.route('/tarefa/', methods=['PUT', 'GET'])
def responsavel():
    if request.method == 'GET':
        return jsonify(taskList)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
#       taskList[len(taskList)] = dados
        dados['id'] = len(taskList)
        taskList.append(dados)
        return jsonify(dados)


if __name__ == '__main__':
    app.run(debug=True)
