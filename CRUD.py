tasks = []

def create_task(task_name):
    """Создание новой задачи (Create)"""
    new_task = {"id": len(tasks) + 1, "name": task_name, "completed": False}
    tasks.append(new_task)
    print(f"Задача создана: {new_task}")

def read_tasks():
    """Чтение всех задач (Read)"""
    if not tasks:
        print("Список задач пуст.")
    else:
        print("Список задач:")
        for task in tasks:
            print(f"- ID: {task['id']}, Название: {task['name']}, Завершена: {task['completed']}")

def update_task(task_id, new_name=None, completed_status=None):
    """Обновление задачи (Update)"""
    for task in tasks:
        if task['id'] == task_id:
            if new_name is not None:
                task['name'] = new_name
            if completed_status is not None:
                task['completed'] = completed_status
            print(f"Задача с ID {task_id} обновлена: {task}")
            return
    print(f"Задача с ID {task_id} не найдена.")

def delete_task(task_id):
    """Удаление задачи (Delete)"""
    global tasks
    initial_len = len(tasks)
    tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) < initial_len:
        print(f"Задача с ID {task_id} удалена.")
    else:
        print(f"Задача с ID {task_id} не найдена.")

# Примеры использования:

# C - Create (Создание)
create_task("Изучить CRUD операции")
create_task("Написать код для примера")

# R - Read (Чтение)
read_tasks()

# U - Update (Обновление)
update_task(1, completed_status=True)
update_task(2, new_name="Написать пример на Python")

# R - Read (Чтение после обновления)
read_tasks()

# D - Delete (Удаление)
delete_task(2)

# R - Read (Чтение после удаления)
read_tasks()