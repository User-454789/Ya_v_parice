tasks = {
    "Задача 1": "В процессе",
    "Задача 2": "Новая",
    "Задача 3": "Завершена"
}

# Функция для изменения статуса задачи
def change_task_status(task_name, new_status):
    if task_name in tasks:
        tasks[task_name] = new_status
        print(f"Статус задачи '{task_name}' изменен на '{new_status}'.")
    else:
        print(f"Задача '{task_name}' не найдена.")

# Изменяем статус задачи
change_task_status("Задача 2", "В процессе")

# Выводим обновленный словарь задач
print(tasks)