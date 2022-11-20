# Import the libraries tk, ttk, filedialog
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import subprocess
import os

# Create a function to get chromat directory
def select_chromat_folder():
    chromat_text.delete('1.0', 'end-1c')
    chromat_dir = filedialog.askdirectory(initialdir=os.getcwd())
    chromat_text.insert('1.0', chromat_dir)

# Create a function to get chromat directory
def select_phd_folder():
    phd_text.delete('1.0', 'end-1c')
    phd_dir = filedialog.askdirectory(initialdir=os.getcwd())
    phd_text.insert('1.0', phd_dir)

# Create a function to open the file dialog
def select_vector_file():
    vector_text.delete('1.0', 'end-1c')

    # Specify the file types
    filetypes = (('text files', '*.txt'),
                 ('all files', '*.*'))
  
    # Show the open file dialog by specifying path
    f = filedialog.askopenfile(filetypes=filetypes)
    vector_sequence = f.name
  
    # Insert the text extracted from file in a textfield
    vector_text.insert('1.0', vector_sequence)

# Execute contigs.py
def execute():
	chromat_dir = chromat_text.get('1.0', 'end-1c')
	phd_dir = phd_text.get('1.0', 'end-1c')
	vector_sequence = vector_text.get('1.0', 'end-1c')
	minimum_match = minmatch_text.get('1.0', 'end-1c')
	minimum_score = minscore_text.get('1.0', 'end-1c')
	
	if chromat_dir and phd_dir and vector_sequence and \
		minimum_match and minimum_score:

		try:
			subprocess.call([
				"python3", 
				"contigs.py", 
				"--chromat_dir", 
				chromat_dir,
				"--phd_dir", 
				phd_dir,
				"--vector_sequence",
				vector_sequence,
				"--minimum_match",
				minimum_match,
				"--minimum_score",
				minimum_score
			])
		except Exception as err:
			print(err)

# Create a GUI app
app = tk.Tk()
  
# Specify the title and dimensions to app
app.title('Contigs Creation')
app.geometry('450x400')
app.minsize(450, 400)
app.maxsize(450, 400)

# Create an open file button
chromat_button = ttk.Button(app, text='Select Chromatograms Folder',
                         command=select_chromat_folder)
chromat_button.grid(row=0, column=0, columnspan=4, sticky='w', padx=10, pady=10)

# Create a textfield
chromat_text = tk.Text(app, width=50, height=2)
chromat_text.grid(row=1, column=0, columnspan=4, sticky='nsew', padx=10)

# Create an open file button
phd_button = ttk.Button(app, text='Select Phd Folder',
                         command=select_phd_folder)
phd_button.grid(row=2, column=0, columnspan=4, sticky='w', padx=10, pady=10)

# Create a textfield
phd_text = tk.Text(app, width=50, height=2)
phd_text.grid(row=3, column=0, columnspan=4, sticky='nsew', padx=10)

# Create an open file button
vector_button = ttk.Button(app, text='Select Vector File',
                         command=select_vector_file)
vector_button.grid(row=4, column=0, columnspan=4, sticky='w', padx=10, pady=10)

# Create a textfield
vector_text = tk.Text(app, width=50, height=2)
vector_text.grid(row=5, column=0, columnspan=4, sticky='nsew', padx=10)

# Create a label
minmatch_label = ttk.Label(app, text="Minmatch:")
minmatch_label.grid(row=6, column=0, sticky='nsew', padx=10, pady=10)

# Create a textfield
minmatch_text = tk.Text(app, width=10, height=2)
minmatch_text.grid(row=6, column=1, sticky='nsew', padx=10,  pady=10)

# Create a label
minscore_label = ttk.Label(app, text="Minscore:")
minscore_label.grid(row=6, column=2, sticky='nsew', padx=10, pady=10)

# Create a textfield
minscore_text = tk.Text(app, width=10, height=2)
minscore_text.grid(row=6, column=3, sticky='nsew', padx=10,  pady=10)

# Create an open file button
run = ttk.Button(app, text='Execute',
                         command=execute)
run.grid(row=7, column=0, sticky='w', padx=10, pady=10)
  
# Make infinite loop for displaying app on the screen
app.mainloop()