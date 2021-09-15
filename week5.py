# with open('todo.txt', 'w') as file:
#     file.write('todo list:')

new_todo = input('please enter a new to do: ')
with open('todo.txt', 'a') as todo:
    todo.write('\n' + new_todo)
with open('todo.txt', 'r') as todo:
    todo_list = todo.read()
print(todo_list)
