import os
import tkinter as tk
from tkinter import filedialog, messagebox, Label, Entry, Button
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(pdf_files, output_file):
    pdf_writer = PdfWriter()
    for pdf_file in pdf_files:
        pdf_reader = PdfReader(pdf_file)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])
    with open(output_file, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
    return True

def select_files():
    file_path = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def select_output():
    folder_path = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, folder_path)

def start_merge():
    pdf_files = root.tk.splitlist(file_entry.get())
    output_path = output_entry.get() + '/merged_output.pdf'
    if merge_pdfs(pdf_files, output_path):
        messagebox.showinfo("Success", "PDFs merged successfully!")
    else:
        messagebox.showerror("Error", "Failed to merge PDFs.")

root = tk.Tk()
root.title("PDF Merger")

Label(root, text="Select PDF Files:").pack()
file_entry = Entry(root, width=50)
file_entry.pack(padx=10, pady=5)
Button(root, text="Browse", command=select_files).pack()

Label(root, text="Select Output Directory:").pack()
output_entry = Entry(root, width=50)
output_entry.pack(padx=10, pady=5)
Button(root, text="Browse", command=select_output).pack()

Button(root, text="Merge PDFs", command=start_merge).pack(pady=10)

root.mainloop()
