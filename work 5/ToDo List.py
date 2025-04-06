tasks = []

def add_task(description):
    tasks.append(description)
    print("Задача успешно добавлена!")

def view_tasks():
    if not tasks:
        print("Список задач пуст.")
    else:
        print("Список задач:")
        for i, task in enumerate(tasks, start=1):
            print(str(i) + ". " + task)

def delete_task(task_id):
    if task_id < 1 or task_id > len(tasks):
        print("Задача с таким номером не найдена.")
    else:
        tasks.pop(task_id - 1)
        print("Задача успешно удалена!")

while True:
    print("Выберите действие:")
    print("1. Добавить задачу")
    print("2. Просмотреть задачи")
    print("3. Удалить задачу")
    print("4. Выйти")
    choice_input = input("> ")
    if not choice_input.isdigit():
        print("Пожалуйста, введите номер действия от 1 до 4.")
        continue
    choice = int(choice_input)
    if choice == 1:
        desc = input("Введите описание задачи: ")
        add_task(desc)
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        task_num_input = input("Введите номер задачи для удаления: ")
        if not task_num_input.isdigit():
            print("Пожалуйста, введите корректный номер задачи.")
        else:
            task_num = int(task_num_input)
            delete_task(task_num)
    elif choice == 4:
        print("Выход из программы.")
        break
    else:
        print("Пожалуйста, выберите действие от 1 до 4.")