import os
import threading
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def run_pipeline(input_file, seperator, progress_bar):

    # Start the progress bar
    progress_bar.start()

    # Select input directory
    input_directory = os.path.dirname(input_file)

    # Select input file
    infile = str(os.path.basename(input_file)).replace(" ","\ ")
    
    # Change to the input file's directory
    os.chdir(input_directory)

    # Run command
    if seperator:
        command = f"sed -i '/Genes of pathway/d' {infile}; sed -i 's| // |\\n|g' {infile}"
    else:
        command = f"sed -i 's/,/\\n/g' {infile}"
    
    try:
        subprocess.run(["wsl", "bash", "-c", command], check=True, creationflags=subprocess.CREATE_NO_WINDOW)
        progress_bar.stop()
        messagebox.showinfo("Success","Input ID's file format converted")

    except subprocess.CalledProcessError as e:
        progress_bar.stop()
        print(f"Error: {e}")
        
def start_thread():
    input_file = input_file_var.get()
    seperator = seperator_var.get()

    if not input_file:
        messagebox.showwarning("Input Error", "Please select an input TXT file.")
        return
    
    # Start command in a new thread
    thread = threading.Thread(target=run_pipeline, args=(input_file, seperator, progress_bar))
    thread.start()

def select_file():
    file_path = filedialog.askopenfilename()
    input_file_var.set(file_path)

# Set up tkinter app
app = tk.Tk()
app.title("SmartTable IDs Converter")

# Input file selection
input_file_var = tk.StringVar()
tk.Label(app, text="Input TXT File:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
tk.Entry(app, textvariable=input_file_var, width=40).grid(row=0, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=select_file).grid(row=0, column=2, padx=10, pady=10)

# Checkbox for additional option
seperator_var = tk.BooleanVar(value=True)
tk.Checkbutton(app, text="Identifiers derived from SmartTable", variable=seperator_var).grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Progress Bar (indeterminate)
progress_bar = ttk.Progressbar(app, mode="indeterminate", length=200)
progress_bar.grid(row=2, column=0, columnspan=3, padx=10, pady=20)

# Start button
tk.Button(app, text="Run program", command=start_thread).grid(row=3, column=1, padx=10, pady=20)

app.mainloop()
