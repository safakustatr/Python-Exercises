def todo_list(task_list, command):
    if command == '1':
        #Add task
        new_task = input('Enter new task: ')
        task_list.append({'task' : new_task , 'done' : False})
        return task_list
    elif command == '2':
        #View tasks
        for task in task_list:
            status = '✓' if task['done'] == True else '✕'
            print(str(task_list.index(task) + 1) + '. ' + task['task'] + ' ' + status)
        return task_list
    elif command == '3':
        #Remove task
        to_remove = int(input('Which task would you like to remove? : '))
        if 1 <= to_remove <= len(task_list):
            print('Removing \'' + task_list[to_remove - 1]['task'] + '\'')
            task_list.pop(to_remove - 1)
            return task_list
        else:
            print('Invalid input')
            return task_list
    elif command == '4':
        #Mark task as done
        to_mark = int(input('Which task would you like to mark? : '))
        if 1 <= to_mark <= len(task_list):
            print('Marking \'' + task_list[to_mark - 1]['task'] + '\' as done')
            task_list[to_mark - 1]['done'] = True
        else:
            print('Invalid input')
        return task_list
    elif command == '5':
        #Exit
        return task_list
    return task_list

print('To-Do List')
print('---')
print('1. Add task')
print('2. View tasks')
print('3. Remove task')
print('4. Mark task as done')
print('5. Exit')

tasks = [
    {'task': 'Study Python', 'done': False},
    {'task': 'Study AI', 'done': False},
    {'task': 'Shave your beard', 'done': False},
    {'task': 'Get a haircut', 'done': False},
    {'task': 'Clean the bathroom', 'done': False}
]

while True:
    command = input('What would you like to do? : ')
    if command == '5':
        break
    tasks = todo_list(tasks, command)