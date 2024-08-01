from tkinter import *
import json
from PIL import Image, ImageTk
from tkinter import messagebox


# -------- SAVE / LOAD -----
# function to add new task in  the dictionary and to keep the old data of the file
def add_task():
    # Getting the task_name and the due date
    task = task_name_entry.get()
    date = date_task_entry.get()
    # Putting into a dictionary
    new_data = {
        task: {
            "due_date": date,
            "status": "🔴",

        }
    }
    if len(task) == 0 or len(date) == 0:
        messagebox.showwarning(title="ERROR", message="Please don't leave any fields empty")
    else:
        # Controlling errors
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
# Function to get all the keys of dic and the contents
def get_keys():
    with open("task.json") as task_file:
        task = task_completed_entry.get()
        # Creation of a string variable which will contain the task in a list form
        list_task = ""
        data_task = json.load(task_file)
        # Concatenating the task inside the list_task
        for key in data_task.keys():
            list_task += f"{data_task[key]['status']} {key} : {data_task[key]['due_date']}\n"
        return list_task


# function to see the number of task we have inside the list_file
def view():
    messagebox.showinfo(title="Task", message=f"Your to-do-list is: \n{get_keys()}")


# ------- REMOVE TASK -----
# function to remove a completed task

def remove_task():
    with open("task.json", "r") as task_file:
        task_file = json.load(task_file)
        deleted_task = remove_task_entry.get()  # If the user have put the right name but in caps
        if deleted_task in task_file:
            # q_deletion_task = messagebox.askyesno(title=f"Suppression of {remove_task_entry.get()}",
            #                                       message=f"The task "
            #                                               f"{remove_task_entry.get()}"
            #                                               f" will be deleted.")
            # if q_deletion_task == "yes":
            task_file.pop(f"{deleted_task}")
            with open("task.json", "w") as data_task:
                json.dump(task_file, data_task, indent=4)
        else:
            messagebox.showerror(title="Not in the file",
                                 message=f"There is no {deleted_task} in the data_file.")
        remove_task_entry.delete(0, END)


# ------- TASK COMPLETED -----

def task_completed():
    task = task_completed_entry.get()
    with open("task.json") as task_file:
        data_task = json.load(task_file)
        if task in data_task.keys():
            data_task[task]["status"] = "✔️"
            with open("task.json", "w") as task_file:
                json.dump(data_task, task_file, indent=4)
            task_completed_entry.delete(0, END)
        else:
            messagebox.showerror(message=f"There is no {task} in the data file.")


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

# Labels ' creation
task_name_label = Label(text="Name: ", bg="#FFC0CB", font=("Times", "24", "bold italic"))
task_name_label.grid(column=0, row=1)

date_task_label = Label(text="Due Date: ", bg="#FFC0CB", font=("Times", "24", "bold italic"))
date_task_label.grid(column=0, row=2)

remove_task_label = Label(text="Remove task: ", bg="#FFC0CB", font=("Times", "24", "bold italic"))
remove_task_label.grid(column=0, row=3)

task_completed_label = Label(text="Task Completed: ", bg="#FFC0CB", font=("Times", "24", "bold italic"))
task_completed_label.grid(column=0, row=4)

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

task_completed_entry = Entry(width=45)
task_completed_entry.insert(0, "Put the name of the task you have completed!")
task_completed_entry.grid(column=1, row=4, sticky="ew")

# Buttons ' creation
view_task_button = Button(text="View", width=25, highlightthickness=0, bg="#0000FF", font=("Calibri", "10", "bold"),
                          command=view)
view_task_button.grid(column=2, row=5)

save_load_task_button = Button(text="Save / Load", width=25, highlightthickness=0, bg="#90ee90",
                               font=("Calibri", "10", "bold"), command=add_task)
save_load_task_button.grid(column=0, row=5)

remove_task_button = Button(text="Remove", width=25, highlightthickness=0, bg="red", font=("Calibri", "10", "bold"),
                            command=remove_task)
remove_task_button.grid(column=2, row=3, padx=5)

task_completed_button = Button(text="Finish", width=25, highlightthickness=0, bg="yellow",
                               font=("Calibri", "10", "bold"), command=task_completed)
task_completed_button.grid(column=2, row=4)

window.mainloop()
