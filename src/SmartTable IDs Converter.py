import threading
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def run_pipeline(input_file, progress_bar):
    try:
        # Start the progress bar
        progress_bar.start()
          
        # Read TXT file as dataframe, by splitting by // ,by ignoring the first line that says Genes of pathway and by using python engine for the specific seperator
        df = pd.read_csv(input_file, header=None, sep=" // ", comment="Genes of pathway", engine='python')

        # Convert columns to rows
        df_t = df.T

        # Write the dataframe to the text file efficiently
        with open(input_file, 'w') as f:
            f.write(
                df_t.to_csv(sep="\t", lineterminator="\n", index=False, doublequote= False, header=False)
            )      

        progress_bar.stop()
        messagebox.showinfo("Success", f"Input ID's file format converted")

    except Exception as e:
        progress_bar.stop()
        messagebox.showerror("Error", str(e))

def start_thread():
    input_file = input_file_var.get()

    if not input_file:
        messagebox.showwarning("Input Error", "Please select an input TXT file.")
        return
    
    # Start command in a new thread
    thread = threading.Thread(target=run_pipeline, args=(input_file, progress_bar))
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

# Progress Bar (indeterminate)
progress_bar = ttk.Progressbar(app, mode="indeterminate", length=200)
progress_bar.grid(row=1, column=0, columnspan=3, padx=10, pady=20)

# Start button
tk.Button(app, text="Run program", command=start_thread).grid(row=2, column=1, padx=10, pady=20)

app.mainloop()
