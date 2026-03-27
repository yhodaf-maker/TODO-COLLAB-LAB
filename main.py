from todo import add_task, list_tasks

add_task("Initial task by A")
add_task("B: buy groceries")
add_task("A: clean room")
tasks = list_tasks()
for t in tasks:
    print(t)
    
