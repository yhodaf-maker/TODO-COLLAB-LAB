from todo import add_task, list_tasks, remove_last_task, update_first_task,count_tasks

add_task("Initial task by A")
add_task("B: buy groceries")
add_task("A: clean room")
tasks = list_tasks()
for t in tasks:
    print(t)
    
remove_last_task()
add_task("B: replaced last task")

update_first_task("A: updated first task")

print("Run by A")
print("Run by B")
print("Total tasks:", count_tasks())