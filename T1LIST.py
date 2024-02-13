from tkinter import *
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.master.geometry("665x400+550+250")
        self.master.resizable(0, 0)


        self.tasks = []

        self.functions_frame = Frame(master, bg="purple")
        self.functions_frame.pack(side="top", expand=True, fill="both")

        self.task_label = Label(self.functions_frame, text="Enter the Task :",
                                font=("arial", "14", "bold"),
                                background="#8EE5EE",
                                foreground="#FF6103"
                                )
        self.task_label.place(x=10, y=30)

        self.task_field = Entry(
            self.functions_frame,
            font=("Arial", "14"),
            width=30,
            foreground="black",
            background="white",
        )
        self.task_field.place(x=180, y=30)

        self.add_button = Button(
            self.functions_frame,
            text="Add",
            width=15,
            bg='#D4AC0D', font=("arial", "14", "bold"),
            command=self.add_task,
        )

        self.del_button = Button(
            self.functions_frame,
            text="Remove",
            width=15,
            bg='#D4AC0D', font=("arial", "14", "bold"),
            command=self.delete_task,
        )



        self.exit_button = Button(
            self.functions_frame,
            text="Exit",
            width=52,
            bg='#D4AC0D', font=("arial", "14", "bold"),
            command=self.close
        )

        self.add_button.place(x=18, y=80)
        self.del_button.place(x=240, y=80)
        self.exit_button.place(x=17, y=330)

        self.task_listbox = Listbox(
            self.functions_frame,
            width=30,
            height=6,
            font="bold",
            selectmode='SINGLE',
            background="salmon",
            foreground="BLACK",
            selectbackground="purple",
            selectforeground="BLACK"
        )
        self.task_listbox.place(x=17, y=140)

        self.list_update()

    def add_task(self):
        task_string = self.task_field.get()
        if len(task_string) == 0:
            messagebox.showinfo('Error', 'Field is Empty.')
        else:
            self.tasks.append(task_string)
            self.list_update()
            self.task_field.delete(0, 'end')

    def list_update(self):
        self.clear_list()
        for task in self.tasks:
            self.task_listbox.insert('end', task)

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            removed_task = self.tasks.pop(selected_index)
        except IndexError:
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')



    def clear_list(self):
        self.task_listbox.delete(0, 'end')

    def close(self):
        print(self.tasks)
        self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    app = ToDoListApp(root)
    root.mainloop()
