import tkinter 
import tkinter.messagebox

window = tkinter.Tk()
window.title("To Do List")

def task_addfunction():
    todo = task_add.get()
    if len(todo)!=0:
        todo_list.insert(tkinter.END,todo,)
        task_add(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning("Attention !", message="please write a task")

def task_delete():
    try:
        select=todo_list.curselection()
        todo_list.delete(select[0])
    except:
        tkinter.messagebox.showwarning("Attention !", message="please select to delete")



task_frame = tkinter.Frame(window)
task_frame.pack()

todo_list=tkinter.Listbox( task_frame,height=20,width=30)
todo_list.pack(side="left", fill="y",pady=0)

task_add=tkinter.Entry(window,width=40)
task_add.pack(side="bottom")


add_button=tkinter.Button(window, text="CLICK TO ADD TASK",font=("serif",10,"bold"),background="green",width=20, command=task_addfunction)
add_button.pack(side="bottom")

remove_button=tkinter.Button(window, text="CLICK TO DELETE TASK",font=("serif",10,"bold"),background="red",width=20, command=task_delete)
remove_button.pack(side="bottom")


window.mainloop()