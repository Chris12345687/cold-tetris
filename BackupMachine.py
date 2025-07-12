import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
import shutil
import os

def backup_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        dir_name = os.path.dirname(file_path)
        base_name = os.path.basename(file_path)
        file_name, file_ext = os.path.splitext(base_name)
        backup_name = f"{file_name}_backup{file_ext}"
        backup_path = os.path.join(dir_name, backup_name)

        try:
            shutil.copy2(file_path, backup_path)
            messagebox.showinfo("Success", f"Backup created:\n{backup_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create backup:\n{e}")

def backup_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        parent_dir = os.path.dirname(folder_path)
        original_folder_name = os.path.basename(folder_path)
        backup_folder_name = f"{original_folder_name}_backup"
        backup_folder_path = os.path.join(parent_dir, backup_folder_name)

        try:
            if os.path.exists(backup_folder_path):
                if not messagebox.askyesno("Folder exists", f"{backup_folder_path} already exists.\nOverwrite it?"):
                    return
                shutil.rmtree(backup_folder_path)

            shutil.copytree(folder_path, backup_folder_path)
            messagebox.showinfo("Success", f"Backup folder created:\n{backup_folder_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create backup folder:\n{e}")

# Build UI
app = ttk.Window(title="The Backup Machine", themename="darkly", size=(400, 300))

ttk.Label(app, text="The Backup Machine", font=("Helvetica", 20, "bold")).pack(pady=20)

ttk.Button(app, text="Backup File", bootstyle="success", command=backup_file).pack(pady=10)
ttk.Button(app, text="Backup Folder", bootstyle="info", command=backup_folder).pack(pady=10)

app.mainloop()
