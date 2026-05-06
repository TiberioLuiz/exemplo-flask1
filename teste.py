import pytest
import requests

BASE_URL = "http://localhost:5000"
tasks=[]


def test_create_task():
    payload = {
        "name": "tarefa de teste",
        "description": "Essa é uma tarefa de teste",
        "completed": False
    }
    response = requests.post(f"{BASE_URL}/tasks", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["message"] == "Tarefa criada com sucesso"


def test_listar():
    response = requests.get(f"{BASE_URL}/listar")
    assert response.status_code == 200
    data = response.json()
    tarefas = data["tasks"]
    print(tarefas)
    assert "tasks" in data
    assert "total_tasks" in data
    assert "completed" in tarefas[0]
    
    

def test_listar2():
    response = requests.get(f"{BASE_URL}/listar")
    data = response.json()
    tarefas = data["tasks"]
    print ("type de response: ", type(response)  )
    print ("type de data: ", type(data  )  )
    print ("type de tarefas: ", type(tarefas)  )
    tarefa = tarefas[0]
    print ("type de tarefa: ", type(tarefa)  )
    print(tarefa)


if __name__ == '__main__':
    print ("Iniciando testes...")
    test_listar2()

# if __name__ == '__main__':
#     x = [1,2,3]
#     y = None
#     z=list(filter(lambda t: t == 72, x))


#     if z:
#         print ("Z é verdadeiro")
#     else:
#         print ("Z é falso") 

#     if y is not None:
#         print ("Y é verdadeiro")
#     else:
#         print ("Y é falso")      


