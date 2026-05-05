from flask import Flask, jsonify   ,request 
from models.task import Task


app = Flask(__name__)


tasks = []
tasks.append(Task(id=1, name="Comprar leite", description="Comprar 2 litros de leite", completed=False))
tasks.append(Task(id=2, name="Estudar Flask", description="Ler a documentação do Flask e criar um projeto de exemplo", completed=False))
tasks.append(Task(id=3, name="Fazer exercícios", description="Resolver exercícios de Flask", completed=False))
tasks.append(Task(id=5, name="Fazer exercícios Número 2", description="Resolver exercícios de Flask 2", completed=False))

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/sobre/<string:nome>', methods=['GET'])
def sobre(nome):
    return f'Sobre a aplicação - {nome}'





@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    lista_tarefas = [task.to_dict() for task in tasks]
    lista_tarefas = list(filter(lambda t: t['id'] == task_id, lista_tarefas))
    resultado = {"tasks": lista_tarefas,
                 "total_tasks": len(lista_tarefas)}
    
    if len(lista_tarefas) > 0:
        return jsonify(resultado , 200)
    else:
        return jsonify({"message": "Tarefa não encontrada"}, 404)   


@app.route('/listar', methods=['GET'])
def listar():
    lista_tarefas = [task.to_dict() for task in tasks]
    resultado = {"tasks": lista_tarefas,
                 "total_tasks": len(lista_tarefas)}
    print (resultado)
    return jsonify(resultado   ) 


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    id = tasks[len(tasks)-1].id + 1 if tasks and tasks.__len__() > 0 else 1
    task = Task(id = id, name = data['name'], description=data['description'])
    print (task.to_dict())
    tasks.append(task)
    return jsonify({"message": "Tarefa criada com sucesso"}), 201


@app.route('/tasks', methods=['PUT'])
def update_task():
    data = request.get_json()
    if 'id' not in data:
        return jsonify({"message": "ID da tarefa é obrigatório"}, 400)
    id = data['id']
    task_filter = list(filter(lambda t: t.id == id, tasks))
    if not task_filter or len(task_filter) == 0:
        return jsonify({"message": "Tarefa não encontrada"}, 404)   
    
    task = task_filter[0]
    task.name = data['name'] if 'name' in data else task.name
    task.description =     data['description'] if 'description' in data else task.description
    task.completed = data['completed'] if 'completed' in data else task.completed

    print (task.to_dict())
    return jsonify({"message": "Tarefa atualizada com sucesso"}), 200

def get_task_by_id(task_id):


    task_filter = list(filter(lambda t: t.id == task_id, tasks))
    return task_filter[0] if task_filter else None



@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delet_task(task_id):
    
    task = get_task_by_id(task_id)
    
    if task:
        tasks.remove(task)
        return jsonify({"message": "Tarefa deletada com sucesso"}, 200)
    else:
        return jsonify({"message": "Tarefa não encontrada"}, 404)   



if __name__ == '__main__':
    app.run(debug=True)

