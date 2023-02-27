import tkinter as tk
import os
from tkinter.filedialog import askdirectory
from tkinter.font import Font

class NoteApp:
    def __init__(self, master):
        self.master = master
        master.title("Note App")

        # Create a frame for the input widgets
        input_frame = tk.Frame(master, bg="#c7fffe")
        input_frame.pack(pady=10)

        # Create a label for the title of the note
        title_label = tk.Label(input_frame, text="Title:", bg="#c7fffe")
        title_label.grid(row=0, column=0, sticky="W")

        # Create an entry widget for the title
        self.title_entry = tk.Entry(input_frame)
        self.title_entry.grid(row=0, column=1)

        # Create a label for the note text
        note_label = tk.Label(input_frame, text="Note:", bg="#c7fffe")
        note_label.grid(row=1, column=0, sticky="W", pady=10)

        # Create a text widget for taking notes
        self.note_text = tk.Text(input_frame, height=20, width=40)
        self.note_text.grid(row=1, column=1)

        # Create a button to change the font of the note
        # Create a button to select the save path
        select_path_button = tk.Button(master, text="Select path",bg = "red", command=self.select_path)
        select_path_button.pack()

        # Create a button to save the notes
        self.save_button = tk.Button(master, text="Save",bg = "yellow", command=self.save_notes)
        self.save_button.pack()

        self.save_path = os.getcwd()
        self.font = Font(font=self.note_text['font'])



    def select_path(self):
        self.save_path = askdirectory()

    def save_notes(self):
        # Get the contents of the text widget
        notes = self.note_text.get("1.0", "end-1c")
        title = self.title_entry.get()
        file_name = f"{title}.txt" if title else "notes.txt"
        file_path = os.path.join(self.save_path, file_name)
        i = 0
        while os.path.exists(file_path):
            i += 1
            file_name = f"{title}({i}).txt" if title else "Your File.txt"
            file_path = os.path.join(self.save_path, file_name)
        
        with open(file_path, "w") as f:
            f.write(notes)

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
