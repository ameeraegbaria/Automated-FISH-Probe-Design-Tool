import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np
from Bio.SeqUtils import MeltingTemp as mt
import os

def gc_content(seq):
    return (seq.count("G") + seq.count("C")) / len(seq) * 100

def design_probes(sequence, probe_length=25, gc_min=40, gc_max=60, tm_min=50, tm_max=70, overlap=0):
    probes = []
    step = probe_length - overlap
    
    for i in range(0, len(sequence) - probe_length + 1, step):
        probe = sequence[i:i+probe_length]
        gc = gc_content(probe)
        tm = mt.Tm_NN(probe)
        
        if gc_min <= gc <= gc_max and tm_min <= tm <= tm_max:
            probes.append({
                'Probe': probe,
                'GC_Content': round(gc, 2),
                'Tm': round(tm, 2),
                'Start': i + 1,
                'End': i + probe_length
            })
    
    return probes

def save_results(probes, file_type):
    if not probes:
        messagebox.showerror("Error", "No probes generated.")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=f".{file_type}", 
                                             filetypes=[(f"{file_type.upper()} files", f"*.{file_type}"), ("All Files", "*.*")])
    if not file_path:
        return
    
    if file_type == "csv":
        df = pd.DataFrame(probes)
        df.to_csv(file_path, index=False)
    elif file_type == "fasta":
        with open(file_path, "w") as fasta:
            for idx, probe in enumerate(probes, start=1):
                fasta.write(f">Probe_{idx}\n{probe['Probe']}\n")
    
    messagebox.showinfo("Success", f"File saved: {file_path}")

def run_design():
    global probes  # Declare probes as a global variable
    sequence = seq_entry.get("1.0", "end-1c").upper()
    if not sequence:
        messagebox.showerror("Error", "Please enter a DNA sequence.")
        return
    
    try:
        probe_length = int(length_var.get())
        gc_min = float(gc_min_var.get())
        gc_max = float(gc_max_var.get())
        tm_min = float(tm_min_var.get())
        tm_max = float(tm_max_var.get())
        overlap = int(overlap_var.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid numerical values.")
        return
    
    probes = design_probes(sequence, probe_length, gc_min, gc_max, tm_min, tm_max, overlap)
    result_var.set(f"Generated {len(probes)} probes.")

def save_csv():
    global probes
    save_results(probes, "csv")

def save_fasta():
    global probes
    save_results(probes, "fasta")

app = tk.Tk()
app.title("FISH Probe Design Tool")
app.geometry("500x500")

# Input fields
tk.Label(app, text="DNA Sequence:").pack()
seq_entry = tk.Text(app, height=5, width=50)
seq_entry.pack()

tk.Label(app, text="Probe Length:").pack()
length_var = tk.StringVar(value="25")
tk.Entry(app, textvariable=length_var).pack()

tk.Label(app, text="GC Min:").pack()
gc_min_var = tk.StringVar(value="40")
tk.Entry(app, textvariable=gc_min_var).pack()

tk.Label(app, text="GC Max:").pack()
gc_max_var = tk.StringVar(value="60")
tk.Entry(app, textvariable=gc_max_var).pack()

tk.Label(app, text="Tm Min:").pack()
tm_min_var = tk.StringVar(value="50")
tk.Entry(app, textvariable=tm_min_var).pack()

tk.Label(app, text="Tm Max:").pack()
tm_max_var = tk.StringVar(value="70")
tk.Entry(app, textvariable=tm_max_var).pack()

tk.Label(app, text="Overlap:").pack()
overlap_var = tk.StringVar(value="0")
tk.Entry(app, textvariable=overlap_var).pack()

# Buttons
tk.Button(app, text="Generate Probes", command=run_design).pack()
result_var = tk.StringVar()
tk.Label(app, textvariable=result_var).pack()
tk.Button(app, text="Save as CSV", command=save_csv).pack()
tk.Button(app, text="Save as FASTA", command=save_fasta).pack()

app.mainloop()
