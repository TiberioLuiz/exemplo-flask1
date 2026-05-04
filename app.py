from flask import Flask, jsonify   ,request 
from models.task import Task


app = Flask(__name__)


tasks = []

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/sobre')
def sobre():
    return 'Sobre a aplicação'


@app.route('/listar')
def listar():
    lista_tarefas = [task.to_dict() for task in tasks]
    resultado = {"tasks": lista_tarefas,
                 "total_tasks": len(lista_tarefas)}
    return jsonify(resultado   ) 


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    print(data)
    id
    task = Task(id = id, name = data['name'], description=data['description'])
    tasks.append(task)
    return jsonify({"message": "Tarefa criada com sucesso"}), 201






if __name__ == '__main__':
    app.run(debug=True)

