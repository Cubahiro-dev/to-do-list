from tkinter import *
import json
from PIL import Image, ImageTk
from tkinter import messagebox


# -------- SAVE / LOAD -----
# function to add new task in  the dictionary and to keep the old data of the file
def add_task():
    task = task_name_entry.get()
    date = date_task_entry.get()
    new_data = {
        task: date
    }
    if len(task) == 0 or len(date) == 0:
        messagebox.showwarning(title="ERROR", message="Please don't leave any fields empty")
    else:
        try:
            with open("task.json", "r") as task_file:
                # Reading the tasks on the file
                task = json.load(task_file)
        except FileNotFoundError:
            # If the task_file doesn't exist, create one
            with open("task.json", "w") as task_file:
                json.dump(new_data, task_file, indent=4)
        else:
            # Updating dictionary with new tasks
            task.update(new_data)
            with open("task.json", "w") as task_file:
                # Saving task
                json.dump(task, task_file, indent=4)
        finally:
            task_name_entry.delete(0, END)
            date_task_entry.delete(0, END)


# --------- VIEW TASK -----
# function to get all the keys and contents of the task_dic and put them in to-do-list manner
def get_keys():
    with open("task.json", "r") as task_file:
        task_dic = task_file.read()
        for key in task_dic.keys():
            return f" • {key} : {task_dic[key]}"


# function to see the number of task we have inside the list_file
def view():
    messagebox.showinfo(title="Task", message=f"Your to-do-list is: {get_keys}")


# ------- REMOVE TASK -----
# function to remove a completed task

def remove_task():
    with open("task.json", "r") as task_file:
        task_file = task_file.read()
        if remove_task_entry.get() in task_file:
            q_deletion_task = messagebox.askyesno(title=f"Suppression of {remove_task_entry.get()}",
                                                  message=f"The task "
                                                          f"{remove_task_entry.get()}"
                                                          f" will be deleted.")
            # if q_deletion_task == "yes":
            # Error for deleting the task
            # json.

        else:
            messagebox.showerror(title="Not in the file",
                                 message=f"There is no {remove_task_entry.get()} in the data_file.")


# THE GUI OF THE TO-DO-LIST

# creation of the window: background-color and size of the window
window = Tk()
window.config(bg="#FFC0CB")
window.title("TO-DO-LIST")
window.config(width=1500, height=10000000)

# putting  the images on the window
# Putting the image in a variable
to_do_list_logo_path = "to_do_list_logo.png"
toDoListLogo = ImageTk.PhotoImage(Image.open(to_do_list_logo_path))

notebook_path = "timer_4_img.webp"
notebook_img = ImageTk.PhotoImage(Image.open(notebook_path))

# Putting in a label
to_do_list_logo_label = Label(window, image=toDoListLogo)
to_do_list_logo_label.config(highlightthickness=0, bg="#FFC0CB")
to_do_list_logo_label.grid(column=1, row=0)

# notebook_label = Label(window, image=notebook_img)
# notebook_label.config(highlightthickness=0, height=330, width=300, bg="#FFC0CB")
# notebook_label.grid(column=1, row=4)

# Labels ' creation
task_name_label = Label(text="Name: ", bg="#FFC0CB", font=("Times", "24", "bold italic"))
task_name_label.grid(column=0, row=1)

date_task_label = Label(text="Due Date: ", bg="#FFC0CB", font=("Times", "24", "bold italic"))
date_task_label.grid(column=0, row=2)

remove_task_label = Label(text="Remove task: ", bg="#FFC0CB", font=("Times", "24", "bold italic"))
remove_task_label.grid(column=0, row=3)

# Entries' creation
task_name_entry = Entry(width=45)
task_name_entry.insert(0, "Put any task of your choice")
task_name_entry.grid(column=1, row=1, sticky="ew")

date_task_entry = Entry(width=45)
date_task_entry.insert(0, "e.g day/month/year")
date_task_entry.grid(column=1, row=2, sticky="ew")

remove_task_entry = Entry(width=45)
remove_task_entry.insert(0, "Put the name of the task to remove")
remove_task_entry.grid(column=1, row=3, sticky="ew")

# Buttons ' creation
view_task_button = Button(text="View", width=25, highlightthickness=0, bg="#0000FF", font=("Calibri", "10", "bold"),
                          command=view)
view_task_button.grid(column=2, row=4)

save_load_task_button = Button(text="Save / Load", width=25, highlightthickness=0, bg="#90ee90",
                               font=("Calibri", "10", "bold"), command=add_task)
save_load_task_button.grid(column=0, row=4)

remove_task_button = Button(text="Remove", width=15, highlightthickness=0, bg="red", font=("Calibri", "10", "bold"),
                            command=remove_task)
remove_task_button.grid(column=3, row=3, padx=10)

window.mainloop()
