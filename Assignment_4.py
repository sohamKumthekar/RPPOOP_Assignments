from tkinter import Tk, Menu, messagebox, Text, colorchooser, filedialog, Toplevel, Label


def copy_text():
    text = text_box.get("1.0", "end-1c")
    root.clipboard_clear()
    root.clipboard_append(text)

def cut_text():
    text = text_box.get("1.0", "end-1c")
    root.clipboard_clear()
    root.clipboard_append(text)
    text_box.delete("1.0", "end")

def paste_text():
    text = root.clipboard_get()
    text_box.insert("insert", text)

def change_font_color():
    color = colorchooser.askcolor()
    if color:
        text_box.config(fg=color[1])

def save_text():
    text = text_box.get("1.0", "end-1c")
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(text)
            messagebox.showinfo("Save", "Text saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the text: {str(e)}")
    else:
        messagebox.showwarning("Save", "No file selected.")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_box.delete("1.0", "end")
            text_box.insert("1.0", file.read())

def about_dialog():
    about_dialog = Toplevel(root)
    about_dialog.title("About")
    about_dialog.geometry("300x200")
    about_label = Label(about_dialog, text="This is a text editor project using Tkinter.")
    about_label.pack(pady=20)


root = Tk()  
root.geometry("600x600")
root.title("Text Editor")
menubar = Menu(root, font=("Verdana",15)) 
file = Menu(menubar, tearoff=0, activebackground="red")  
file.add_command(label="New",command=cut_text)  
file.add_command(label="Open",command=open_file)  
file.add_command(label="Save", command=save_text)  
file.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file)



edit = Menu(menubar, tearoff=0, activebackground="red")
edit.add_command(label="Clear Text", command=cut_text)  
edit.add_command(label="Select all", command=copy_text)  
edit.add_command(label="Paste", command=paste_text)  
edit.add_command(label="Text Color", command=change_font_color)  
menubar.add_cascade(label="Edit", menu=edit)  



help = Menu(menubar, tearoff=0)  
help.add_command(label="About", activebackground="red", command=about_dialog)  
menubar.add_cascade(label="Help", menu=help)  



root.config(menu=menubar) 



text_box = Text(root, width=70, height=90)
text_box.pack()


root.mainloop()