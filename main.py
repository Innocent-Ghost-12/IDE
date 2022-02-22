from tkinter import *
from tkinter.filedialog import *
import subprocess

file_path = ''

def set_file_path(path):
    global file_path
    file_path = path

def run():
    if file_path != '':
        command = f'python {file_path}'
    else:
        save_as()
        command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
    output, errors = process.communicate()
    code_output.insert(END, output)
    code_output.insert(END, errors)

def new():
    editor.delete('1.0', END)

def open_file():
    path = askopenfilename(filetypes=[('All Files', '*.*'),
                                        ('Python Files', '*.py'),
                                        ('Text Document', '*.txt')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert(1.0, code)
        set_file_path(path)

def save():
    code = editor.get('1.0',END)
    exec(code)

def save_as():
    if file_path=='':
        path = asksaveasfilename(filetypes=[('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

compiler = Tk()

compiler.title("IDE Project")

menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New', command=new)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save as', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File',menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run',menu=run_bar)

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()


compiler.mainloop()